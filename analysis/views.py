from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ResultForm
from django.contrib import messages
from .models import Result
import os
import re
from random import choice

videoID = ""
videoPath = ""

def showContent(request):
    db = Result.objects.all()
    return render(request, 'analysis/demo-content.html', {"list": db})

def SearchContent(request):
    db = Result.objects.all()
    return render(request, 'analysis/demo-content.html', {"list": db})

def googleForm(request):
    return render(request, 'analysis/googleForm.html')

@login_required
def classification(request):
    return render(request, 'analysis/classification.html')


@login_required
def category(request):
    global videoID
    global videoPath
    targetDb = []
    db = Result.objects.all()
    if request.method == 'POST':
        Video_Quality = request.POST.getlist('Quality', '')
        Ruminating_Foraging = request.POST.getlist('Ruminating/Foraging', '')
        State_of_Locomotion = request.POST.getlist('State_of_Locomotion', '')
        Is_a_calf_visible = request.POST.getlist('Is_a_calf_visible', '')
        Other_caribou_visible_excluding_own_calf = request.POST.getlist('Other_caribou_visible_excluding_own_calf', '')
        Does_the_cow_have_antlers = request.POST.getlist('Does_the_cow_have_antlers', '')
        What_part_of_the_habitat_is_visible = request.POST.getlist('What_part_of_the_habitat_is_visible', '')
        Potential_insect_avoidance_behavior = request.POST.getlist('Potential_insect_avoidance_behavior', '')
        What_is_the_PREDOMINANT_vegetation = request.POST.getlist('What_is_the_PREDOMINANT_vegetation', '')
        Habitat_features_visible = request.POST.getlist('Habitat_features_visible', '')

        # get queries that satisfy users' selection
        if Video_Quality:
            return queryField(request, db, targetDb, Video_Quality, 'Video_Quality')

        if Ruminating_Foraging:
            return queryField(request, db, targetDb, Ruminating_Foraging, 'Ruminating_Foraging')

        if State_of_Locomotion:
            return queryField(request, db, targetDb, State_of_Locomotion, 'State_of_Locomotion')
        if Is_a_calf_visible:
            return queryField(request, db, targetDb, Is_a_calf_visible, 'Is_a_calf_visible')
        if Other_caribou_visible_excluding_own_calf:
            return queryField(request, db, targetDb, Other_caribou_visible_excluding_own_calf, 'Other_caribou_visible_excluding_own_calf')
        if Does_the_cow_have_antlers:
            return queryField(request, db, targetDb, Does_the_cow_have_antlers, 'Does_the_cow_have_antlers')

        # Special case: multiChoice
        if Potential_insect_avoidance_behavior:
            return queryField(request, db, targetDb, Potential_insect_avoidance_behavior, 'Potential_insect_avoidance_behavior')

        if What_part_of_the_habitat_is_visible:
            return queryField(request, db, targetDb, What_part_of_the_habitat_is_visible, 'What_part_of_the_habitat_is_visible')
        if What_is_the_PREDOMINANT_vegetation:
            return queryField(request, db, targetDb, What_is_the_PREDOMINANT_vegetation, 'What_is_the_PREDOMINANT_vegetation')
        if Habitat_features_visible:
            return queryField(request, db, targetDb, Habitat_features_visible, 'Habitat_features_visible')

    return render(request, 'analysis/category.html')

@login_required
def targetVideo(request):
    global videoID
    global videoPath
    videoID = getRandVideoID()
    videoPath = "/videos/" + videoID + ".mp4"
    return render(request, 'analysis/targetVideo.html', {'videoPath': videoPath, 'videoID': videoID})

# current use
@login_required
def ResultPrefilled(request, video_id):
    searchQuery = Result.objects.filter(File_Name=video_id)
    # if the query exists
    if searchQuery.exists():
        result = Result.objects.get(File_Name=video_id)
        prefilledName = {'Observer_Name': request.user.first_name + ' ' + request.user.last_name}

        if request.method == "POST":
            form = ResultForm(instance=result, data=request.POST, initial=prefilledName)
            if form.is_valid():
                form.save()
                messages.success(request, f'Analysis for video:{video_id} has been submitted successfully!')
                return redirect('analysis-category')
        else:
            # make prefilled fields read-only beginning ###################
            form = ResultForm(instance=result, initial=prefilledName)
            if result.Video_Quality != '':
                form.fields['Video_Quality'].disabled = True

            if result.Ruminating_Foraging != '':
                form.fields['Ruminating_Foraging'].disabled = True

            if result.State_of_Locomotion != '':
                form.fields['State_of_Locomotion'].disabled = True

            if result.Is_a_calf_visible != '':
                form.fields['Is_a_calf_visible'].disabled = True

            if result.Other_caribou_visible_excluding_own_calf != '':
                form.fields['Other_caribou_visible_excluding_own_calf'].disabled = True

            if result.Does_the_cow_have_antlers != '':
                form.fields['Does_the_cow_have_antlers'].disabled = True

            if result.Potential_insect_avoidance_behavior:
                form.fields['Potential_insect_avoidance_behavior'].disabled = True

            if result.What_part_of_the_habitat_is_visible != '':
                form.fields['What_part_of_the_habitat_is_visible'].disabled = True

            if result.What_is_the_PREDOMINANT_vegetation != '':
                form.fields['What_is_the_PREDOMINANT_vegetation'].disabled = True

            if result.Habitat_features_visible != '':
                form.fields['Habitat_features_visible'].disabled = True
            # make prefilled fields read-only ending ###################
    # otherwise, create a new query
    else:
        prefilledName = {
            'File_Name': videoID,
            'Observer_Name': request.user.first_name + ' ' + request.user.last_name}
        if request.method == "POST":
            form = ResultForm(data=request.POST, initial=prefilledName)
            if form.is_valid():
                form.save()
                return redirect('analysis-category')
        else:
            form = ResultForm(initial=prefilledName)
    return render(request, 'analysis/classification.html', {'form': form, 'videoPath': videoPath, 'videoID': videoID})



# -------Used functions-------
def getRandVideoID():
    pwd = os.getcwd()
    video_Path = pwd+'\\analysis\\static\\videos'
    fileList=getAllFile(video_Path)
    # randomly choose one video
    randomVideo = choice(fileList)
    return randomVideo

def getAllFile( path ):
    # initialize list to store path and name of all files
    allPath = []
    #  get the list of all files and directories in the specified directory
    fileList = os.listdir( path )
    for eachFile in fileList:
        videoName = re.search(r'(.+?)\.', eachFile).group(1)
        # append file names to the list
        allPath.append(videoName)
    return allPath

def queryField( request, db, targetDb, fieldQuery, fieldName ):
    global videoID
    global videoPath

    for fieldElement in fieldQuery:
        targetData = db.filter(**{fieldName: fieldElement})
        if targetData:
            targetDb.extend(targetData)
    # get those videos id
    videoList = []
    for key in targetDb:
        videoList.append(key.pk)
    if videoList:
        videoID = choice(videoList)
        videoPath = "/videos/" + videoID + ".mp4"
        # print(targetData)
        return render(request, 'analysis/targetVideo.html',
                      {'videoPath': videoPath, 'videoID': videoID})
    else:
        messages.success(request,
                         f'No videos satisfied your preference so far, sorry, please try others.')
        return redirect('analysis-category')


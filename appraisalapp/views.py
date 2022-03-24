from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.urls import reverse

agent_list = ['CRO']
manager_list = ['Manager','Team Leader']

def IndexPage(request):
    logout(request)
    return render(request, "common/index.html")

def LoginPage(request):
    if request.method == "POST":
        username = request.POST["user"]
        password = request.POST["pass"]
        user = authenticate(username=username, password=password)
        # check = PartA_Appraisee.objects.get(emp_id=username)
        if user is not None:
            # user_login
            login(request, user)
            desi = request.user.profile.emp_desi
            if desi in agent_list:
                return redirect("/appraisal/notice")
            elif desi in manager_list:
                return redirect("/appraisal/manager-dashboard")
            # if check:
            #     return redirect("view",id=username)
            else:
                messages.info(request, 'Invalid Designation !')
                return redirect("/appraisal/")
        else:
            messages.info(request, 'Invalid user !')
            return redirect("/appraisal/login")
    else:
        messages.info(request,'Invalid Request !')
        return redirect("/appraisal/")

@login_required
def managerDashboard(request):
    emp_id = request.user.profile.emp_id
    profile = Profile.objects.filter(Q(emp_rm1_id=emp_id) | Q(emp_rm2_id=emp_id) | Q(emp_rm3_id=emp_id))
    data = {"profile": profile}
    return render(request, "manager/manager_dashboard.html",data)

@login_required
def Notice(request):
    user = request.user
    emp_id = Profile.objects.get(user=user).emp_id
    if PartA_Appraisee.objects.filter(emp_id=emp_id):
        profile = Profile.objects.get(user=user)
        data = {"profile":profile}
        return render(request, "common/notice.html", data)
    else:
        messages.info(request, "Waiting for your manager to complete it! Please Check later.")
        return redirect("/appraisal/")

@login_required
def part_a_save(request):
    user = request.user
    emp_id = Profile.objects.get(user=user).emp_id
    if PartA_Appraisee.objects.filter(emp_id=emp_id):
        if request.method == "POST":
            parameter_1_rating_agent = request.POST["parameter_1_rating_agent"]
            parameter_1_comment_agent = request.POST.get("parameter_1_comment_agent")
            parameter_2_rating_agent = request.POST.get("parameter_2_rating_agent")
            parameter_2_comment_agent = request.POST.get("parameter_2_comment_agent")
            parameter_3_rating_agent = request.POST.get("parameter_3_rating_agent")
            parameter_3_comment_agent = request.POST.get("parameter_3_comment_agent")
            parameter_4_rating_agent = request.POST.get("parameter_4_rating_agent")
            parameter_4_comment_agent = request.POST.get("parameter_4_comment_agent")
            parameter_5_rating_agent = request.POST.get("parameter_5_rating_agent")
            parameter_5_comment_agent = request.POST.get("parameter_5_comment_agent")
            parameter_6_rating_agent = request.POST.get("parameter_6_rating_agent")
            parameter_6_comment_agent = request.POST.get("parameter_6_comment_agent")

            e=PartA_Appraisee.objects.get(emp_id=emp_id)
            e.parameter_1_rating_agent = parameter_1_rating_agent
            e.parameter_1_comment_agent = parameter_1_comment_agent
            e.parameter_2_rating_agent = parameter_2_rating_agent
            e.parameter_2_comment_agent = parameter_2_comment_agent
            e.parameter_3_rating_agent = parameter_3_rating_agent
            e.parameter_3_comment_agent = parameter_3_comment_agent
            e.parameter_4_rating_agent = parameter_4_rating_agent
            e.parameter_4_comment_agent = parameter_4_comment_agent
            e.parameter_5_rating_agent = parameter_5_rating_agent
            e.parameter_5_comment_agent = parameter_5_comment_agent
            e.parameter_6_rating_agent = parameter_6_rating_agent
            e.parameter_6_comment_agent = parameter_6_comment_agent
            e.save()
            return redirect("/appraisal/partb")
        else:
            try:
                profile = Profile.objects.get(user=user)
                sup = profile.emp_rm3
                rev = profile.emp_rm1
                sup_desi = Profile.objects.get(emp_id=profile.emp_rm3_id).emp_desi
                rev_desi = Profile.objects.get(emp_id=profile.emp_rm1_id).emp_desi
                parta = PartA_Appraisee.objects.get(agent=profile)
                data = {"profile": profile,"parta":parta,"sup":sup,"sup_desi":sup_desi,"rev":rev,"rev_desi":rev_desi}
                return render(request, "agent/part-a-form.html", data)
            except PartA_Appraisee.DoesNotExist:
                messages.info(request,"Waiting for your manager to complete it! Please Check later.")
                return redirect("/appraisal/")
    else:
        messages.info(request, "Waiting for your manager to complete it! Please Check later.")
        return redirect("/appraisal/")

def manager_part_a_save(request,id):
    if request.method == "POST":
        supervisor_name = request.POST["sup_name"]
        supervisor_desig = request.POST["sup_desg"]
        reviewers_name = request.user.profile.emp_name
        reviewers_desig = request.user.profile.emp_desi

        parameter_1 = request.POST["parameter_1"]
        parameter_1_score = int(request.POST["parameter_1_score"])
        parameter_1_rating = int(request.POST["parameter_1_rating"])
        parameter_1_rating = parameter_1_score*parameter_1_rating/100
        parameter_1_comment = request.POST.get("parameter_1_comment")

        parameter_2 = request.POST.get("parameter_2")
        if parameter_2:
            parameter_2_score = int(request.POST.get("parameter_2_score"))
            parameter_2_rating = int(request.POST.get("parameter_2_rating"))
            parameter_2_rating = parameter_2_score*parameter_2_rating/100
            parameter_2_comment = request.POST.get("parameter_2_comment")

        parameter_3 = request.POST.get("parameter_3")
        if parameter_3:
            parameter_3_score = int(request.POST.get("parameter_3_score"))
            parameter_3_rating = int(request.POST.get("parameter_3_rating"))
            parameter_3_rating = parameter_3_score*parameter_3_rating/100
            parameter_3_comment = request.POST.get("parameter_3_comment")

        parameter_4 = request.POST.get("parameter_4")
        if parameter_4:
            parameter_4_score = int(request.POST.get("parameter_4_score"))
            parameter_4_rating = int(request.POST.get("parameter_4_rating"))
            parameter_4_rating = parameter_4_score*parameter_4_rating/100
            parameter_4_comment = request.POST.get("parameter_4_comment")

        parameter_5 = request.POST.get("parameter_5")
        if parameter_5:
            parameter_5_score = int(request.POST.get("parameter_5_score"))
            parameter_5_rating = int(request.POST.get("parameter_5_rating"))
            parameter_5_rating = parameter_5_score*parameter_5_rating/100
            parameter_5_comment = request.POST.get("parameter_5_comment")

        parameter_6 = request.POST.get("parameter_6")
        if parameter_6:
            parameter_6_score = int(request.POST.get("parameter_6_score"))
            parameter_6_rating = int(request.POST.get("parameter_6_rating"))
            parameter_6_rating = parameter_6_score*parameter_6_rating/100
            parameter_6_comment = request.POST.get("parameter_6_comment")

        mgr_comment = request.POST.get("Spe_other")
        profile = Profile.objects.get(emp_id=id)

        e = PartA_Appraisee()
        e.agent = profile
        e.emp_id = profile.emp_id
        e.emp_name = profile.emp_name
        e.emp_desi = profile.emp_desi
        e.emp_rm1_id = profile.emp_rm1_id
        e.emp_rm2_id = profile.emp_rm2_id
        e.emp_rm3_id = profile.emp_rm3_id
        e.emp_process = profile.emp_process
        e.supervisor_name = supervisor_name
        e.supervisor_desig = supervisor_desig
        e.reviewers_name = reviewers_name
        e.reviewers_desig = reviewers_desig
        e.parameter_1 = parameter_1
        e.parameter_1_score = parameter_1_score
        e.parameter_1_rating = parameter_1_rating
        e.parameter_1_comment = parameter_1_comment
        e.parameter_2 = parameter_2
        if parameter_2:
            e.parameter_2_score = parameter_2_score
            e.parameter_2_rating = parameter_2_rating
            e.parameter_2_comment = parameter_2_comment
        e.parameter_3 = parameter_3
        if parameter_3:
            e.parameter_3_score = parameter_3_score
            e.parameter_3_rating = parameter_3_rating
            e.parameter_3_comment = parameter_3_comment
        e.parameter_4 = parameter_4
        if parameter_4:
            e.parameter_4_score = parameter_4_score
            e.parameter_4_rating = parameter_4_rating
            e.parameter_4_comment = parameter_4_comment
        e.parameter_5 = parameter_5
        if parameter_5:
            e.parameter_5_score = parameter_5_score
            e.parameter_5_rating = parameter_5_rating
            e.parameter_5_comment = parameter_5_comment
        e.parameter_6 = parameter_6
        if parameter_6:
            e.parameter_6_score = parameter_6_score
            e.parameter_6_rating = parameter_6_rating
            e.parameter_6_comment = parameter_6_comment
        e.mangr_special_comment = mgr_comment
        e.save()
        return redirect("manpartb",id=id)

    else:
        try:
            PartA_Appraisee.objects.get(emp_id=id)
            messages.info(request,"Part A for this Agent is Already done! Redirecting you to Part B.")
            return redirect("manpartb", id=id)
        except PartA_Appraisee.DoesNotExist:
            profile = Profile.objects.get(emp_id=id)
            rm3_desi = Profile.objects.get(emp_id=id).emp_rm3_id
            print(rm3_desi,"before")
            rm3_desi = Profile.objects.get(emp_id=rm3_desi).emp_desi
            print(rm3_desi,"After")
            data = {"profile": profile,"rm3_desi":rm3_desi}
            return render(request, "manager/manager_part-a-form.html", data)


def part_b_save(request):
    user = request.user
    if request.method=="POST":
        # user = request.user
        one_comment = request.POST.get("one_com")
        two_comment = request.POST.get("two_com")
        three_comment = request.POST.get("three_com")
        four_comment = request.POST.get("four_com")
        five_comment = request.POST.get("five_com")
        six_comment = request.POST.get("six_com")
        seven_comment = request.POST.get("seven_com")
        eight_comment = request.POST.get("eight_com")
        nine_comment = request.POST.get("nine_com")
        ten_comment = request.POST.get("ten_com")
        eleven_comment = request.POST.get("eleven_com")
        twelve_comment = request.POST.get("twelve_com")
        thirteen_comment = request.POST.get("thirteen_com")
        fourteen_comment = request.POST.get("fourteen_com")
        fifteen_comment = request.POST.get("fifteen_com")
        sixteen_comment = request.POST.get("sixteen_com")
        seventeen_comment = request.POST.get("seventeen_com")
        eighteen_comment = request.POST.get("eighteen_com")
        one_comment_2 = request.POST.get("one_com2")
        two_comment_2 = request.POST.get("two_com2")
        three_comment_2 = request.POST.get("three_com2")
        four_comment_2 = request.POST.get("four_com2")
        five_comment_2 = request.POST.get("five_com2")
        six_comment_2 = request.POST.get("six_com2")
        seven_comment_2 = request.POST.get("seven_com2")
        eight_comment_2 = request.POST.get("eight_com2")
        nine_comment_2 = request.POST.get("nine_com2")
        ten_comment_2 = request.POST.get("ten_com2")
        eleven_comment_2 = request.POST.get("eleven_com2")
        one_comment_3 = request.POST.get("one_com3")
        two_comment_3 = request.POST.get("two_com3")
        three_comment_3 = request.POST.get("three_com3")
        four_comment_3 = request.POST.get("four_com3")
        five_comment_3 = request.POST.get("five_com3")
        six_comment_3 = request.POST.get("six_com3")
        seven_comment_3 = request.POST.get("seven_com3")
        eight_comment_3 = request.POST.get("eight_com3")
        one_comment_4 = request.POST.get("one_com4")
        two_comment_4 = request.POST.get("two_com4")
        three_comment_4 = request.POST.get("three_com4")
        four_comment_4 = request.POST.get("four_com4")
        five_comment_4 = request.POST.get("five_com4")
        six_comment_4 = request.POST.get("six_com4")
        seven_comment_4 = request.POST.get("seven_com4")
        eight_comment_4 = request.POST.get("eight_com4")
        nine_comment_4 = request.POST.get("nine_com4")
        ten_comment_4 = request.POST.get("ten_com4")
        eleven_comment_4 = request.POST.get("eleven_com4")
        twelve_comment_4 = request.POST.get("twelve_com4")
        thirteen_comment_4 = request.POST.get("thirteen_com4")
        fourteen_comment_4 = request.POST.get("fourteen_com4")
        fifteen_comment_4 = request.POST.get("fifteen_com4")
        sixteen_comment_4 = request.POST.get("sixteen_com4")
        seventeen_comment_4 = request.POST.get("seventeen_com4")
        eighteen_comment_4 = request.POST.get("eighteen_com4")
        nineteen_comment_4 = request.POST.get("nineteen_com4")
        twenty_comment_4 = request.POST.get("twenty_com4")
        twentyone_comment_4 = request.POST.get("twentyone_com4")
        twentytwo_comment_4 = request.POST.get("twentytwo_com4")
        twentythree_comment_4 = request.POST.get("twentythree_com4")

        one_rating = request.POST["one_rat"]
        two_rating = request.POST["two_rat"]
        three_rating = request.POST["three_rat"]
        four_rating = request.POST["four_rat"]
        five_rating = request.POST["five_rat"]
        six_rating = request.POST["six_rat"]
        seven_rating = request.POST["seven_rat"]
        eight_rating = request.POST["eight_rat"]
        nine_rating = request.POST["nine_rat"]
        ten_rating = request.POST["ten_rat"]
        eleven_rating = request.POST["eleven_rat"]
        twelve_rating = request.POST["twelve_rat"]
        thirteen_rating = request.POST["thirteen_rat"]
        fourteen_rating = request.POST["fourteen_rat"]
        fifteen_rating = request.POST["fifteen_rat"]
        sixteen_rating = request.POST["sixteen_rat"]
        seventeen_rating = request.POST["seventeen_rat"]
        eighteen_rating = request.POST["eighteen_rat"]
        agent_table_1_total = [int(one_rating), int(two_rating), int(three_rating),
                             int(four_rating), int(five_rating), int(six_rating),
                             int(seven_rating), int(eight_rating), int(nine_rating),
                             int(ten_rating), int(eleven_rating), int(twelve_rating),
                             int(thirteen_rating), int(fourteen_rating), int(fifteen_rating),
                             int(sixteen_rating), int(seventeen_rating), int(eighteen_rating)]
        agent_table_1_total = round(sum(agent_table_1_total) / 18, 2)
        print(agent_table_1_total,"agent_table_1_total")
        one_rating_2 = request.POST["one_rat2"]
        two_rating_2 = request.POST["two_rat2"]
        three_rating_2 = request.POST["three_rat2"]
        four_rating_2 = request.POST["four_rat2"]
        five_rating_2 = request.POST["five_rat2"]
        six_rating_2 = request.POST["six_rat2"]
        seven_rating_2 = request.POST["seven_rat2"]
        eight_rating_2 = request.POST["eight_rat2"]
        nine_rating_2 = request.POST["nine_rat2"]
        ten_rating_2 = request.POST["ten_rat2"]
        eleven_rating_2 = request.POST["eleven_rat2"]
        agent_table_2_total = [int(one_rating_2),int(two_rating_2),int(three_rating_2),
                                int(four_rating_2),int(five_rating_2),int(six_rating_2),
                                int(seven_rating_2),int(eight_rating_2),int(nine_rating_2),
                                int(ten_rating),int(eleven_rating)]
        agent_table_2_total = round(sum(agent_table_2_total)/11,2)
        print(agent_table_2_total,"agent_table_2_total")
        one_rating_3 = request.POST["one_rat3"]
        two_rating_3 = request.POST["two_rat3"]
        three_rating_3 = request.POST["three_rat3"]
        four_rating_3 = request.POST["four_rat3"]
        five_rating_3 = request.POST["five_rat3"]
        six_rating_3 = request.POST["six_rat3"]
        seven_rating_3 = request.POST["seven_rat3"]
        eight_rating_3 = request.POST["eight_rat3"]
        agent_table_3_total = [int(one_rating_3),int(two_rating_3),int(three_rating_3),
                                int(four_rating_3),int(five_rating_3),int(six_rating),
                                int(seven_rating_3),int(eight_rating_3)]
        agent_table_3_total = round(sum(agent_table_3_total)/8,2)
        print(agent_table_3_total,"agent_table_3_total")
        one_rating_4 = request.POST["one_rat4"]
        two_rating_4 = request.POST["two_rat4"]
        three_rating_4 = request.POST["three_rat4"]
        four_rating_4 = request.POST["four_rat4"]
        five_rating_4 = request.POST["five_rat4"]
        six_rating_4 = request.POST["six_rat4"]
        seven_rating_4 = request.POST["seven_rat4"]
        eight_rating_4 = request.POST["eight_rat4"]
        nine_rating_4 = request.POST["nine_rat4"]
        ten_rating_4 = request.POST["ten_rat4"]
        eleven_rating_4 = request.POST["eleven_rat4"]
        twelve_rating_4 = request.POST["twelve_rat4"]
        thirteen_rating_4 = request.POST["thirteen_rat4"]
        fourteen_rating_4 = request.POST["fourteen_rat4"]
        fifteen_rating_4 = request.POST["fifteen_rat4"]
        sixteen_rating_4 = request.POST["sixteen_rat4"]
        seventeen_rating_4 = request.POST["seventeen_rat4"]
        eighteen_rating_4 = request.POST["eighteen_rat4"]
        nineteen_rating_4 = request.POST["nineteen_rat4"]
        twenty_rating_4 = request.POST["twenty_rat4"]
        twentyone_rating_4 = request.POST["twentyone_rat4"]
        twentytwo_rating_4 = request.POST["twentytwo_rat4"]
        twentythree_rating_4 = request.POST["twentythree_rat4"]
        agent_table_4_total = [int(one_rating_4),int(two_rating_4),int(three_rating_4),
                                int(four_rating_4),int(five_rating_4),int(six_rating_4),
                                int(seven_rating_4),int(eight_rating_4),int(nine_rating_4),
                                int(ten_rating_4),int(eleven_rating_4),int(twelve_rating_4),
                                int(thirteen_rating_4),int(fourteen_rating_4),int(fifteen_rating_4),
                                int(sixteen_rating_4),int(seventeen_rating_4),int(eighteen_rating_4),
                                int(nineteen_rating_4), int(twenty_rating_4), int(twentyone_rating_4),
                                int(twentytwo_rating_4), int(twentythree_rating_4)]
        agent_table_4_total = round(sum(agent_table_4_total)/23,2)
        print(agent_table_4_total,"agent_table_4_total")
        e=PartB_Appraisee.objects.get(emp_id=user.profile.emp_id)
        e.agent_table_1_total=agent_table_1_total
        e.agent_table_2_total=agent_table_2_total
        e.agent_table_3_total=agent_table_3_total
        e.agent_table_4_total=agent_table_4_total
        e.one_comment=one_comment
        e.two_comment=two_comment
        e.three_comment=three_comment
        e.four_comment=four_comment
        e.five_comment=five_comment
        e.six_comment=six_comment
        e.seven_comment=seven_comment
        e.eight_comment=eight_comment
        e.nine_comment=nine_comment
        e.ten_comment=ten_comment
        e.eleven_comment=eleven_comment
        e.twelve_comment=twelve_comment
        e.thirteen_comment=thirteen_comment
        e.fourteen_comment=fourteen_comment
        e.fifteen_comment=fifteen_comment
        e.sixteen_comment=sixteen_comment
        e.seventeen_comment=seventeen_comment
        e.eighteen_comment=eighteen_comment
        e.one_comment_2=one_comment_2
        e.two_comment_2=two_comment_2
        e.three_comment_2=three_comment_2
        e.four_comment_2=four_comment_2
        e.five_comment_2=five_comment_2
        e.six_comment_2=six_comment_2
        e.seven_comment_2=seven_comment_2
        e.eight_comment_2=eight_comment_2
        e.nine_comment_2=nine_comment_2
        e.ten_comment_2=ten_comment_2
        e.eleven_comment_2=eleven_comment_2
        e.one_comment_3=one_comment_3
        e.two_comment_3=two_comment_3
        e.three_comment_3=three_comment_3
        e.four_comment_3=four_comment_3
        e.five_comment_3=five_comment_3
        e.six_comment_3=six_comment_3
        e.seven_comment_3=seven_comment_3
        e.eight_comment_3=eight_comment_3
        e.one_comment_4=one_comment_4
        e.two_comment_4=two_comment_4
        e.three_comment_4=three_comment_4
        e.four_comment_4=four_comment_4
        e.five_comment_4=five_comment_4
        e.six_comment_4=six_comment_4
        e.seven_comment_4=seven_comment_4
        e.eight_comment_4=eight_comment_4
        e.nine_comment_4=nine_comment_4
        e.ten_comment_4=ten_comment_4
        e.eleven_comment_4=eleven_comment_4
        e.twelve_comment_4=twelve_comment_4
        e.thirteen_comment_4=thirteen_comment_4
        e.fourteen_comment_4=fourteen_comment_4
        e.fifteen_comment_4=fifteen_comment_4
        e.sixteen_comment_4=sixteen_comment_4
        e.seventeen_comment_4=seventeen_comment_4
        e.eighteen_comment_4=eighteen_comment_4
        e.nineteen_comment_4=nineteen_comment_4
        e.twenty_comment_4=twenty_comment_4
        e.twentyone_comment_4=twentyone_comment_4
        e.twentytwo_comment_4=twentytwo_comment_4
        e.twentythree_comment_4=twentythree_comment_4


        e.one_rating=one_rating
        e.two_rating=two_rating
        e.three_rating=three_rating
        e.four_rating=four_rating
        e.five_rating=five_rating
        e.six_rating=six_rating
        e.seven_rating=seven_rating
        e.eight_rating=eight_rating
        e.nine_rating=nine_rating
        e.ten_rating=ten_rating
        e.eleven_rating=eleven_rating
        e.twelve_rating=twelve_rating
        e.thirteen_rating=thirteen_rating
        e.fourteen_rating=fourteen_rating
        e.fifteen_rating=fifteen_rating
        e.sixteen_rating=sixteen_rating
        e.seventeen_rating=seventeen_rating
        e.eighteen_rating=eighteen_rating
        e.one_rating_2=one_rating_2
        e.two_rating_2=two_rating_2
        e.three_rating_2=three_rating_2
        e.four_rating_2=four_rating_2
        e.five_rating_2=five_rating_2
        e.six_rating_2=six_rating_2
        e.seven_rating_2=seven_rating_2
        e.eight_rating_2=eight_rating_2
        e.nine_rating_2=nine_rating_2
        e.ten_rating_2=ten_rating_2
        e.eleven_rating_2=eleven_rating_2
        e.one_rating_3=one_rating_3
        e.two_rating_3=two_rating_3
        e.three_rating_3=three_rating_3
        e.four_rating_3=four_rating_3
        e.five_rating_3=five_rating_3
        e.six_rating_3=six_rating_3
        e.seven_rating_3=seven_rating_3
        e.eight_rating_3=eight_rating_3
        e.one_rating_4=one_rating_4
        e.two_rating_4=two_rating_4
        e.three_rating_4=three_rating_4
        e.four_rating_4=four_rating_4
        e.five_rating_4=five_rating_4
        e.six_rating_4=six_rating_4
        e.seven_rating_4=seven_rating_4
        e.eight_rating_4=eight_rating_4
        e.nine_rating_4=nine_rating_4
        e.ten_rating_4=ten_rating_4
        e.eleven_rating_4=eleven_rating_4
        e.twelve_rating_4=twelve_rating_4
        e.thirteen_rating_4=thirteen_rating_4
        e.fourteen_rating_4=fourteen_rating_4
        e.fifteen_rating_4=fifteen_rating_4
        e.sixteen_rating_4=sixteen_rating_4
        e.seventeen_rating_4=seventeen_rating_4
        e.eighteen_rating_4=eighteen_rating_4
        e.nineteen_rating_4=nineteen_rating_4
        e.twenty_rating_4=twenty_rating_4
        e.twentyone_rating_4=twentyone_rating_4
        e.twentytwo_rating_4=twentytwo_rating_4
        e.twentythree_rating_4=twentythree_rating_4

        e.save()
        return redirect("/appraisal/partc")

    else:
        profile = Profile.objects.get(user=user)
        data = {"profile": profile}
        return render(request,'agent/partb.html', data)



def manager_part_b_save(request,id):
    user = request.user
    if request.method=="POST":
        agent = Profile.objects.get(emp_id=id)
        emp_id = agent.emp_id
        emp_name = agent.emp_name
        emp_rm1 = agent.emp_rm1
        emp_rm2 = agent.emp_rm2
        emp_rm3 = agent.emp_rm3
        emp_rm1_id = agent.emp_rm1_id
        emp_rm2_id = agent.emp_rm2_id
        emp_rm3_id = agent.emp_rm3_id
        # user = request.user
        mangr_one_comment = request.POST.get("one_com")
        mangr_two_comment = request.POST.get("two_com")
        mangr_three_comment = request.POST.get("three_com")
        mangr_four_comment = request.POST.get("four_com")
        mangr_five_comment = request.POST.get("five_com")
        mangr_six_comment = request.POST.get("six_com")
        mangr_seven_comment = request.POST.get("seven_com")
        mangr_eight_comment = request.POST.get("eight_com")
        mangr_nine_comment = request.POST.get("nine_com")
        mangr_ten_comment = request.POST.get("ten_com")
        mangr_eleven_comment = request.POST.get("eleven_com")
        mangr_twelve_comment = request.POST.get("twelve_com")
        mangr_thirteen_comment = request.POST.get("thirteen_com")
        mangr_fourteen_comment = request.POST.get("fourteen_com")
        mangr_fifteen_comment = request.POST.get("fifteen_com")
        mangr_sixteen_comment = request.POST.get("sixteen_com")
        mangr_seventeen_comment = request.POST.get("seventeen_com")
        mangr_eighteen_comment = request.POST.get("seventeen_com")
        mangr_one_comment_2 = request.POST.get("one_com2")
        mangr_two_comment_2 = request.POST.get("two_com2")
        mangr_three_comment_2 = request.POST.get("three_com2")
        mangr_four_comment_2 = request.POST.get("four_com2")
        mangr_five_comment_2 = request.POST.get("five_com2")
        mangr_six_comment_2 = request.POST.get("six_com2")
        mangr_seven_comment_2 = request.POST.get("seven_com2")
        mangr_eight_comment_2 = request.POST.get("eight_com2")
        mangr_nine_comment_2 = request.POST.get("nine_com2")
        mangr_ten_comment_2 = request.POST.get("ten_com2")
        mangr_eleven_comment_2 = request.POST.get("eleven_com2")
        mangr_one_comment_3 = request.POST.get("one_com3")
        mangr_two_comment_3 = request.POST.get("two_com3")
        mangr_three_comment_3 = request.POST.get("three_com3")
        mangr_four_comment_3 = request.POST.get("four_com3")
        mangr_five_comment_3 = request.POST.get("five_com3")
        mangr_six_comment_3 = request.POST.get("six_com3")
        mangr_seven_comment_3 = request.POST.get("seven_com3")
        mangr_eight_comment_3 = request.POST.get("eight_com3")
        mangr_one_comment_4 = request.POST.get("one_com4")
        mangr_two_comment_4 = request.POST.get("two_com4")
        mangr_three_comment_4 = request.POST.get("three_com4")
        mangr_four_comment_4 = request.POST.get("four_com4")
        mangr_five_comment_4 = request.POST.get("five_com4")
        mangr_six_comment_4 = request.POST.get("six_com4")
        mangr_seven_comment_4 = request.POST.get("seven_com4")
        mangr_eight_comment_4 = request.POST.get("eight_com4")
        mangr_nine_comment_4 = request.POST.get("nine_com4")
        mangr_ten_comment_4 = request.POST.get("ten_com4")
        mangr_eleven_comment_4 = request.POST.get("eleven_com4")
        mangr_twelve_comment_4 = request.POST.get("twelve_com4")
        mangr_thirteen_comment_4 = request.POST.get("thirteen_com4")
        mangr_fourteen_comment_4 = request.POST.get("fourteen_com4")
        mangr_fifteen_comment_4 = request.POST.get("fifteen_com4")
        mangr_sixteen_comment_4 = request.POST.get("sixteen_com4")
        mangr_seventeen_comment_4 = request.POST.get("seventeen_com4")
        mangr_eighteen_comment_4 = request.POST.get("eighteen_com4")
        mangr_nineteen_comment_4 = request.POST.get("nineteen_com4")
        mangr_twenty_comment_4 = request.POST.get("twenty_com4")
        mangr_twentyone_comment_4 = request.POST.get("twentyone_com4")
        mangr_twentytwo_comment_4 = request.POST.get("twentytwo_com4")
        mangr_twentythree_comment_4 = request.POST.get("twentythree_com4")

        mangr_one_rating = request.POST["one_rat"]
        mangr_two_rating = request.POST["two_rat"]
        mangr_three_rating = request.POST["three_rat"]
        mangr_four_rating = request.POST["four_rat"]
        mangr_five_rating = request.POST["five_rat"]
        mangr_six_rating = request.POST["six_rat"]
        mangr_seven_rating = request.POST["seven_rat"]
        mangr_eight_rating = request.POST["eight_rat"]
        mangr_nine_rating = request.POST["nine_rat"]
        mangr_ten_rating = request.POST["ten_rat"]
        mangr_eleven_rating = request.POST["eleven_rat"]
        mangr_twelve_rating = request.POST["twelve_rat"]
        mangr_thirteen_rating = request.POST["thirteen_rat"]
        mangr_fourteen_rating = request.POST["fourteen_rat"]
        mangr_fifteen_rating = request.POST["fifteen_rat"]
        mangr_sixteen_rating = request.POST["sixteen_rat"]
        mangr_seventeen_rating = request.POST["seventeen_rat"]
        mangr_eighteen_rating = request.POST["eighteen_rat"]
        mgr_table_1_total = [int(mangr_one_rating),int(mangr_two_rating),int(mangr_three_rating),
                                int(mangr_four_rating),int(mangr_five_rating),int(mangr_six_rating),
                                int(mangr_seven_rating),int(mangr_eight_rating),int(mangr_nine_rating),
                                int(mangr_ten_rating),int(mangr_eleven_rating),int(mangr_twelve_rating),
                                int(mangr_thirteen_rating),int(mangr_fourteen_rating),int(mangr_fifteen_rating),
                                int(mangr_sixteen_rating),int(mangr_seventeen_rating),int(mangr_eighteen_rating)]
        mgr_table_1_total = round(sum(mgr_table_1_total)/18,2)
        mangr_one_rating_2 = request.POST["one_rat2"]
        mangr_two_rating_2 = request.POST["two_rat2"]
        mangr_three_rating_2 = request.POST["three_rat2"]
        mangr_four_rating_2 = request.POST["four_rat2"]
        mangr_five_rating_2 = request.POST["five_rat2"]
        mangr_six_rating_2 = request.POST["six_rat2"]
        mangr_seven_rating_2 = request.POST["seven_rat2"]
        mangr_eight_rating_2 = request.POST["eight_rat2"]
        mangr_nine_rating_2 = request.POST["nine_rat2"]
        mangr_ten_rating_2 = request.POST["ten_rat2"]
        mangr_eleven_rating_2 = request.POST["eleven_rat2"]
        mgr_table_2_total = [int(mangr_one_rating_2),int(mangr_two_rating_2),int(mangr_three_rating_2),
                                int(mangr_four_rating_2),int(mangr_five_rating_2),int(mangr_six_rating_2),
                                int(mangr_seven_rating_2),int(mangr_eight_rating_2),int(mangr_nine_rating_2),
                                int(mangr_ten_rating),int(mangr_eleven_rating)]
        mgr_table_2_total = round(sum(mgr_table_2_total)/11,2)
        mangr_one_rating_3 = request.POST["one_rat3"]
        mangr_two_rating_3 = request.POST["two_rat3"]
        mangr_three_rating_3 = request.POST["three_rat3"]
        mangr_four_rating_3 = request.POST["four_rat3"]
        mangr_five_rating_3 = request.POST["five_rat3"]
        mangr_six_rating_3 = request.POST["six_rat3"]
        mangr_seven_rating_3 = request.POST["seven_rat3"]
        mangr_eight_rating_3 = request.POST["eight_rat3"]
        mgr_table_3_total = [int(mangr_one_rating_3),int(mangr_two_rating_3),int(mangr_three_rating_3),
                                int(mangr_four_rating_3),int(mangr_five_rating_3),int(mangr_six_rating),
                                int(mangr_seven_rating_3),int(mangr_eight_rating_3)]
        mgr_table_3_total = round(sum(mgr_table_3_total)/8,2)
        mangr_one_rating_4 = request.POST["one_rat4"]
        mangr_two_rating_4 = request.POST["two_rat4"]
        mangr_three_rating_4 = request.POST["three_rat4"]
        mangr_four_rating_4 = request.POST["four_rat4"]
        mangr_five_rating_4 = request.POST["five_rat4"]
        mangr_six_rating_4 = request.POST["six_rat4"]
        mangr_seven_rating_4 = request.POST["seven_rat4"]
        mangr_eight_rating_4 = request.POST["eight_rat4"]
        mangr_nine_rating_4 = request.POST["nine_rat4"]
        mangr_ten_rating_4 = request.POST["ten_rat4"]
        mangr_eleven_rating_4 = request.POST["eleven_rat4"]
        mangr_twelve_rating_4 = request.POST["twelve_rat4"]
        mangr_thirteen_rating_4 = request.POST["thirteen_rat4"]
        mangr_fourteen_rating_4 = request.POST["fourteen_rat4"]
        mangr_fifteen_rating_4 = request.POST["fifteen_rat4"]
        mangr_sixteen_rating_4 = request.POST["sixteen_rat4"]
        mangr_seventeen_rating_4 = request.POST["seventeen_rat4"]
        mangr_eighteen_rating_4 = request.POST["eighteen_rat4"]
        mangr_nineteen_rating_4 = request.POST["nineteen_rat4"]
        mangr_twenty_rating_4 = request.POST["twenty_rat4"]
        mangr_twentyone_rating_4 = request.POST["twentyone_rat4"]
        mangr_twentytwo_rating_4 = request.POST["twentytwo_rat4"]
        mangr_twentythree_rating_4 = request.POST["twentythree_rat4"]
        mgr_table_4_total = [int(mangr_one_rating_4),int(mangr_two_rating_4),int(mangr_three_rating_4),
                                int(mangr_four_rating_4),int(mangr_five_rating_4),int(mangr_six_rating_4),
                                int(mangr_seven_rating_4),int(mangr_eight_rating_4),int(mangr_nine_rating_4),
                                int(mangr_ten_rating_4),int(mangr_eleven_rating_4),int(mangr_twelve_rating_4),
                                int(mangr_thirteen_rating_4),int(mangr_fourteen_rating_4),int(mangr_fifteen_rating_4),
                                int(mangr_sixteen_rating_4),int(mangr_seventeen_rating_4),int(mangr_eighteen_rating_4),
                                int(mangr_nineteen_rating_4), int(mangr_twenty_rating_4), int(mangr_twentyone_rating_4),
                                int(mangr_twentytwo_rating_4), int(mangr_twentythree_rating_4)]
        mgr_table_4_total = round(sum(mgr_table_4_total)/23,2)

        e = PartB_Appraisee()
        e.mgr_table_1_total = mgr_table_1_total
        e.mgr_table_2_total = mgr_table_2_total
        e.mgr_table_3_total = mgr_table_3_total
        e.mgr_table_4_total = mgr_table_4_total
        e.agent = Profile.objects.get(emp_id=emp_id)
        e.emp_id = emp_id
        e.emp_name = emp_name
        e.emp_rm1 = emp_rm1
        e.emp_rm2 = emp_rm2
        e.emp_rm3 = emp_rm3
        e.emp_rm1_id = emp_rm1_id
        e.emp_rm2_id = emp_rm2_id
        e.emp_rm3_id = emp_rm3_id
        e.mangr_one_comment=mangr_one_comment
        e.mangr_two_comment=mangr_two_comment
        e.mangr_three_comment=mangr_three_comment
        e.mangr_four_comment=mangr_four_comment
        e.mangr_five_comment=mangr_five_comment
        e.mangr_six_comment=mangr_six_comment
        e.mangr_seven_comment=mangr_seven_comment
        e.mangr_eight_comment=mangr_eight_comment
        e.mangr_nine_comment=mangr_nine_comment
        e.mangr_ten_comment=mangr_ten_comment
        e.mangr_eleven_comment=mangr_eleven_comment
        e.mangr_twelve_comment=mangr_twelve_comment
        e.mangr_thirteen_comment=mangr_thirteen_comment
        e.mangr_fourteen_comment=mangr_fourteen_comment
        e.mangr_fifteen_comment=mangr_fifteen_comment
        e.mangr_sixteen_comment=mangr_sixteen_comment
        e.mangr_seventeen_comment=mangr_seventeen_comment
        e.mangr_eighteen_comment=mangr_eighteen_comment
        e.mangr_one_comment_2=mangr_one_comment_2
        e.mangr_two_comment_2=mangr_two_comment_2
        e.mangr_three_comment_2=mangr_three_comment_2
        e.mangr_four_comment_2=mangr_four_comment_2
        e.mangr_five_comment_2=mangr_five_comment_2
        e.mangr_six_comment_2=mangr_six_comment_2
        e.mangr_seven_comment_2=mangr_seven_comment_2
        e.mangr_eight_comment_2=mangr_eight_comment_2
        e.mangr_nine_comment_2=mangr_nine_comment_2
        e.mangr_ten_comment_2=mangr_ten_comment_2
        e.mangr_eleven_comment_2=mangr_eleven_comment_2
        e.mangr_one_comment_3=mangr_one_comment_3
        e.mangr_two_comment_3=mangr_two_comment_3
        e.mangr_three_comment_3=mangr_three_comment_3
        e.mangr_four_comment_3=mangr_four_comment_3
        e.mangr_five_comment_3=mangr_five_comment_3
        e.mangr_six_comment_3=mangr_six_comment_3
        e.mangr_seven_comment_3=mangr_seven_comment_3
        e.mangr_eight_comment_3=mangr_eight_comment_3
        e.mangr_one_comment_4=mangr_one_comment_4
        e.mangr_two_comment_4=mangr_two_comment_4
        e.mangr_three_comment_4=mangr_three_comment_4
        e.mangr_four_comment_4=mangr_four_comment_4
        e.mangr_five_comment_4=mangr_five_comment_4
        e.mangr_six_comment_4=mangr_six_comment_4
        e.mangr_seven_comment_4=mangr_seven_comment_4
        e.mangr_eight_comment_4=mangr_eight_comment_4
        e.mangr_nine_comment_4=mangr_nine_comment_4
        e.mangr_ten_comment_4=mangr_ten_comment_4
        e.mangr_eleven_comment_4=mangr_eleven_comment_4
        e.mangr_twelve_comment_4=mangr_twelve_comment_4
        e.mangr_thirteen_comment_4=mangr_thirteen_comment_4
        e.mangr_fourteen_comment_4=mangr_fourteen_comment_4
        e.mangr_fifteen_comment_4=mangr_fifteen_comment_4
        e.mangr_sixteen_comment_4=mangr_sixteen_comment_4
        e.mangr_seventeen_comment_4=mangr_seventeen_comment_4
        e.mangr_eighteen_comment_4=mangr_eighteen_comment_4
        e.mangr_nineteen_comment_4=mangr_nineteen_comment_4
        e.mangr_twenty_comment_4=mangr_twenty_comment_4
        e.mangr_twentyone_comment_4=mangr_twentyone_comment_4
        e.mangr_twentytwo_comment_4=mangr_twentytwo_comment_4
        e.mangr_twentythree_comment_4=mangr_twentythree_comment_4


        e.mangr_one_rating=mangr_one_rating
        e.mangr_two_rating=mangr_two_rating
        e.mangr_three_rating=mangr_three_rating
        e.mangr_four_rating=mangr_four_rating
        e.mangr_five_rating=mangr_five_rating
        e.mangr_six_rating=mangr_six_rating
        e.mangr_seven_rating=mangr_seven_rating
        e.mangr_eight_rating=mangr_eight_rating
        e.mangr_nine_rating=mangr_nine_rating
        e.mangr_ten_rating=mangr_ten_rating
        e.mangr_eleven_rating=mangr_eleven_rating
        e.mangr_twelve_rating=mangr_twelve_rating
        e.mangr_thirteen_rating=mangr_thirteen_rating
        e.mangr_fourteen_rating=mangr_fourteen_rating
        e.mangr_fifteen_rating=mangr_fifteen_rating
        e.mangr_sixteen_rating=mangr_sixteen_rating
        e.mangr_seventeen_rating=mangr_seventeen_rating
        e.mangr_eighteen_rating=mangr_eighteen_rating
        e.mangr_one_rating_2=mangr_one_rating_2
        e.mangr_two_rating_2=mangr_two_rating_2
        e.mangr_three_rating_2=mangr_three_rating_2
        e.mangr_four_rating_2=mangr_four_rating_2
        e.mangr_five_rating_2=mangr_five_rating_2
        e.mangr_six_rating_2=mangr_six_rating_2
        e.mangr_seven_rating_2=mangr_seven_rating_2
        e.mangr_eight_rating_2=mangr_eight_rating_2
        e.mangr_nine_rating_2=mangr_nine_rating_2
        e.mangr_ten_rating_2=mangr_ten_rating_2
        e.mangr_eleven_rating_2=mangr_eleven_rating_2
        e.mangr_one_rating_3=mangr_one_rating_3
        e.mangr_two_rating_3=mangr_two_rating_3
        e.mangr_three_rating_3=mangr_three_rating_3
        e.mangr_four_rating_3=mangr_four_rating_3
        e.mangr_five_rating_3=mangr_five_rating_3
        e.mangr_six_rating_3=mangr_six_rating_3
        e.mangr_seven_rating_3=mangr_seven_rating_3
        e.mangr_eight_rating_3=mangr_eight_rating_3
        e.mangr_one_rating_4=mangr_one_rating_4
        e.mangr_two_rating_4=mangr_two_rating_4
        e.mangr_three_rating_4=mangr_three_rating_4
        e.mangr_four_rating_4=mangr_four_rating_4
        e.mangr_five_rating_4=mangr_five_rating_4
        e.mangr_six_rating_4=mangr_six_rating_4
        e.mangr_seven_rating_4=mangr_seven_rating_4
        e.mangr_eight_rating_4=mangr_eight_rating_4
        e.mangr_nine_rating_4=mangr_nine_rating_4
        e.mangr_ten_rating_4=mangr_ten_rating_4
        e.mangr_eleven_rating_4=mangr_eleven_rating_4
        e.mangr_twelve_rating_4=mangr_twelve_rating_4
        e.mangr_thirteen_rating_4=mangr_thirteen_rating_4
        e.mangr_fourteen_rating_4=mangr_fourteen_rating_4
        e.mangr_fifteen_rating_4=mangr_fifteen_rating_4
        e.mangr_sixteen_rating_4=mangr_sixteen_rating_4
        e.mangr_seventeen_rating_4=mangr_seventeen_rating_4
        e.mangr_eighteen_rating_4=mangr_eighteen_rating_4
        e.mangr_nineteen_rating_4=mangr_nineteen_rating_4
        e.mangr_twenty_rating_4=mangr_twenty_rating_4
        e.mangr_twentyone_rating_4=mangr_twentyone_rating_4
        e.mangr_twentytwo_rating_4=mangr_twentytwo_rating_4
        e.mangr_twentythree_rating_4=mangr_twentythree_rating_4
        # e.appraise = user

        e.save()
        return redirect("manpartc",id=id)

    else:
        try:
            PartB_Appraisee.objects.get(emp_id=id)
            messages.info(request,"Part B for this Agent is Already done! Redirecting you to Part C.")
            return redirect("manpartc", id=id)
        except PartB_Appraisee.DoesNotExist:
            profile = Profile.objects.get(emp_id=id)
            rm3_desi = Profile.objects.get(emp_id=id).emp_rm3_id
            rm3_desi = Profile.objects.get(emp_id=rm3_desi).emp_desi
            data = {"profile": profile,"rm3_desi":rm3_desi}
            return render(request,'manager/manager_partb.html', data)



def part_c_save(request):
    user = request.user
    if request.method == "POST":
        respect_rating = request.POST["res_rat"]
        integrity_rating = request.POST["int_rat"]
        diversity_rating = request.POST["div_rat"]
        excellence_rating = request.POST["exc_rat"]
        teamwork_rating = request.POST["tea_rat"]
        agent_score = [int(respect_rating),int(integrity_rating),int(diversity_rating),int(excellence_rating),int(teamwork_rating)]
        agent_score = round(sum(agent_score)/5,2)
        respect_comment = request.POST.get("res_com")
        integrity_comment = request.POST.get("int_com")
        diversity_comment = request.POST.get("div_com")
        excellence_comment = request.POST.get("exc_com")
        teamwork_comment = request.POST.get("tea_com")

        e = PartC_Appraisee.objects.get(emp_id=user.profile.emp_id)
        e.agent_score = agent_score
        e.respect_rating = respect_rating
        e.integrity_rating = integrity_rating
        e.diversity_rating = diversity_rating
        e.excellence_rating = excellence_rating
        e.teamwork_rating = teamwork_rating
        e.respect_comment = respect_comment
        e.integrity_comment = integrity_comment
        e.diversity_comment = diversity_comment
        e.excellence_comment = excellence_comment
        e.teamwork_comment = teamwork_comment

        e.save()
        return redirect("/appraisal/partd")

    else:
        profile = Profile.objects.get(user=user)
        data = {"profile": profile}
        return render(request, "agent/part_c.html",data)

def manager_part_c_save(request,id):
    profile = Profile.objects.get(emp_id=id)
    if request.method == "POST":
        # us = request.user
        respect_rating = request.POST["res_rat"]
        integrity_rating = request.POST["int_rat"]
        diversity_rating = request.POST["div_rat"]
        excellence_rating = request.POST["exc_rat"]
        teamwork_rating = request.POST["tea_rat"]
        mgr_score = [int(respect_rating),int(integrity_rating),int(diversity_rating),int(excellence_rating),int(teamwork_rating)]
        mgr_score = round(sum(mgr_score)/5,2)
        respect_comment = request.POST.get("res_com")
        integrity_comment = request.POST.get("int_com")
        diversity_comment = request.POST.get("div_com")
        excellence_comment = request.POST.get("exc_com")
        teamwork_comment = request.POST.get("tea_com")

        e = PartC_Appraisee()
        e.mgr_score = mgr_score
        e.agent = profile
        e.emp_id = id
        e.emp_name = profile.emp_name
        e.emp_rm1 = profile.emp_rm1
        e.emp_rm2 = profile.emp_rm2
        e.emp_rm3 = profile.emp_rm3
        e.emp_rm1_id = profile.emp_rm1_id
        e.emp_rm2_id = profile.emp_rm2_id
        e.emp_rm3_id = profile.emp_rm3_id
        e.mangr_respect_rating = respect_rating
        e.mangr_integrity_rating = integrity_rating
        e.mangr_diversity_rating = diversity_rating
        e.mangr_excellence_rating = excellence_rating
        e.mangr_teamwork_rating = teamwork_rating
        e.mangr_respect_comment = respect_comment
        e.mangr_integrity_comment = integrity_comment
        e.mangr_diversity_comment = diversity_comment
        e.mangr_excellence_comment = excellence_comment
        e.mangr_teamwork_comment = teamwork_comment

        e.save()
        return redirect("manpartd",id=id)
    else:
        data = {"profile":profile}
        return render(request, "manager/manager_part_c.html", data)



def part_d_save(request):
    if request.method=="POST":
        userr = request.user
        strengths = request.POST["strengths"]
        improvement_areas = request.POST["improvement"]
        development_need_1 = request.POST["development1"]
        development_need_2 = request.POST["development2"]
        development_need_3 = request.POST["development3"]
        development_need_4 = request.POST["development4"]
        action_plan_1 = request.POST["action1"]
        action_plan_2 = request.POST["action2"]
        action_plan_3 = request.POST["action3"]
        action_plan_4 = request.POST["action4"]
        responsibility_time_1 = request.POST["responsibility1"]
        responsibility_time_2 = request.POST["responsibility2"]
        responsibility_time_3 = request.POST["responsibility3"]
        responsibility_time_4 = request.POST["responsibility4"]
        desired_level_1 = request.POST["desired1"]
        desired_level_2 = request.POST["desired2"]
        desired_level_3 = request.POST["desired3"]
        desired_level_4 = request.POST["desired4"]
        train_identify_refitment = request.POST.get("train_identify_refitment")
        coach_train_redeploy = request.POST.get("coach_train_redeploy")
        future_leaders = request.POST.get("future_leaders")
        need_development = request.POST.get("need_development")
        # solid_citizens_1 = request.POST.get("solid_citizens_1")
        # solid_citizens_2 = request.POST.get("solid_citizens_2")
        no_scope_improvement = request.POST.get("no_scope_improvement")
        need_development_coach = request.POST.get("need_development_coach")
        coach_on_value = request.POST.get("coach_on_value")
        traing_type_1 = request.POST.get("traing_type_1")
        traing_type_2 = request.POST.get("traing_type_2")
        traing_type_3 = request.POST.get("traing_type_3")
        traing_type_4 = request.POST.get("traing_type_4")
        traing_type_5 = request.POST.get("traing_type_5")
        traing_time_1 = request.POST.get("traing_time_1")
        traing_time_2 = request.POST.get("traing_time_2")
        traing_time_3 = request.POST.get("traing_time_3")
        traing_time_4 = request.POST.get("traing_time_4")
        traing_time_5 = request.POST.get("traing_time_5")
        appraisee_roles = request.POST.get("appraisee_roles")
        appraisee_skills_required = request.POST.get("appraisee_skills_required")
        appraisee_time_frame = request.POST.get("appraisee_time_frame")
        agree = request.POST.get("rating")
        if_disagree = request.POST.get("dis_com")
        comments_feedback = request.POST.get("feedback")


        e = PartD_Appraisee()
        e.strengths = strengths
        e.improvement_areas = improvement_areas
        e.development_need_1 = development_need_1
        e.development_need_2 =development_need_2
        e.development_need_3 =development_need_3
        e.development_need_4 =development_need_4
        e.action_plan_1 =action_plan_1
        e.action_plan_2 =action_plan_2
        e.action_plan_3 =action_plan_3
        e.action_plan_4 =action_plan_4
        e.responsibility_time_1 =responsibility_time_1
        e.responsibility_time_2 =responsibility_time_2
        e.responsibility_time_3 =responsibility_time_3
        e.responsibility_time_4 =responsibility_time_4
        e.desired_level_1 =desired_level_1
        e.desired_level_2 =desired_level_2
        e.desired_level_3 =desired_level_3
        e.desired_level_4 =desired_level_4
        e.train_identify_refitment =train_identify_refitment
        e.coach_train_redeploy =coach_train_redeploy
        e.future_leaders =future_leaders
        e.need_development =need_development
        # e.solid_citizens_1 =
        # e.solid_citizens_2 =
        e.no_scope_improvement =no_scope_improvement
        e.need_development_coach =need_development_coach
        e.coach_on_value =coach_on_value
        e.traing_type_1 =traing_type_1
        e.traing_type_2 =traing_type_2
        e.traing_type_3 =traing_type_3
        e.traing_type_4 =traing_type_4
        e.traing_type_5 =traing_type_5
        e.traing_time_1 =traing_time_1
        e.traing_time_2 =traing_time_2
        e.traing_time_3 =traing_time_3
        e.traing_time_4 =traing_time_4
        e.traing_time_5 =traing_time_5
        e.appraisee_roles =appraisee_roles
        e.appraisee_skills_required =appraisee_skills_required
        e.appraisee_time_frame =appraisee_time_frame
        e.agree =agree
        e.if_disagree =if_disagree
        e.comments_feedback =comments_feedback
        e.appraisee = userr

        e.save()

        return render(request, "common/part_d.html")

    else:
        profile = Profile.objects.get(emp_id=request.user.profile.emp_id)
        data = {"profile":profile}
        return render(request, "agent/part_d.html",data)


def manager_part_d_save(request,id):
    if request.method=="POST":
        pass
        return redirect("/appraisal/login")
    else:
        part_d = PartC_Appraisee.objects.get(emp_id=id)
        profile = Profile.objects.get(emp_id=id)
        data = {"part_d": part_d, "profile": profile}
        return render(request, "manager/manager_part_d.html", data)


def viewAppraisal(request,id):
    part_a = PartA_Appraisee.objects.get(emp_id=id)
    part_b = PartB_Appraisee.objects.get(emp_id=id)
    part_c = PartC_Appraisee.objects.get(emp_id=id)
    profile = Profile.objects.get(emp_id=id)
    data = {"part_a": part_a,"part_b": part_b,"part_c": part_c, "profile": profile}
    return render(request, "common/viewall.html", data)
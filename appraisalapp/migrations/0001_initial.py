# Generated by Django 4.0.3 on 2022-04-21 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=12)),
                ('emp_name', models.CharField(max_length=200)),
                ('emp_desi', models.CharField(max_length=200)),
                ('emp_rm1', models.CharField(max_length=200)),
                ('emp_rm1_id', models.CharField(max_length=30)),
                ('emp_rm2', models.CharField(max_length=200)),
                ('emp_rm2_id', models.CharField(max_length=30)),
                ('emp_rm3', models.CharField(max_length=200)),
                ('emp_rm3_id', models.CharField(max_length=30)),
                ('emp_process', models.CharField(max_length=200)),
                ('process_id', models.IntegerField(blank=True, null=True)),
                ('emp_doj', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=12)),
                ('emp_name', models.CharField(max_length=200)),
                ('emp_desi', models.CharField(max_length=200)),
                ('emp_rm1', models.CharField(max_length=200)),
                ('emp_rm1_id', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_rm2', models.CharField(max_length=200)),
                ('emp_rm2_id', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_rm3', models.CharField(max_length=200)),
                ('emp_rm3_id', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_process', models.CharField(max_length=200)),
                ('process_id', models.IntegerField(blank=True, null=True)),
                ('emp_doj', models.DateField(blank=True, null=True)),
                ('pc', models.BooleanField(default=False)),
                ('agent_score', models.FloatField(blank=True, null=True)),
                ('final_score', models.FloatField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PartD_Appraisee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=12)),
                ('emp_name', models.CharField(blank=True, max_length=200, null=True)),
                ('emp_rm1_id', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_rm2_id', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_rm3_id', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_rm1', models.CharField(max_length=200)),
                ('emp_rm2', models.CharField(max_length=200)),
                ('emp_rm3', models.CharField(max_length=200)),
                ('strengths', models.TextField(blank=True, null=True)),
                ('improvement_areas', models.TextField(blank=True, null=True)),
                ('development_need_1', models.TextField(blank=True, null=True)),
                ('development_need_2', models.TextField(blank=True, null=True)),
                ('development_need_3', models.TextField(blank=True, null=True)),
                ('development_need_4', models.TextField(blank=True, null=True)),
                ('action_plan_1', models.TextField(blank=True, null=True)),
                ('action_plan_2', models.TextField(blank=True, null=True)),
                ('action_plan_3', models.TextField(blank=True, null=True)),
                ('action_plan_4', models.TextField(blank=True, null=True)),
                ('responsibility_time_1', models.TextField(blank=True, null=True)),
                ('responsibility_time_2', models.TextField(blank=True, null=True)),
                ('responsibility_time_3', models.TextField(blank=True, null=True)),
                ('responsibility_time_4', models.TextField(blank=True, null=True)),
                ('desired_level_1', models.TextField(blank=True, null=True)),
                ('desired_level_2', models.TextField(blank=True, null=True)),
                ('desired_level_3', models.TextField(blank=True, null=True)),
                ('desired_level_4', models.TextField(blank=True, null=True)),
                ('checkbox', models.CharField(blank=True, max_length=250, null=True)),
                ('traing_type_1', models.TextField(blank=True, null=True)),
                ('traing_type_2', models.TextField(blank=True, null=True)),
                ('traing_type_3', models.TextField(blank=True, null=True)),
                ('traing_type_4', models.TextField(blank=True, null=True)),
                ('traing_type_5', models.TextField(blank=True, null=True)),
                ('traing_time_1', models.TextField(blank=True, null=True)),
                ('traing_time_2', models.TextField(blank=True, null=True)),
                ('traing_time_3', models.TextField(blank=True, null=True)),
                ('traing_time_4', models.TextField(blank=True, null=True)),
                ('traing_time_5', models.TextField(blank=True, null=True)),
                ('mgr_appraisee_roles', models.TextField(blank=True, null=True)),
                ('mgr_appraisee_skills_required', models.TextField(blank=True, null=True)),
                ('mgr_appraisee_time_frame', models.TextField(blank=True, null=True)),
                ('appraisee_roles', models.TextField(blank=True, null=True)),
                ('appraisee_skills_required', models.TextField(blank=True, null=True)),
                ('appraisee_time_frame', models.TextField(blank=True, null=True)),
                ('agree', models.TextField(blank=True, null=True)),
                ('if_disagree', models.TextField(blank=True, null=True)),
                ('comments_feedback', models.TextField(blank=True, null=True)),
                ('mgr_comments_feedback', models.TextField(blank=True, null=True)),
                ('agent_complete_status', models.BooleanField(default=False)),
                ('agent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appraisalapp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='PartC_Appraisee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=12)),
                ('emp_name', models.CharField(blank=True, max_length=200, null=True)),
                ('emp_rm1', models.CharField(max_length=200)),
                ('emp_rm2', models.CharField(max_length=200)),
                ('emp_rm3', models.CharField(max_length=200)),
                ('emp_rm1_id', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_rm2_id', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_rm3_id', models.CharField(blank=True, max_length=30, null=True)),
                ('respect_rating', models.IntegerField(blank=True, null=True)),
                ('integrity_rating', models.IntegerField(blank=True, null=True)),
                ('diversity_rating', models.IntegerField(blank=True, null=True)),
                ('excellence_rating', models.IntegerField(blank=True, null=True)),
                ('teamwork_rating', models.IntegerField(blank=True, null=True)),
                ('respect_comment', models.TextField(blank=True, null=True)),
                ('integrity_comment', models.TextField(blank=True, null=True)),
                ('diversity_comment', models.TextField(blank=True, null=True)),
                ('excellence_comment', models.TextField(blank=True, null=True)),
                ('teamwork_comment', models.TextField(blank=True, null=True)),
                ('mangr_respect_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_integrity_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_diversity_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_excellence_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_teamwork_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_respect_comment', models.TextField(blank=True, null=True)),
                ('mangr_integrity_comment', models.TextField(blank=True, null=True)),
                ('mangr_diversity_comment', models.TextField(blank=True, null=True)),
                ('mangr_excellence_comment', models.TextField(blank=True, null=True)),
                ('mangr_teamwork_comment', models.TextField(blank=True, null=True)),
                ('mgr_score', models.FloatField(blank=True, null=True)),
                ('agent_score', models.FloatField(blank=True, null=True)),
                ('agent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appraisalapp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='PartB_Appraisee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=12)),
                ('emp_name', models.CharField(blank=True, max_length=200, null=True)),
                ('emp_rm1', models.CharField(max_length=200)),
                ('emp_rm2', models.CharField(max_length=200)),
                ('emp_rm3', models.CharField(max_length=200)),
                ('emp_rm1_id', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_rm2_id', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_rm3_id', models.CharField(blank=True, max_length=30, null=True)),
                ('one_rating', models.IntegerField(blank=True, null=True)),
                ('two_rating', models.IntegerField(blank=True, null=True)),
                ('three_rating', models.IntegerField(blank=True, null=True)),
                ('four_rating', models.IntegerField(blank=True, null=True)),
                ('five_rating', models.IntegerField(blank=True, null=True)),
                ('six_rating', models.IntegerField(blank=True, null=True)),
                ('seven_rating', models.IntegerField(blank=True, null=True)),
                ('eight_rating', models.IntegerField(blank=True, null=True)),
                ('nine_rating', models.IntegerField(blank=True, null=True)),
                ('ten_rating', models.IntegerField(blank=True, null=True)),
                ('eleven_rating', models.IntegerField(blank=True, null=True)),
                ('twelve_rating', models.IntegerField(blank=True, null=True)),
                ('thirteen_rating', models.IntegerField(blank=True, null=True)),
                ('fourteen_rating', models.IntegerField(blank=True, null=True)),
                ('fifteen_rating', models.IntegerField(blank=True, null=True)),
                ('sixteen_rating', models.IntegerField(blank=True, null=True)),
                ('seventeen_rating', models.IntegerField(blank=True, null=True)),
                ('eighteen_rating', models.IntegerField(blank=True, null=True)),
                ('one_rating_2', models.IntegerField(blank=True, null=True)),
                ('two_rating_2', models.IntegerField(blank=True, null=True)),
                ('three_rating_2', models.IntegerField(blank=True, null=True)),
                ('four_rating_2', models.IntegerField(blank=True, null=True)),
                ('five_rating_2', models.IntegerField(blank=True, null=True)),
                ('six_rating_2', models.IntegerField(blank=True, null=True)),
                ('seven_rating_2', models.IntegerField(blank=True, null=True)),
                ('eight_rating_2', models.IntegerField(blank=True, null=True)),
                ('nine_rating_2', models.IntegerField(blank=True, null=True)),
                ('ten_rating_2', models.IntegerField(blank=True, null=True)),
                ('eleven_rating_2', models.IntegerField(blank=True, null=True)),
                ('one_rating_3', models.IntegerField(blank=True, null=True)),
                ('two_rating_3', models.IntegerField(blank=True, null=True)),
                ('three_rating_3', models.IntegerField(blank=True, null=True)),
                ('four_rating_3', models.IntegerField(blank=True, null=True)),
                ('five_rating_3', models.IntegerField(blank=True, null=True)),
                ('six_rating_3', models.IntegerField(blank=True, null=True)),
                ('seven_rating_3', models.IntegerField(blank=True, null=True)),
                ('eight_rating_3', models.IntegerField(blank=True, null=True)),
                ('one_rating_4', models.IntegerField(blank=True, null=True)),
                ('two_rating_4', models.IntegerField(blank=True, null=True)),
                ('three_rating_4', models.IntegerField(blank=True, null=True)),
                ('four_rating_4', models.IntegerField(blank=True, null=True)),
                ('five_rating_4', models.IntegerField(blank=True, null=True)),
                ('six_rating_4', models.IntegerField(blank=True, null=True)),
                ('seven_rating_4', models.IntegerField(blank=True, null=True)),
                ('eight_rating_4', models.IntegerField(blank=True, null=True)),
                ('nine_rating_4', models.IntegerField(blank=True, null=True)),
                ('ten_rating_4', models.IntegerField(blank=True, null=True)),
                ('eleven_rating_4', models.IntegerField(blank=True, null=True)),
                ('twelve_rating_4', models.IntegerField(blank=True, null=True)),
                ('thirteen_rating_4', models.IntegerField(blank=True, null=True)),
                ('fourteen_rating_4', models.IntegerField(blank=True, null=True)),
                ('fifteen_rating_4', models.IntegerField(blank=True, null=True)),
                ('sixteen_rating_4', models.IntegerField(blank=True, null=True)),
                ('seventeen_rating_4', models.IntegerField(blank=True, null=True)),
                ('eighteen_rating_4', models.IntegerField(blank=True, null=True)),
                ('nineteen_rating_4', models.IntegerField(blank=True, null=True)),
                ('twenty_rating_4', models.IntegerField(blank=True, null=True)),
                ('twentyone_rating_4', models.IntegerField(blank=True, null=True)),
                ('twentytwo_rating_4', models.IntegerField(blank=True, null=True)),
                ('twentythree_rating_4', models.IntegerField(blank=True, null=True)),
                ('one_comment', models.TextField(blank=True, null=True)),
                ('two_comment', models.TextField(blank=True, null=True)),
                ('three_comment', models.TextField(blank=True, null=True)),
                ('four_comment', models.TextField(blank=True, null=True)),
                ('five_comment', models.TextField(blank=True, null=True)),
                ('six_comment', models.TextField(blank=True, null=True)),
                ('seven_comment', models.TextField(blank=True, null=True)),
                ('eight_comment', models.TextField(blank=True, null=True)),
                ('nine_comment', models.TextField(blank=True, null=True)),
                ('ten_comment', models.TextField(blank=True, null=True)),
                ('eleven_comment', models.TextField(blank=True, null=True)),
                ('twelve_comment', models.TextField(blank=True, null=True)),
                ('thirteen_comment', models.TextField(blank=True, null=True)),
                ('fourteen_comment', models.TextField(blank=True, null=True)),
                ('fifteen_comment', models.TextField(blank=True, null=True)),
                ('sixteen_comment', models.TextField(blank=True, null=True)),
                ('seventeen_comment', models.TextField(blank=True, null=True)),
                ('eighteen_comment', models.TextField(blank=True, null=True)),
                ('one_comment_2', models.TextField(blank=True, null=True)),
                ('two_comment_2', models.TextField(blank=True, null=True)),
                ('three_comment_2', models.TextField(blank=True, null=True)),
                ('four_comment_2', models.TextField(blank=True, null=True)),
                ('five_comment_2', models.TextField(blank=True, null=True)),
                ('six_comment_2', models.TextField(blank=True, null=True)),
                ('seven_comment_2', models.TextField(blank=True, null=True)),
                ('eight_comment_2', models.TextField(blank=True, null=True)),
                ('nine_comment_2', models.TextField(blank=True, null=True)),
                ('ten_comment_2', models.TextField(blank=True, null=True)),
                ('eleven_comment_2', models.TextField(blank=True, null=True)),
                ('one_comment_3', models.TextField(blank=True, null=True)),
                ('two_comment_3', models.TextField(blank=True, null=True)),
                ('three_comment_3', models.TextField(blank=True, null=True)),
                ('four_comment_3', models.TextField(blank=True, null=True)),
                ('five_comment_3', models.TextField(blank=True, null=True)),
                ('six_comment_3', models.TextField(blank=True, null=True)),
                ('seven_comment_3', models.TextField(blank=True, null=True)),
                ('eight_comment_3', models.TextField(blank=True, null=True)),
                ('one_comment_4', models.TextField(blank=True, null=True)),
                ('two_comment_4', models.TextField(blank=True, null=True)),
                ('three_comment_4', models.TextField(blank=True, null=True)),
                ('four_comment_4', models.TextField(blank=True, null=True)),
                ('five_comment_4', models.TextField(blank=True, null=True)),
                ('six_comment_4', models.TextField(blank=True, null=True)),
                ('seven_comment_4', models.TextField(blank=True, null=True)),
                ('eight_comment_4', models.TextField(blank=True, null=True)),
                ('nine_comment_4', models.TextField(blank=True, null=True)),
                ('ten_comment_4', models.TextField(blank=True, null=True)),
                ('eleven_comment_4', models.TextField(blank=True, null=True)),
                ('twelve_comment_4', models.TextField(blank=True, null=True)),
                ('thirteen_comment_4', models.TextField(blank=True, null=True)),
                ('fourteen_comment_4', models.TextField(blank=True, null=True)),
                ('fifteen_comment_4', models.TextField(blank=True, null=True)),
                ('sixteen_comment_4', models.TextField(blank=True, null=True)),
                ('seventeen_comment_4', models.TextField(blank=True, null=True)),
                ('eighteen_comment_4', models.TextField(blank=True, null=True)),
                ('nineteen_comment_4', models.TextField(blank=True, null=True)),
                ('twenty_comment_4', models.TextField(blank=True, null=True)),
                ('twentyone_comment_4', models.TextField(blank=True, null=True)),
                ('twentytwo_comment_4', models.TextField(blank=True, null=True)),
                ('twentythree_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_one_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_two_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_three_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_four_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_five_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_six_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_seven_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_eight_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_nine_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_ten_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_eleven_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_twelve_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_thirteen_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_fourteen_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_fifteen_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_sixteen_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_seventeen_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_eighteen_rating', models.IntegerField(blank=True, null=True)),
                ('mangr_one_rating_2', models.IntegerField(blank=True, null=True)),
                ('mangr_two_rating_2', models.IntegerField(blank=True, null=True)),
                ('mangr_three_rating_2', models.IntegerField(blank=True, null=True)),
                ('mangr_four_rating_2', models.IntegerField(blank=True, null=True)),
                ('mangr_five_rating_2', models.IntegerField(blank=True, null=True)),
                ('mangr_six_rating_2', models.IntegerField(blank=True, null=True)),
                ('mangr_seven_rating_2', models.IntegerField(blank=True, null=True)),
                ('mangr_eight_rating_2', models.IntegerField(blank=True, null=True)),
                ('mangr_nine_rating_2', models.IntegerField(blank=True, null=True)),
                ('mangr_ten_rating_2', models.IntegerField(blank=True, null=True)),
                ('mangr_eleven_rating_2', models.IntegerField(blank=True, null=True)),
                ('mangr_one_rating_3', models.IntegerField(blank=True, null=True)),
                ('mangr_two_rating_3', models.IntegerField(blank=True, null=True)),
                ('mangr_three_rating_3', models.IntegerField(blank=True, null=True)),
                ('mangr_four_rating_3', models.IntegerField(blank=True, null=True)),
                ('mangr_five_rating_3', models.IntegerField(blank=True, null=True)),
                ('mangr_six_rating_3', models.IntegerField(blank=True, null=True)),
                ('mangr_seven_rating_3', models.IntegerField(blank=True, null=True)),
                ('mangr_eight_rating_3', models.IntegerField(blank=True, null=True)),
                ('mangr_one_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_two_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_three_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_four_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_five_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_six_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_seven_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_eight_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_nine_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_ten_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_eleven_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_twelve_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_thirteen_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_fourteen_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_fifteen_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_sixteen_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_seventeen_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_eighteen_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_nineteen_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_twenty_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_twentyone_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_twentytwo_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_twentythree_rating_4', models.IntegerField(blank=True, null=True)),
                ('mangr_one_comment', models.TextField(blank=True, null=True)),
                ('mangr_two_comment', models.TextField(blank=True, null=True)),
                ('mangr_three_comment', models.TextField(blank=True, null=True)),
                ('mangr_four_comment', models.TextField(blank=True, null=True)),
                ('mangr_five_comment', models.TextField(blank=True, null=True)),
                ('mangr_six_comment', models.TextField(blank=True, null=True)),
                ('mangr_seven_comment', models.TextField(blank=True, null=True)),
                ('mangr_eight_comment', models.TextField(blank=True, null=True)),
                ('mangr_nine_comment', models.TextField(blank=True, null=True)),
                ('mangr_ten_comment', models.TextField(blank=True, null=True)),
                ('mangr_eleven_comment', models.TextField(blank=True, null=True)),
                ('mangr_twelve_comment', models.TextField(blank=True, null=True)),
                ('mangr_thirteen_comment', models.TextField(blank=True, null=True)),
                ('mangr_fourteen_comment', models.TextField(blank=True, null=True)),
                ('mangr_fifteen_comment', models.TextField(blank=True, null=True)),
                ('mangr_sixteen_comment', models.TextField(blank=True, null=True)),
                ('mangr_seventeen_comment', models.TextField(blank=True, null=True)),
                ('mangr_eighteen_comment', models.TextField(blank=True, null=True)),
                ('mangr_one_comment_2', models.TextField(blank=True, null=True)),
                ('mangr_two_comment_2', models.TextField(blank=True, null=True)),
                ('mangr_three_comment_2', models.TextField(blank=True, null=True)),
                ('mangr_four_comment_2', models.TextField(blank=True, null=True)),
                ('mangr_five_comment_2', models.TextField(blank=True, null=True)),
                ('mangr_six_comment_2', models.TextField(blank=True, null=True)),
                ('mangr_seven_comment_2', models.TextField(blank=True, null=True)),
                ('mangr_eight_comment_2', models.TextField(blank=True, null=True)),
                ('mangr_nine_comment_2', models.TextField(blank=True, null=True)),
                ('mangr_ten_comment_2', models.TextField(blank=True, null=True)),
                ('mangr_eleven_comment_2', models.TextField(blank=True, null=True)),
                ('mangr_one_comment_3', models.TextField(blank=True, null=True)),
                ('mangr_two_comment_3', models.TextField(blank=True, null=True)),
                ('mangr_three_comment_3', models.TextField(blank=True, null=True)),
                ('mangr_four_comment_3', models.TextField(blank=True, null=True)),
                ('mangr_five_comment_3', models.TextField(blank=True, null=True)),
                ('mangr_six_comment_3', models.TextField(blank=True, null=True)),
                ('mangr_seven_comment_3', models.TextField(blank=True, null=True)),
                ('mangr_eight_comment_3', models.TextField(blank=True, null=True)),
                ('mangr_one_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_two_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_three_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_four_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_five_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_six_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_seven_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_eight_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_nine_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_ten_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_eleven_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_twelve_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_thirteen_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_fourteen_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_fifteen_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_sixteen_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_seventeen_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_eighteen_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_nineteen_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_twenty_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_twentyone_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_twentytwo_comment_4', models.TextField(blank=True, null=True)),
                ('mangr_twentythree_comment_4', models.TextField(blank=True, null=True)),
                ('mgr_score', models.FloatField(blank=True, null=True)),
                ('agent_score', models.FloatField(blank=True, null=True)),
                ('agent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appraisalapp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='PartA_Appraisee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=12)),
                ('emp_name', models.CharField(max_length=200)),
                ('emp_desi', models.CharField(max_length=200)),
                ('emp_rm1_id', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_rm2_id', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_rm3_id', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_process', models.CharField(max_length=200)),
                ('supervisor_name', models.CharField(blank=True, max_length=150, null=True)),
                ('supervisor_desig', models.CharField(blank=True, max_length=150, null=True)),
                ('reviewers_name', models.CharField(blank=True, max_length=150, null=True)),
                ('reviewers_desig', models.CharField(blank=True, max_length=150, null=True)),
                ('parameter_1', models.CharField(blank=True, max_length=150, null=True)),
                ('parameter_1_score', models.IntegerField(blank=True, null=True)),
                ('parameter_1_rating', models.FloatField(blank=True, null=True)),
                ('parameter_1_comment', models.TextField(blank=True, null=True)),
                ('parameter_1_rating_agent', models.FloatField(blank=True, null=True)),
                ('parameter_1_comment_agent', models.TextField(blank=True, null=True)),
                ('parameter_2', models.CharField(blank=True, max_length=150, null=True)),
                ('parameter_2_score', models.IntegerField(blank=True, null=True)),
                ('parameter_2_rating', models.FloatField(blank=True, null=True)),
                ('parameter_2_comment', models.TextField(blank=True, null=True)),
                ('parameter_2_rating_agent', models.FloatField(blank=True, null=True)),
                ('parameter_2_comment_agent', models.TextField(blank=True, null=True)),
                ('parameter_3', models.CharField(blank=True, max_length=150, null=True)),
                ('parameter_3_score', models.IntegerField(blank=True, null=True)),
                ('parameter_3_rating', models.FloatField(blank=True, null=True)),
                ('parameter_3_comment', models.TextField(blank=True, null=True)),
                ('parameter_3_rating_agent', models.FloatField(blank=True, null=True)),
                ('parameter_3_comment_agent', models.TextField(blank=True, null=True)),
                ('parameter_4', models.CharField(blank=True, max_length=150, null=True)),
                ('parameter_4_score', models.IntegerField(blank=True, null=True)),
                ('parameter_4_rating', models.FloatField(blank=True, null=True)),
                ('parameter_4_comment', models.TextField(blank=True, null=True)),
                ('parameter_4_rating_agent', models.FloatField(blank=True, null=True)),
                ('parameter_4_comment_agent', models.TextField(blank=True, null=True)),
                ('parameter_5', models.CharField(blank=True, max_length=150, null=True)),
                ('parameter_5_score', models.IntegerField(blank=True, null=True)),
                ('parameter_5_rating', models.FloatField(blank=True, null=True)),
                ('parameter_5_comment', models.TextField(blank=True, null=True)),
                ('parameter_5_rating_agent', models.FloatField(blank=True, null=True)),
                ('parameter_5_comment_agent', models.TextField(blank=True, null=True)),
                ('parameter_6', models.CharField(blank=True, max_length=150, null=True)),
                ('parameter_6_score', models.IntegerField(blank=True, null=True)),
                ('parameter_6_rating', models.FloatField(blank=True, null=True)),
                ('parameter_6_comment', models.TextField(blank=True, null=True)),
                ('parameter_6_rating_agent', models.FloatField(blank=True, null=True)),
                ('parameter_6_comment_agent', models.TextField(blank=True, null=True)),
                ('mangr_special_comment', models.TextField(null=True)),
                ('mgr_score', models.FloatField(blank=True, null=True)),
                ('agent_score', models.FloatField(blank=True, null=True)),
                ('agent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appraisalapp.profile')),
            ],
        ),
    ]

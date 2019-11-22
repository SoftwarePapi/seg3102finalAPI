from rest_framework import serializers
from v1.models import Comments, Courses, Section_students, Sections, Team_Members, Teams, Threads, Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.account_type = validated_data.get('account_type', instance.account_type)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.indentification_number = validated_data.get('indentification_number', instance.indentification_number)
        instance.program = validated_data.get('program', instance.program)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = "__all__"
    def create(self, validated_data):
        return Teams.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.team_id = validated_data.get('team_id', instance.team_id)
        instance.team_name = validated_data.get('team_name', instance.team_name)
        instance.creation_date = validated_data.get('creation_date', instance.creation_date)
        instance.captain = validated_data.get('captain', instance.captain)
        instance.status = validated_data.get('status', instance.status)
        instance.min_capacity = validated_data.get('min_capacity', instance.min_capacity)
        instance.max_capacity = validated_data.get('max_capacity', instance.max_capacity)
        instance.save()
        return instance


class Team_MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team_Members
        fields = "__all__"
    def create(self, validated_data):
        return Team_Members.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.team_id = validated_data.get('team_id', instance.team_id)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.save()
        return instance

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"
    def create(self, validated_data):
        return Courses.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.course_id = validated_data.get('course_id', instance.course_id)
        instance.course_code = validated_data.get('course_code', instance.course_code)
        instance.save()
        return instance

class SectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = "__all__"
    def create(self, validated_data):
        return Sections.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.section_id = validated_data.get('section_id', instance.section_id)
        instance.section_name = validated_data.get('section_name', instance.section_name)
        instance.course_id = validated_data.get('course_id', instance.course_id)
        instance.professor = validated_data.get('professor', instance.professor)
        instance.save()
        return instance

class Section_studentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section_students
        fields = "__all__"
    def create(self, validated_data):
        return Section_students.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.section_id = validated_data.get('section_id', instance.section_id)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.save()
        return instance

class ThreadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threads
        fields = "__all__"
    def create(self, validated_data):
        return Threads.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.thread_id = validated_data.get('thread_id', instance.thread_id)
        instance.title = validated_data.get('title', instance.title)
        instance.body_text = validated_data.get('body_text', instance.body_text)
        instance.author = validated_data.get('author', instance.author)
        instance.team_id = validated_data.get('team_id', instance.team_id)
        instance.save()
        return instance

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
    def create(self, validated_data):
        return Comments.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.comment_id = validated_data.get('thread_id', instance.thread_id)
        instance.body_text = validated_data.get('body_text', instance.body_text)
        instance.author = validated_data.get('author', instance.author)
        instance.thread_id = validated_data.get('thread_id', instance.thread_id)
        instance.save()
        return instance

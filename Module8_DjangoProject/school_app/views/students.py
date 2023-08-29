from school_app.models.students import Students
import json
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from school_app.utilities.validations import validate_name,validate_username,validate_password
from school_project.middleware import *
from datetime import datetime
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect


@csrf_exempt
def student_registration_data(request):

    if request.method == "POST":
        data = json.loads(request.body)
        username_valid = validate_username(data['username'])
        name_valid =validate_name(data['name'])
        password_valid = validate_password(data['password'])
        
        if name_valid is True and username_valid is True and password_valid is True:

            print('start')
            if User.objects.filter(username=data['username']).exists():
                print('start 1')
                return JsonResponse({'message':'user already exists'})
            else:
                print("Entered")
                user1 =User.objects.create(
                        username = data['username'],
                        email = data['email'],
                        password = make_password(data['password']),)
                Students.objects.create(
                        user =user1,           
                        name =data['name'],
                        age =data['age'],
                        guardian = data['guardian'],
                        relation = data['relation'],
                        phone = data['phone'],
                        created_by=user1)
                print("end")
                return JsonResponse({'message': 'Data created successfully'})

        else:
            errors =[]
            if name_valid != True :
                errors.extend(name_valid)
            if username_valid != True:
                errors.extend(username_valid)
            if password_valid != True:
                errors.extend(password_valid)
            return JsonResponse({'message': errors},status=400)
    return HttpResponse(status=405)
        
def get_all_student_data(request):

    print(request.path)
    print(request.user.is_authenticated)
    if request.method == "GET":
        data =Students.objects.filter(is_deleted=False).values()
        return JsonResponse({'data':list(data)})
    else:
        return HttpResponse(status=405)
    
def get_student_data(request,id):

    if request.method == "GET":
        data =Students.objects.filter(user_id=id,is_deleted=False).values()
        if data:
            return JsonResponse({'data':list(data)})
        else:
            return JsonResponse({"message":"Student not found"})

    else:
        return JsonResponse({"message":"Details not found"},status=405)

@csrf_exempt
def update_student_data(request,id):
    if request.method == 'PUT':
        try:
            user=User.objects.get(id=id)
            data = json.loads(request.body)
            user.username = data['username']
            user.email = data['email']
            user.password = make_password(data['password'])
            student=Students.objects.get(user_id=id)
            student.name =data['name']
            student.age =data['age']
            student.guardian = data['guardian']
            student.relation = data['relation']
            student.phone = data['phone']
            student.updated_by = request.user
            student.updated_on = datetime.now()

            user.save()
            student.save()
            return JsonResponse({'message': 'Student data updated successfully'})
        
        except User.DoesNotExist:
            return JsonResponse({'message': 'Student not found'}, status=404)
        
        except:
            return JsonResponse({'message': 'Invalid Data'},status=400)

    elif request.method == 'PATCH':
        try:
            user=User.objects.get(id=id)
            student=Students.objects.get(user_id=id)

            data = json.loads(request.body)

            if 'username' in data :
                user.username = data['username']
            if 'email' in data :
                user.email = data['email']
            if 'password' in data:
                user.password = make_password(data['password'])
            if 'name' in data :
                student.name =data['name']
            if 'age' in data :
                student.age =data['age']
            if 'guardian' in data :
                student.guardian = data['guardian']
            if 'relation' in data :
                student.relation = data['relation']
            if 'phone' in data:
                student.phone = data['phone']
            student.updated_by = request.user
            student.updated_on = datetime.now

            user.save()
            student.save()
            return JsonResponse({'message': 'Student Data updated successfully'})
        
        except User.DoesNotExist:
            return JsonResponse({'message': 'Student not found'}, status=404)
        
        except:
            return JsonResponse({'message': 'Invalid Data'},status=400)
        
    return HttpResponse(status=405)

#@decorator_from_middleware(CustomAuthorizationMiddleware)        
#@login_required
@csrf_exempt
def delete_student_data(request,id):

    if request.method == "DELETE":
        try :
            user= User.objects.get(id=id)
            student = Students.objects.get(user__id=id)
            student.is_deleted = True
            student.deleted_by=request.user
            student.deleted_on = datetime.now()
            student.save()
            #student.delete()

            return JsonResponse({'data':'Student deleted successfully'})
        
        except User.DoesNotExist:
            return JsonResponse({'message': 'Student not found'}, status=404)
        
        except:
            return JsonResponse({'message': 'Error deleting user'}, status=500)
    
    return HttpResponse(status=400)


User = get_user_model()

def activate(request, token):
    try:
        user = User.objects.get(is_active=False)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse('Account successfully activated')
    except User.DoesNotExist:
        pass

    return HttpResponse('Account successfully activated')
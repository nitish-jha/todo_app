from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from todo.models import Note, User, Document
from todo.forms import DocumentForm
from django.core.urlresolvers import reverse
from django.template import RequestContext
import datetime

# Create your views here.

def login(request):
	return render(request, 'todo/login.html')

def home(request):
	u, p, flag = [], [], 0
	try:
		user = request.session['user']
		obj = User.objects.raw('select id from todo_user where username= %s', user)
		for i in obj:
			uid = i.id
		notes = Note.objects.filter(username_id = uid)
		context = {'notes' : notes, 'user' : user}
		return render(request, 'todo/home.html', context)
	except:
		user = request.POST['username']
		password = request.POST['password']
		obj = User.objects.raw('select id from todo_user where username= %s', user)
		for i in obj:
			uid = i.id
		notes = Note.objects.filter(username_id = uid)
		x = User.objects.all();
		for i in x.values():
			for j, k in i.iteritems():
				if j == 'username':
					u.append(k)
				elif j == 'password':
					p.append(k)
		for i in range(len(u)):
			if user == u[i] and password == p[i]:
				request.session['user'] = user;
				context = {'notes': notes, 'user' : user}
				flag = 1
				return render(request, 'todo/home.html', context)		
	if flag == 0:
		return HttpResponse('Invalid Username or Password')

def home1(request):
	#p = get_object_or_404(Note, pk=note_id)
	#comment = p.choice_set.get(pk=request.POST['comment'])
	comment = request.POST['comment']
	category = request.POST['category']
	user = request.session['user']
	date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S");
	obj = User.objects.raw('select id from todo_user where username= %s', user)
	for i in obj:
		uid = i.id
	p1 = Note(note=comment, username_id=uid, category=category, timestamp=date)
	p1.save()
	return HttpResponseRedirect(reverse('home'))

def notes(request):
	if request.method == 'POST':
		user = request.session['user']
		category = request.POST['category'];
		if category == 'all':
			category_list = Note.objects.all();
		else:
			category_list = Note.objects.filter(category=category)
		context = {'user' : user, 'list' : category_list}
		return render(request, 'todo/notes.html', context)

def list(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(docfile = request.FILES['docfile'])
			newdoc.save()

			return HttpResponseRedirect(reverse('list'))
	else:
		form = DocumentForm()

	documents = Document.objects.all()

	return render_to_response('todo/list.html', {'documents' : documents,
		'form' : form}, context_instance=RequestContext(request))

def logout(request):
	try:
		del request.session['user']
	except KeyError:
		pass
	return HttpResponseRedirect(reverse('login'));
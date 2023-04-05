from django.shortcuts import render

def home(request):
	return render(request, 'home.html')


def reverse(request):
	user_text = request.GET['usertext']
	reverse_text = user_text[::-1]
	count_the_number_of_words = len(user_text.split())
	return render(request, 'reverse.html', {'usertext':user_text,
		'reversetext':reverse_text,
		'numberwords':count_the_number_of_words
		})
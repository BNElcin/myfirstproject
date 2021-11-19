from django.shortcuts import render
def page(request):
	return render(request,'page.html')
def reverse(request):
        user_input_text=request.GET["userinputtext"]
        reversed_text=user_input_text[::-1]
        return render(request,'reverse.html',{"UIT":user_input_text,"RT":reversed_text})

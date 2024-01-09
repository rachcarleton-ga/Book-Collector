from django.shortcuts import render
books = [
    {'title': 'Atomic Habits', 'author': 'James Clear', 'description': 'An Easy & Proven Way to Build Good Habits & Break Bad Ones', 'publishedyear': 2018 },
    {'title': 'The Dead Romantics', 'author': 'Ashley Poston', 'description': 'Romance is dead, but this is not what she had in mind. Florence Day is the ghostwriter for one of the most prolific romance authors in the industry, and she has a problem: After a terrible breakup, she no longer believes in love. It is as good as dead. When her new editor, a too-handsome mountain of a man, refuses to give her an extension on her book deadline, Florence prepares to kiss her career goodbye. But then she gets a phone call she never wanted to receive, and she must return home for the first time in a decade to help her family bury her beloved father. For ten years, she has run from the town that never understood her, and even though she misses the the sounds of the warm Southern night and her eccentric, loving family and their funeral parlor, she cannot bring herself to stay. Her father is gone, yet everything else feels the same. And she hates it. Until she finds a ghost standing at the front door of the funeral parlor, just as broad and infuriatingly handsome as ever, and he is just as confused about why he is there as she is. Romance is most certainly dead... but so is her new editor, and his unfinished business will have her second-guesing everything she has ever known about love stories.', 'publishedyear': 2022 },
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):
      return render(request, 'books/index.html', {
    'books': books
  })
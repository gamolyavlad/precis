import os

path = lambda root,*a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

settings = {
    'static_path': path(ROOT, 'static'),
    'template_path':path(ROOT, 'templates')
}

print settings['static_path']
def save_in_viewed(url):
    print(url)


viewed_list = []

#read file
viewed_list = list(map(str.rstrip, open('viewed.txt').readlines()))

print(viewed_list)
open('viewed.txt', 'w').write('rrr')
open('viewed.txt', 'w').write('rrr')
open('viewed.txt', 'w').write('rrr')
open('viewed.txt', 'w').write('www')
        
        
def already_saved(url):
    print(url)
    
    
    
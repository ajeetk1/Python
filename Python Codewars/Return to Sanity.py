# This function should return an object, but it's not doing what's intended. What's wrong?
    #def mystery():
    #results = {
    #'sanity': 'Hello'}
    #return
    #results

# Solution 

def mystery():
    return {
    'sanity': 'Hello'}
  
def build_string(*args):
    return "I like {}!".format(",".join(args))
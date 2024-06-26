
# xpath
#---------
# XPath is defined as XML path.
# It is a syntax or language for finding any element on the web page using XML path expression.
# XPath is used to find the location of any element on a webpage using HTML DOM structure.
# XPath can be used to navigate through elements and attributes in DOM.
# XPath is an address of the element.

# Types of xpath
# 1) Absolute/Full xpath
# Ex: /html/body/nav/div/div[2]/ul[3]/li[1]/a /html/body/div[1]/div/div[3]/div[1]/img

# 2) Relative/Partial xpath
# Ex: //*[@id="header-navbar"]/ul[3]/li[1]/a
# //*[@id="divLogo"]/img


# Diff between Absolute & Relative Xpaths
# 1) Absolute xpath starts from root html node
# Relative xpath directly jump to element on DOM.

# 2) Absolute xpath start with /
# Relative xpath start with //

# 3) in Absolute xpath we use only tags/nodes
# In Relative xpath we use attributes.

# How to write xpaths manually
# html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a

# syntax of writing relative xpath
# //tagname [@attribute='value']
# //input[@id=' small-searchterms']
# //*[@id=' small-searchterms']


# How to capture xpath automatically
# 1) Firebug, firepath --> firefox -->deprecated/ not available
# 2) Right click on element-->Inspect--> Highlight html code-->Right click-->Copy Xpath 3) SelectorsHub

# 2 reasons to prefer relative xpath
# 1) if developer introduced new element then absolute xpath will be broken.
# 2) if developer changed the location then absolute xpath will be broken.
# 3) relative xpath is more stable than absolute xpath

# absolute xpath is unstable....
# Which XPath is prefered? Why?
# Ans: Relative

# xpath options
#---------------
# and                "//tag_name[@attribute='value' and @attribute='value']"
# or                 "//tag_name[@attribute='value' or @attribute='value']"
# contains()         "//tag_name[contains(@id,st)]
# starts-with()      "//tag_name[starts-with(@id,st)]
# text()             "//tag_name[text()='women']"
 
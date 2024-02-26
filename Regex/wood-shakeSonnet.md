# Ex 2 Step File

Find: ```^\s\s```
Replace: ```Nothing```

Find: ```^.+$```
Replace: ```<line>\0</line>```

Find:```<line>\s([A-Z])+</line>```
Replace:```</sonnet><sonnet number="\1">```

Did some cleanup work at the end adding an ```<xml>``` root element.
Also got rid of the beginning ```</sonnet>``` and added
one at the bottom.

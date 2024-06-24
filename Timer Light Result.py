Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/dell/AppData/Local/Programs/Python/Python312/SkillShare/Timer Light.py
>>> timer=Timer()
>>> timer.set(6)
>>> timer.elapse(4)
>>> timer.elapse(3)
Timer is Up!!
>>> timer.left
0
>>> bulb=TimerLight()
>>> bulb.set(7)
>>> bulb.on
True
>>> bulb.elapse(4)
>>> bulb.on
True
>>> bulb.elapse(4)
Timer is Up!!
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    bulb.elapse(4)
  File "C:/Users/dell/AppData/Local/Programs/Python/Python312/SkillShare/Timer Light.py", line 33, in elapse
    self.ring()
  File "C:/Users/dell/AppData/Local/Programs/Python/Python312/SkillShare/Timer Light.py", line 42, in ring
    delf.on=False
NameError: name 'delf' is not defined. Did you mean: 'self'?

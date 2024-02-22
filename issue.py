# issue.py

class F:
	def __format__(self, format_spec):
		print("spec:", repr(format_spec))
		return format_spec.join(["a", "b", "c"])

print("out: ", repr((f"{F():\n}")))
print("out: ", repr((f"{F():\u2603}")))

print("out: ", repr((format(F(), "\n"))))
print("out: ", repr((format(F(), "\u2603"))))

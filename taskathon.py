import subprocess
import json

class Tasks:
	def __init__(self, logging=False):
		self.logging = logging
		
	def fprint(self, message):
		if self.logging:
			print(message)
			
	def _formatOutput(self, data):
		self.fprint(data)
		try:
			return json.loads(data)
		except:
			return str(data, 'latin-1')
		
	def cmd(self, command):
		self.fprint(f"Executing {command}")
		if not command.startswith("task "):
			command = f"task {command}"
			
		command = f"{command} rc.confirmation:0"
		self.fprint(f"Command finalized: {command}")
		
		f = subprocess.run(command.split(), stderr=subprocess.PIPE, stdout=subprocess.PIPE)
			
		if f.stdout:
			return self._formatOutput(f.stdout)
		else:
			return self._formatOutput(f.stderr)
		
	def add(self, description):
		return self.cmd(f'task add {description}')
	
	def done(self, _id):
		return self.cmd(f'task done {_id}')	
	
	def delete(self, _id):
		return self.cmd(f'task delete {_id}')		
	
	def export(self, _id = ""):
		if _id:
			f = f'task {str(_id)} export'
		else:
			f = 'task export'
			
		return self.cmd(f)
		
	def get(self, dom):
		return self.cmd(f'task _get {dom}')


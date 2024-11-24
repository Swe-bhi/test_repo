import requests

class AWS_EC2_Adapter:
    def create_vm(self, name):
        response = requests.post(
            'http://localhost:5001/create-vm',
            json={'name': name}
        )
        return response.json().get('vmID')

    def run_vm(self, vmID):
        response = requests.post(
            'http://localhost:5001/run-vm',
            json={'vmID': vmID}
        )
        return response.json().get('message')



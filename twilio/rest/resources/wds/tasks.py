from .. import InstanceResource, ListResource


class Task(InstanceResource):
    """
    A Task resource
    """

    def delete(self):
        """
        Delete a task.
        """
        return self.parent.delete_instance(self.name)

    def update(self, **kwargs):
        """
        Update a task.
        """
        return self.parent.update_instance(self.name, kwargs)


class Tasks(ListResource):
    """ A list of Task resources """

    name = "Tasks"
    instance = Task

    def create(self, attributes, workflow_sid):
        """
        Create a Task.

        :param attributes: Url-encoded JSON string describing the attributes of
            this task. This data will be passed back to the Workflow's
            AssignmentCallbackURL when the Task is assigned to a Worker. An
            example task: { 'task_type': 'call', 'twilio_call_sid': '...',
            'customer_ticket_number': '12345' }.
        :param workflow_sid: The workflow_sid for the Workflow that you would
            like to handle routing for this Task.
        """
        return self.create_instance({'attributes': attributes,
                                     'workflow_sid': workflow_sid})

    def delete(self, sid):
        """
        Delete the given task
        """
        return self.delete_instance(sid)

    def update(self, sid, **kwargs):
        """
        Update a :class:`Task` with the given parameters.

        All the parameters are describe above in :meth:`create`
        """
        return self.update_instance(sid, kwargs)

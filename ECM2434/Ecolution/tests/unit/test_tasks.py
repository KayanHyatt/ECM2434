from Ecolution.models import CustomUser, Pet
from Ecolution.models import UserTask
from Ecolution.models import Task
from Ecolution.tests.base_test import BaseTestCase

class TasksUnitTests(BaseTestCase):

    def setUp(self):
        # create a test user
        self.user1 = CustomUser.objects.create_user(username = 'testuser', password = 'password')
        self.client.login(username = 'testuser', password = 'password')
        # create a test task
        self.task1 = Task.objects.create(task_name = "Buy groceries", description = "Go to the store and buy food")
        self.task2 = Task.objects.create(task_name = "Task 2", description = "Task description here")
        # **Ensure points_given is set here:**
        self.task3 = Task.objects.create(task_name = "Task 3", description = "Task description here", xp_given = 100, points_given = 50)
        # create user's pet
        self.pet1 = Pet.objects.create(
            user = self.user1,
            pet_name = "TestPet",
            pet_level = 1,
            pet_exp = 0, # pet starts with 0 XP
            pet_type = "mushroom"
        )

    # As a user, I can add (pre-defined) tasks to my list
    def test_user_adds_tasks(self):
        # add task to user list
        user_tasks = UserTask.objects.create(user = self.user1, task = self.task1)
        # check task is now in user's list
        self.assertTrue(UserTask.objects.filter(user = self.user1).exists())

    # As a user, I can remove tasks from my list
    def test_user_removes_tasks(self):
        # add task to user list
        user_task = UserTask.objects.create(user = self.user1, task = self.task1)
        # check task is now in user's list
        self.assertTrue(UserTask.objects.filter(user = self.user1).exists())
        # remove task from list
        user_task.delete()
        # check task is no longer in user's list
        self.assertFalse(UserTask.objects.filter(user = self.user1, task = self.task1).exists())

    # As a user, I can complete tasks
    def test_user_completes_tasks(self):
        # add task to user list
        user_tasks = UserTask.objects.create(user = self.user1, task = self.task1)
        # check task is now in user's current tasks list
        self.assertTrue(UserTask.objects.filter(user = self.user1).exists())
        self.assertTrue(UserTask.objects.filter(task = self.task1, completed = False).exists())
        # user marks task as "complete"
        user_tasks.completed = True
        user_tasks.save()
        # task no longer appears in current tasks list
        self.assertFalse(UserTask.objects.filter(task = self.task1, completed = False).exists())
        # task now appears in completed tasks list
        self.assertTrue(UserTask.objects.filter(task = self.task1, completed = True).exists())
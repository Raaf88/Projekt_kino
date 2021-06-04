from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from django.urls import reverse

from . import forms
from .forms import CommentForm

def test_valid_data(self):
    form = CommentForm({
        'name': "Turanga Leela",
        'email': "leela@example.com",
        'body': "Hi there",
    }, entry=self.entry)
    self.assertTrue(form.is_valid())
    comment = form.save()
    self.assertEqual(comment.name, "Turanga Leela")
    self.assertEqual(comment.email, "leela@example.com")
    self.assertEqual(comment.body, "Hi there")
    self.assertEqual(comment.entry, self.entry)

def test_blank_data(self):
    form = CommentForm({}, entry=self.entry)
    self.assertFalse(form.is_valid())
    self.assertEqual(form.errors, {
        'name': ['required'],
        'email': ['required'],
        'body': ['required'],
    })


class HomePageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get('movie_detail')
        self.assertEquals(response.status_code, 404)

    def test_view_uses_correct_template(self):
        response = self.client.get('movie_detail')
        self.assertEquals(response.status_code, 404)


    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Movie Spot')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')


    def test_view_url_by_name(self):
        response = self.client.get('register')
        self.assertEquals(response.status_code, 404)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/register.html')

from .models import Movie, Category

class MovieModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name = 'Thriller')
        Movie.objects.create(category_id= 1, name='Big', rezyser='John Stamos', rok_produkcji=2010, movie_description = 'jdfnjdh', movie_recenzja='jhdbfdhb', price=9 )

    def test_name_label(self):
        name = Movie.objects.get(id=1)
        field_label = name._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_movie_name_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('name').max_length
        self.assertEqual(max_length, 180)

    def test_movie_name_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('rezyser').max_length
        self.assertEqual(max_length, 180) # błąd musi być 180 znaków

    def test_object_name_is_last_name_comma_first_name(self):
        movie = Movie.objects.get(id=1)
        expected_object_name = f'{movie.name}'
        self.assertEqual(str(movie), expected_object_name)


class SignUpPageTests(TestCase):
    def setUp(self) -> None:
        self.last_name = 'Kowalski'
        self.first_name = 'Jan'
        self.username = 'testuser'
        self.email = 'testuser@email.com'
        self.password = 'password'

    def test_signup_page_url(self):
        response = self.client.get("/users/register/")
        self.assertEqual(response.status_code, 404)


    def test_signup_page_view_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register/register.html')

    def test_signup_form(self):
        response = self.client.post(reverse('register'), data={
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,

            'password1': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 302)

        users = get_user_model().objects.all()



@override_settings(
    ACCOUNT_ACTIVATION_DAYS=7,
    REGISTRATION_OPEN=True,
    REGISTRATION_SUPPLEMENT_CLASS=None,
    REGISTRATION_BACKEND_CLASS=(
            'registration.backends.default.DefaultRegistrationBackend'),)
class RegistrationViewTestCase(TestCase):


    def test_registration_view_get(self):

        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'register/register.html')
        self.failUnless(isinstance(response.context['form'],
                                   forms.RegisterForm))


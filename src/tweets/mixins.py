from django.forms.utils import ErrorList
from django import forms


class FormUserNeedMixun(object):
    def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(FormUserNeedMixun, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged"])
        #    form.non_field_errors =  ErrorList(["User must be logged"])
            return self.form_invalid(form)

class UserOwnerMixin(object):
    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(UserOwnerMixin, self).form_valid(form)
        else:
            form.errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["The user is not allow to change this data"])
            return self.form_invalid(form)

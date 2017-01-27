#!/bin/bash
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Adapted from https://github.com/ansible/django-gulp-nginx
# https://github.com/ansible/django-gulp-nginx/blob/master/ansible/roles/django-gunicorn/files/entrypoint.sh
MANAGE=/srv/project/manage.py
BINDIR=/srv/bin

set -x

if [[ $@ == *"gunicorn"* || $@ == *"runserver"* ]]; then
	if [[ -f $MANAGE ]]; then
        $BINDIR/wait_on_postgres.py
        if [[ $? == 0 ]]; then
            $MANAGE migrate --noinput
            $MANAGE collectstatic --noinput
            $BINDIR/setsite.py
            $BINDIR/setadmin.py
        fi
	fi
fi

# Run the actual server
exec "$@"

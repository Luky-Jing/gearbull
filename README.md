GearBull:  ���ֹ�ţ

Featres:

1����������ṹ��ͨ��json��������֧�������֧���롢�򡢷ǹ�ϵ

2����ϸ��ִ�п��ƣ��������ơ�����ִ�С�����ִ�С���ͣ�㡢�ָ�ִ�С�ʧ�ܱ�����������

3��ֱ��֧�� python��shell��Ϊҵ���߼����ԣ������ڲ�����ά��������������������������ȳ�����ά����

4��ʧ������Failover����������롢ȫ���������

5��֧��Restful API



��ΰ�װ��

1����װ python36�� pip3

2����GearBull ��Ŀ clone ������, ����clone�� /home/work/gearbull

3����װ����,  cd /home/work/gearbull &&  pip3  install -r requirements.txt

4����ʼ�����ݿ� python3  manage.py migrate

5���޸� supervisor/supervisord.conf��  [program:scheduler]��[program:monitor]��[program:webserver] �� directory ������Ĭ��Ϊ /home/work/gearbull�� ����������

[program:scheduler]

command=python3  WorkFlow/scheduler.py 

directory=/home/work/gearbull              

...


[program:monitor]

command=python3  WorkFlow/monitor.py 

directory=/home/work/gearbull              

...


[program:webserver]

command=python3 manage.py runserver 127.0.0.1:8088 

directory=/home/work/gearbull  



6������ supervisord,   supervisord -c supervisor/supervisord.conf 

7��/usr/local/python36/bin/supervisorctl -c supervisor/supervisord.conf  status �鿴״̬

supervisorctl -c supervisor/supervisord.conf  status

monitor                          RUNNING   pid 4143, uptime 0:00:06

scheduler                        RUNNING   pid 4144, uptime 0:00:06

webserver                        RUNNING   pid 4145, uptime 0:00:06





���ʹ�ã�
0. �鿴��ǰ����Щ��������
curl 'http://127.0.0.1:8088/workflow/api/flows/' 

2. �鿴����������
curl 'http://127.0.0.1:8088/workflow/api/flow/?name=example_task'  

1. ����job , ���� targets��Ҫ�����Ķ���task_type��flow ����
curl -H 'Content-type: application/json' -X POST -d '{"targets":["h1", "h2"], "task_type": "test_clause"}' http://localhost:8088/workflow/api/create_job/

2. �鿴job�б�
curl 'http://127.0.0.1:8088/workflow/jobs/' 

3. �鿴ָ��job����
curl 'http://127.0.0.1:8088/workflow/jobs/1/' 

4. ͬ��, task, action
curl 'http://127.0.0.1:8088/workflow/tasks/'  
curl 'http://127.0.0.1:8088/workflow/tasks/16/'  
curl 'http://127.0.0.1:8088/workflow/actions/'  
curl 'http://127.0.0.1:8088/workflow/actions/89/'  

5. �鿴����������ϵ
curl 'http://127.0.0.1:8088/workflow/api/show_flow/?job_id=1'   

6.�����Լ��Ĺ�����
     a��cd /home/work/gearbull 
    b���� data/plugins �£�cp example_tasks.py  your_tasks.py 

    c���༭ conf/task_trees.py, ���� trees����:

example_task_trees = {

    "trees": {

        "tree1": {

            "nodes": ["action1", "action2", "action3"],

        },

    },

    "name": "example_tasks",

    "src_path": PLUGINS_DIR,

    "module": "example_tasks",

    "class": "ExampleTask",

}


    d����trees_dict �����µ�tree����: "example_task": example_task_trees,

   e������ server: supervisorctl -c supervisor/supervisord.conf  restart all

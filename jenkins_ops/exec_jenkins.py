import jenkins
from jenkins_ops import logger
import time
class Run_jenkins():
    def __init__(self,url,user,passwd,project):
        self.url=url
        self.user=user
        self.passwd=passwd
        self.project=project
    def __run_status(self,ret):
        build_run = ret.get_running_builds()
        run_job = []
        for item in build_run:
            run_job.append(item['name'])
        return run_job
    def __run_job(self,ret,next_build_number):
        flag = True
        while flag:
            run_job=self.__run_status(ret)
            if run_job==[]:
                logger.log.info("{project} #{number} is not running,keep waiting......".format(project=self.project,
                                                                                     number=next_build_number))
                time.sleep(2)
            else:
                logger.log.info("{project} #{number} is still building......".format(project=self.project,number=next_build_number))
                flag=False
        flag1 = True
        while flag1:
            run_job = self.__run_status(ret)
            if self.project not in run_job:
                # lastnum1 = ret.get_job_info(project)['lastCompletedBuild']['number']
                self.__run_result(ret, next_build_number)
                flag1 = False
            else:
                logger.log.info("{project} #{number} is still building......".format(project=self.project,number=next_build_number))
                time.sleep(2)
    def __run_result(self,req,next_build_number):
        build_info = req.get_build_info(self.project, next_build_number)
        build_result = build_info['result']
        build_ip=build_info['builtOn']
        logger.log.info("{project} #{number} FINISHED".format(project=self.project, number=next_build_number))
        logger.log.info("{project} #{number} build {status}".format(project=self.project, number=next_build_number,
                                                                    status=build_result))
        logger.log.info("{project} #{number} build on {build_ip}".format(project=self.project, number=next_build_number,
                                                                    build_ip=build_ip))
    def run_jenkins(self,build_target,version_type):
        ret = jenkins.Jenkins(self.url, self.user, self.passwd)
        if  not ret.job_exists(self.project):
            logger.log.error("the {job} not exist,please check".format(job=self.project))
            raise ValueError("the {job} not exist,please check".format(job=self.project))
        run_job = self.__run_status(ret)
        if self.project  not in run_job:
            next_build_number = ret.get_job_info(self.project)['nextBuildNumber']
            ret.build_job(self.project, {'build_target': build_target, 'version_type':version_type})
            logger.log.warning(
                "{project} #{number} will be build......".format(project=self.project, number=next_build_number))
            time.sleep(2)
            self.__run_job(ret, next_build_number)
        else:
            logger.log.warning("the job was started by others,please waiting!")
    def job_list(self):
        ret = jenkins.Jenkins(self.url, self.user, self.passwd)
        req=ret.get_all_jobs()
        jobs=[]
        for i in req:
            s={'value':i['name']}
            jobs.append(s)
        return (jobs)
    def get_build_info(self):
        ret=jenkins.Jenkins(self.url, self.user, self.passwd)
        last_num=ret.get_job_info(self.project)['lastCompletedBuild']['number']
        info=ret.get_build_console_output(self.project,last_num)
        return info
if __name__ == '__main__':
    s=Run_jenkins('http://10.203.105.90:8500','admin','admin','test_gateway')
    r=s.job_list()
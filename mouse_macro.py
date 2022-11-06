from	PIL				import Image
from	difflib			import SequenceMatcher
import	pytesseract
import	pyautogui
import 	time

# 문제 리스트
class Quest:
	_quest_list = [
		[
			"number",
			"1",
			"Question: \
which of the following statements is true regarding amazon ec2 pricing?",
			"2",
		],	[
			"number",
			"1",
			"Question: \
the prices that aws pricing calculator uses for the estimates come from the aws ___?",
			"1",
		],	[
			"string",
			"1",
			"Question: \
which amazon s3 feature automatically changes data storage tiers based on your specifications?",
			"lifecycle configuration",
		],	[
			"number",
			"1",
			"Question: \
a developer would like to setup a simple, low cost, static website that delivers html, javascript, images, video and other files to visitors. which action should the developer take?",
			"1",
		],	[
			"string",
			"1"
			"Question: \
amazon ________ is object storage built to store and retrieve any amount of data from anywhere of the internet.",
			"simple storage service (amazon s3)",
		],	[
			"string",
			"1",
			"Question: \
amazon s3 bucket policies and IAM policies are written in whar format?",
			"json",
		],	[
			"number",
			"1",
			"Question: \
___ provides an IP address for an nfsv4 endpoint at which you can mount an amazon efs file system.",
			"3",
		],	[
			"number",
			"1",
			"Question: \
the aws management console is recommended for uploading files larger than 160 GB to amazon s3",
			"2",
		],	[
			"number",
			"2",
			"Question: \
which of the following statements regarding amazon s3 is true? (choose 2)",
			"1, 3",
		],	[
			"number",
			"2",
			"Question: \
which of the following statements about the query operation in amazon dynamodb are correct? (choose two)",
			"1, 4",
		],	[
			"number",
			"1",
			"Question: \
when configuring an s3 bucket for website hosting, how can you grant public access to the bucket?",
			"3",
		],	[
			"number",
			"3",
			"Question: \
which of the following functions does amazon relational database service (rds) do on your behalf? (choose 3)",
			"1, 2, 3",
		],	[
			"number",
			"1",
			"Question: \
when deploying a new efs file system, if there are multiple subnets in an availability zone in your vpc, you create a mount target ____",
			"1",
		],	[
			"number",
			"1",
			"Question: \
which service is a key-value and document database that delivers single-digit millisecond performance at any scale?",
			"3",
		],	[
			"number",
			"3",
			"Question: \
which of the below are examples of cloud computing deployment models? (choose 3).",
			"1, 3, 4",
		],	[
			"number",
			"2",
			"Question: \
which of the following may be configured when creating a new ec2 instance? (choose 2)",
			"1, 4",
		],	[
			"number",
			"1",
			"Question: \
nat gateways allow instances in a private subnet to connect to the internet",
			"1",
		],	[
			"number",
			"2",
			"Question: \
which of the following statements about pagination are correct? (choose two)",
			"1, 3",
		],	[
			"number",
			"1",
			"Question: \
a vpc peering connection can only be established between two vpcs",
			"1",
		],	[
			"number",
			"1",
			"Question: \
what are the basic components of amazon dynamoDB",
			"3",
		],	[
			"string",
			"1",
			"Question: \
which statement about the amazon s3 data consistency model is correct?",
			"Amazon S3 provides strong read-after-write consistency for PUT and DELETE requests of objects in your Amazon S3 bucket in all AWS Regions.",
		],	[
			"number",
			"1",
			"Question: \
using amazon dynamodb, what type of consistency delivers a response after a read request which might not reflect the latest data of a recently complete write operation unless another read request is triggered after a short time?",
			"2",
		],	[
			"number",
			"3",
			"Question: \
which of the following statements about secondary indexes are correct? (choose three)",
			"1, 3, 4",
		],	[
			"number",
			"1",
			"Question: \
which of the following services is not able to access an efs file system?",
			"1",
		],	[
			"number",
			"2",
			"Question: \
which of the following statements about the scan operation in amazon dynamoDB  are correct? (choose two.)",
			"1, 3",
		],	[
			"number",
			"1",
			"Question: \
Which of the following accurately describes cloud computing?",
			"3",
		],	[
			"number",
			"1",
			"Question: \
If a security group is configured with a rule to allow HTTPS traffic to an instance, what will happen if an HTTP connection is attempted?",
			"2",
		],	[
			"number",
			"1",
			"Question: \
An EBS-backed EC2 instance must be _____ in order to change its instance type",
			"1",
		],	[
			"string",
			"1",
			"Question: \
What is the maximum number of objects an Amazon S3 bucket can store?",
			"There is no limit",
		],	[
			"number",
			"1",
			"Question: \
What is an Amazon S3 Bucket?",
			"2",
		],	[
			"number",
			"1",
			"Question: \
The default view of the AWS Management Console displays all resources in all regions.",
			"2",
		],	[
			"number",
			"1",
			"Question: \
When you establish peering relationships between VPCs across different AWS Regions, traffic always stays on the global AWS backbone, and never traverses the public internet.",
			"1",
		],	[
			"number",
			"1",
			"Question: \
VPC peering connections can route traffic using private IPv4 or IPv6 addresses.",
			"1",
		],	[
			"number",
			"4",
			"Question: \
What should you do if your Amazon RDS queries seem to be running slowly? (choose 4)",
			"1, 2, 3, 4",
		],	[
			"string",
			"1",
			"Question: \
Which Amazon S3 feature automatically changes data storage tiers based on your specifications?",
			"Lifecycle configuration",
		],	[
			"number",
			"1",
			"Question: \
By default, Amazon RDS will retain a backup of your DB instance for a period of 7days",
			"1",
		],	[
			"string",
			"1",
			"Question: \
The prices that AWS pricing Calculator uses for the estimates come from the AWS ___",
			"Price List API",
		],	[
			"string",
			"1",
			"Question: \
Which of the following statements regarding auto scaling and load balancing is TRUE",
			"A load balancer will rout traffic to all targets, no matter which availability zone they are in.",
		],	[
			"string",
			"1",
			"Question: \
Application Load Balancers [ALB] use a ________ to verify that traffic should be sent to a target.",
			"health check",
		],	[
			"string",
			"1",
			"Question: \
which of the following statements is true?",
			"An AMI is a template used for launching new instances with identical configurations.",
		],	[
			"number",
			"1",
			"Question: \
When the load balancer detects an unhealthy target, it stops routing traffic to that target even when the target becomes healthy again.",
			"2",
		],	[
			"number",
			"3",
			"Question: \
Which of the following are valid targets for an Application Load Balancer [ALB]? (choose 3)",
			"1, 2, 4",
		],	[
			"string",
			"1",
			"Question: \
An organization has two m5. xlarge EC2 instances - each with 40GM of storage attached. One instance is running while the other is stopped. Which of the following statements is true?",
			"The organization will be charged for 1 running instance and 80 GB of storage.",
		],	[
			"number",
			"2",
			"Question: \
Which of the following statements best describes the shared responsibility model for AWS security?",
			"2, 4",
		],	[
			"number",
			"1",
			"Question: \
Windows and Linux EC2 instances have free tier eligible instance types",
			"1",
		],	[
			"number",
			"1",
			"Question: \
there is no charge for inbound data from the internet into AWS.",
			"1",
		],	[
			"number",
			"3",
			"Question: \
What are the three primary EC2 management functions of EC2 Auto Scaling?(Choose 3)",
			"1, 3, 4",
		],	[
			"number",
			"4",
			"Question: \
Which of the following metrics can be tracked in a scaling policy? (Choose 4)",
			"1, 2, 3, 4",
		],	[
			"number",
			"1",
			"Question: \
IAM users can belong to multiple groups, but IAM user groups cannot be nested.",
			"1",
		],	[
			"number",
			"1",
			"Question: \
By default, a user-created Amazon Machine Image [AMI] is available in all AWS regions.",
			"2",
		],	[
			"number",
			"3",
			"Question: \
Which of the following are true of the root user in an AWS account?",
			"1, 2, 4",
		],	[
			"string",
			"1",
			"Question: \
The ____ estimate path enables you to generate an estimate for the Amazon EC2 instances with an hourly snapshot requirement.",
			"advanced",
		],	[
			"string",
			"3",
			"Question: \
which of the following are security principals for the principal element of a resourced-based policy? (choose 3)",
			"IAM User,  IAM Role,  AWS Services",
		],	[
			"string",
			"1",
			"Question: \
which of the following is an example of an EC2 instance type?",
			"m5.large",
		],	[
			"number",
			"2",
			"Q.which of the following statements about the query operation in amazon dynamodb are correct? (choose two)",
			"1, 3",
		],	[
			"number",
			"1",
			"Question: \
Amazon EC2 provides secure and resizable _____ in the cloud.",
			"3",
		],	[
			"number",
			"1",
			"Question: \
an architect designed their database schema to make the most commacon and important database queries as fast and as inexpensive as possible. which aws database service is best suited to achieve their goal?",
			"2",
		],	[
			"number",
			"2",
			"Question: \
which statements are true regarding vpc peering connections? (choose 2)",
			"1, 2",
		],	[
			"number",
			"1",
			"Question: \
Which service allows two Linux applications running in different AZs to share a common file system?",
			"1",
		],	[
			"number",
			"1",
			"Question: \
Amazon ___ is object storage built to store and retrieve any amount of data from anywhere on the internet",
			"3",
		],	[
			"number",
			"2",
			"Question: \
Which are NOT valid types of Auto Scaling? (CHoose 2)",
			"4, 5",
		],	[
			"number",
			"2",
			"Question: \
Which of the following statements regarding Amazon S3 is TRUE? (Choose 2)",
			"1, 3",
		],	[
			"number",
			"2",
			"Question: \
Which of the following statements is TRUE regarding Amazon S3 pricing? (Choose 2)",
			"3, 4",
		],	[
			"number",
			"1",
			"Question: \
Which protocol does Amazon EFS supports",
			"3",
		],	[
			"number",
			"4",
			"Question: \
What should you do if your Amazon RDS queries seem to be running slowly (choose 4)",
			"1, 2, 3, 4",
		],	[
			"number",
			"1",
			"Question: \
_____ act as a virtual firewall that controls the traffic for one or more instances.",
			"2",
		],	[
			"number",
			"1",
			"Question: \
Which AWS pricing model offers lower prices on AWS Compute and AWS Machine learning across any region?",
			"4",
		],	[
			"number",
			"1",
			"Question: \
Which Amazon EC2 pricing model adjusts based on supply and demand of EC2 instances?",
			"3",
		],	[
			"number",
			"1",
			"Question: \
What happens if you do not specify a weekly maintenance window when creating your RDS DB instance?",
			"1",
		],	[
			"number",
			"1",
			"Question: \
Which of the following can NOT be included when creating an Amazon Machine Image (AMI)?",
			"3",
		],	[
			"number",
			"1",
			"Question: \
Which of the following statements is true?",
			"1",
		],	[
			"number",
			"1",
			"Question: \
Every AWS Region is made up of at least ___ Availability Zones.",
			"3",
		],	[
			"number",
			"2",
			"Question: \
Which of the following can be used to restrict access to specific EC2 instances? (choose 2)",
			"3, 4",
		],	[
			"number",
			"1",
			"Question: \
An architect designed their database schema to make the most common and important database queries as fast and as inexpensive as possible. Which AWS database service is best suited to achieve their goal?",
			"2",
		],	[
			"number",
			"3",
			"Question: \
Which of the following are true statements regarding default VPCs? (choose 3)",
			"2, 3, 4",
		],	[
			"number",
			"4",
			"Question: \
Which of the following metrics can be tracked in a scaling policy? (Choose 4)",
			"1, 2, 3, 4",
		],	[
			"number",
			"1",
			"Question: \
When the load balancer detects an unhealthy target, it stops routing traffic to that target even when the target becomes healthy again",
			"2",
		],	[
			"number",
			"1",
			"Question: \
Which of the following automates the creation, retention and deletion of EBS snapshots and EBS-backed AMIs?",
			"1",
		],	[
			"number",
			"1",
			"Question: \
Which of the following best describes an AWS Region?",
			"2",
		],	[
			"number",
			"1",
			"Question: \
EC2 Instance Connect requires a user-created and downloaded SSH key.",
			"2",
		],	[
			"number",
			"1",
			"Question: \
In an IAM policy. which option designates the API calls to allow or deny?",
			"4",
		],	[
			"number",
			"1",
			"Question: \
Elastic Block Store (EBS) volumes are automatically replicated within an Availability Zone",
			"1",
		],	[
			"number",
			"1",
			"Question: \
___ are key-value pairs which allow a user to add custom content and metadata describing an EC2 instance",
			"4",
		],	[
			"string",
			"1",
			"Question: \
Increasing the number of Amazon EC2 instances behind a load balancer is an example of ________ scaling.",
			"Horizontal",
		],	[
			"number",
			"1",
			"Question: \
Which is nnot a valid example of a Cloud Computing Model?",
			"3",
		],	[
			"number",
			"3",
			"Question: \
Which database engines does Amazon Relational Database Service (RDS) support? (Choose 3).",
			"2, 3, 4",
		],	[
			"number",
			"1",
			"Question: \
There is a 20 KB limit on Amazon S3 bucket policy sizes.",
			"1",
		],	[
			"number",
			"1",
			"Question: \
You can peer VPCs across AWS Regions.",
			"1",
		],	[
			"number",
			"1",
			"Question: \
EC2 Intance Connect allows a user to connect to a —--- instance via —-- .",
			"2",
		],	[
			"number",
			"1",
			"Question: \
Changing the EC2 instance ____ allow you to scale it to the demands of a workload",
			"4",
		],	[
			"number",
			"1",
			"Question: \
which of following allows a user to connect to a LINUX amazon EC2 instance via SSH client?",
			"2",
		],	[
			"number",
			"1",
			"Question: \
When launching an Amazon EC2 instance, which option can be selected for the instance location?",
			"2",
		],	[
			"number",
			"1",
			"Question: \
Which of the following AWS services provides resizable compute capacity in the cloud, designed to make web-scale computing easier for developers?",
			"1",
		]
	]
	_quest_count = len(_quest_list)
	def search(self, str):
		diff_list = []
		for i in range(self._quest_count):
			diff_list.append(SequenceMatcher(None, str, self._quest_list[i][2]).ratio())
		return self._quest_list[diff_list.index(max(diff_list))]

def mouseClick():
	pyautogui.dragTo(button="left")
	pyautogui.dragTo(button="left")
	pyautogui.dragTo(button="left")
	pyautogui.dragTo(button="left")
	pyautogui.dragTo(button="left")

# 설정?
pyautogui.FAILSAFE = False
status = 0
sub_status = 0
while 1:
	if status == 0:
		time.sleep(0.5)	
		print("[MACRO] finding something...")
		xPos = pyautogui.locateOnScreen("x_button.png", confidence=0.95)
		wPos = pyautogui.locateOnScreen("wrong_button.png", confidence=0.95)
		tPos = pyautogui.locateOnScreen('take_button.png', confidence=0.95)
		if xPos != None and sub_status == 0:
			status = 1
			continue
		elif wPos != None:
			print("[MACRO] wrong answer, sorry...")
			pyautogui.moveTo(wPos.left/1.9, wPos.top/1.9, duration=0.2)
			mouseClick()
			status = 1
			continue
		elif tPos != None:
			print("[MACRO] take!")
			pyautogui.moveTo(tPos.left/1.9, tPos.top/1.9, duration=0.2)
			mouseClick()
			status = 0
			sub_status = 0
			continue
	elif status == 1:
		sub_status = 1
		print("[MACRO] question detected")
		# 문제 읽기
		pyautogui.screenshot('capture.png', region=(77, 150, 3300, 480))
		cimg = Image.open('capture.png')
		ctxt = pytesseract.image_to_string(cimg)
		print("---------------------------------------------")
		print(ctxt)
		print("---------------------------------------------")

		# 버튼 위치 파악하기
		count = 0
		button_left = []
		buttons = []
		for i in pyautogui.locateAllOnScreen('smallbox.png', confidence=0.95):
			if (int((i.left - 25 * count)/190) * 100 not in button_left):
				button_left.append(int((i.left - 25 * count)/190) * 100)
				buttons.append([(i.left - 25 * count)/1.9, (i.top/1.9)])
				count += 1
		print("[MACRO] buttons found :", len(buttons))

		# 답 리스트 만들기
		qInstance = Quest()
		question = qInstance.search(ctxt)
		answers = []
		max_count = len(buttons)
		diff_list = []
		if (question[0] == "number"):
			for i in range(int(question[1])):
				answers.append(int(question[3].split(", ")[i]))
		else:
			for i in range(max_count):
				pyautogui.moveTo(buttons[i][0], buttons[i][1], duration=0.2)
				cimg = pyautogui.screenshot('answer'+str(i)+'.png', region=(buttons[i][0] * 1.9 - 100, buttons[i][1] * 1.9 - 450, 450, 450))
				ctxt = pytesseract.image_to_string(cimg)
				diff_list.append(SequenceMatcher(None, ctxt, question[3]).ratio())
		if (question[0] == "string"):
			answers.append(diff_list.index(max(diff_list)) + 1)
		print("[MACRO] answers found :", answers)
		for answer in answers:
			pyautogui.moveTo(buttons[answer - 1][0], buttons[answer - 1][1], duration=0.2)
			mouseClick()
		print("[MACRO] click complete!")

		aPos = pyautogui.locateOnScreen('answer_button.png', confidence=0.95)
		pyautogui.moveTo(aPos.left/1.9, aPos.top/1.9, duration=0.2)
		mouseClick()
		status = 0
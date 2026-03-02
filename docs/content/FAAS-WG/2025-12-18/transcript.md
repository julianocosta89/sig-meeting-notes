SIG: FAAS WG
Date: 2025-12-18
Duration: 31 minutes
Zoom Recording URL: https://zoom.us/rec/share/O9gogOhr3z9Izm_xaaeymizACE2USdMks3xj-uYLIvBb7E_aoxCW4fTNXb9bqq1x.uZ1yBhyE8Wy9Ubun
============================================================

## Zoom Recording Transcript

**Bhaskar Banerjee** 01:03 Hey, Stephen.
**Stephen Hong** 01:06 Hey, Bosker, how are you doing?
**Bhaskar Banerjee** 01:08 Doing good, it's one thing.
**Stephen Hong** 01:10 Yeah, yeah.
**Bhaskar Banerjee** 01:15 Are you taking off next week, Stephen? Are you in?
**Stephen Hong** 01:17 Yeah, I'll be, out of the office starting next week.
**Warre Pessers** 01:33 Hi, dude, afternoon for me, maybe good morning for, some of you.
**Bhaskar Banerjee** 01:40 Hey, good day.
Not sure who all is in which time zone. Stephen and I are from Capital One.
Usa.
Not sure where we all are located.
Good day. Hello to all of you all.
**Tyler Benson** 01:57 Hello, hello!
**Bhaskar Banerjee** 02:03 I guess I met Tyler two weeks back.
And he mentioned that the meet is not happening on that day.
**Tyler Benson** 02:09 Yeah. I think I also met you, several months ago, when you attended the meeting last time.
**Bhaskar Banerjee** 02:16 That's right, that's right, yes.
**Warre Pessers** 02:25 Yeah, so I know we have…
some pretty new contributor named Lucas, who was supposed to be joining, but…
He's, offline on Slack, so maybe he's forgotten.
So I think we can get started anyway.
**Bhaskar Banerjee** 02:45 We guys don't have access to the… Document from our…
company laptops, so we have not been able to add an entry for us.
**Warre Pessers** 02:59 Yeah, let me look if I can bring up the documents…
**Bhaskar Banerjee** 03:04 Thank you.
**Tyler Benson** 03:06 I'm working on, updating the calendar invite to have the new document.
**Warre Pessers** 03:11 Yeah, that's great.
I'll, I'll share my screen.
For now.
This one… Okay, so you should be able to… See my screen now?
**Bhaskar Banerjee** 03:33 Lucas heading from Capital One.
that's… Welcome, you know.
**Warre Pessers** 03:40 So that should be a colleague of yours.
**Bhaskar Banerjee** 03:42 Yes, how come you don't? I haven't.
Known him or heard about him.
**Warre Pessers** 03:50 has been doing some work on the Collector mostly recently, I believe. He's been pretty involved. He was going to introduce himself today, but…
I don't know, he's not here, so… Maybe next time.
**Bhaskar Banerjee** 04:04 You mean collector for the, Lambda?
**Warre Pessers** 04:07 Yes, specifically, the collector lambda layer, indeed.
**Bhaskar Banerjee** 04:12 And what has he been working on?
**Warre Pessers** 04:15 some more logging capabilities. I also saw that he added some… it's still an open PR for some of the AWS Lambda telemetry API metrics that are exposed.
And there's some stuff that's been reviewed by Serkin as well, but I don't have it top of mind what that was about.
**Bhaskar Banerjee** 04:37 Got it. Good to know, thank you.
**Warre Pessers** 04:39 Okay, so you, want me to add an entry for you? I'll also add your names in the documents, to reflect that you're attending.
Okay, so do you want to add something to the agenda, Baskar, or not?
**Bhaskar Banerjee** 05:20 Yes, I have an item to ask in the agenda.
**Warre Pessers** 05:25 I think there's nothing else for now, so, you can go ahead.
**Bhaskar Banerjee** 05:29 Okay, thank you.
Capital One is a very heavy Lambda user.
And, for a couple of years, it has been using New Relic as its APM agent.
And when we are trying to move away from the Neuralink APM agent, or rather to say, the Neuralink APM layers.
to open telemetry layers.
We are seeing a significant increase in the cold start times.
and also… A moderate increase in the execution times.
I have compared the E dot layers.
I have compared AWS's application signals
I've compared it with the collector extension and without the collector extension.
But either way, the cold starts are not Actually, coming down significantly.
So you want to know… Has there been any study?
Or any other report.
Of such comparison, because our users are not
Very willing to accept the increase in cold starts.
and V before… Trying to invest more.
Want to find out.
If there are any such reports, because I believe we'll not be the only ones in this predicament.
Hence this question.
**Warre Pessers** 07:05 Yeah, definitely. I've seen this at my company as well, and I know that Serkan, who, is currently on holiday, so he isn't here, but he has done some work in the past,
to significantly improve cold starts, but that was specifically for the Node.js layer.
**Bhaskar Banerjee** 07:26 Wasn't it Python?
**Warre Pessers** 07:28 I believe it was the Node.js player, since I know he's done a lot of work on the bundling setup and did some complicated stuff with the tree shaking that's going on there.
I don't think it was for the Python layer that he's, investigated that.
**Tyler Benson** 07:49 Baskar, what, what languages are you using that you're seeing these cold start delays on?
**Bhaskar Banerjee** 07:54 Or… so… the maximum increase… let me just bring up my documentation, I can tell you.
How much we are seeing in water.
**Tyler Benson** 08:06 And are you seeing that mainly from the addition of the language layer, or the collector layer?
**Bhaskar Banerjee** 08:14 the SDK. Collector also adds the cold start, needless to say.
But, that is… that runs…
For a couple of hundred milliseconds.
And I would say under half a second.
But the majority is from the SDK. So, let me just pull up my numbers here.
And what I'm seeing is… for Java.
the Neuralink SDK is about 75%.
Faster.
Then open telemetry.
In terms of… Cold start.
or Python.
It is about 25% faster.
than open telemetry.
And… For cold starts.
And about 90% Faster.
For normal executions.
for JavaScript, Neuralink is about… Little more than 40% faster.
Then, open telemetry.
For gold starts?
And roughly about… 90% faster.
for execution times. Now, the execution times can vary significantly.
But the cold starts when they go up.
cause the trouble. And I'll give you some numbers.
we ran a Hello World application.
with Neuralink.
And with OpenTelemetry.
The P99 cold start time for Neuralink was 1250 milliseconds for Java.
And… 5,000 milliseconds for Java for OpenTelemetry.
Likewise.
for Python, Neuralix P99 of Cold Start was 1400.
While that with open telemetry was 1900.
JavaScript.
Neuralink?
P99 cold start was 1200.
While with OpenTelemeter, it was 2100. So, some numbers here. I also have documentation about the execution times.
This is, in general, what we are seeing.
**Tyler Benson** 10:43 So, I… I think it would be, very valuable to… if you guys are able to, you know, do some deeper dives and try to identify specifically what part of the execution
startup is taking the most time. I imagine with the Java agent layer instrumentation that there is some instrumentation that you could potentially disable to improve that startup time.
I would also be curious if, these lambda layers, are they, fairly large in…
Like, the number of classes that it's loading, or are they pretty small?
**Bhaskar Banerjee** 11:29 Well, the layers are built directly from the open source.
**Tyler Benson** 11:33 No, I mean, like, sorry, not the layers that you're building, but the actual lambdas.
**Bhaskar Banerjee** 11:39 The actual lambda is a hello world lambda, pure hello world lambda.
**Tyler Benson** 11:43 Okay, so, very small, low class loading.
**Bhaskar Banerjee** 11:48 Yes, indeed.
**Tyler Benson** 11:54 And is a Hello World, type application, fairly indicative of the, the size of, lambdas that you, execute in, in Lambda?
**Bhaskar Banerjee** 12:06 Not at all. It's actually inverse.
But I have not… see, customer… real customer applications vary significantly.
**Tyler Benson** 12:16 Oh, I understand.
**Bhaskar Banerjee** 12:18 I did not have bandwidth of testing several kinds of applications, but this was primarily testing,
Between two different vendors.
How it is faring.
**Tyler Benson** 12:31 Yeah, no, I'm just trying to get an idea of the shape of the problem here.
Got you.
**Bhaskar Banerjee** 12:37 No, it is not. It is rather opposite. None of our application lambdas are… So simple, or so tiny.
**Tyler Benson** 12:45 Okay.
So,
If anything, your normal application startup would be a lot worse, because they'd be loading a lot more classes, presumably.
**Bhaskar Banerjee** 13:00 That is right. In real world,
Applications do take much longer for a cold start.
than what I have indicated from a Hello World Lambda. And that is why, many times, these cold start times… so we are already using these layers, open source layers, and many times, these costs get absorbed, and people do not notice it so much.
But then we do have few customers who are extremely picky.
Because the applications… Extremely high throughput, which means more than 600 TPS.
And latency less than 60 milliseconds.
**Tyler Benson** 13:42 Yeah.
**Bhaskar Banerjee** 13:43 So their… their open telemetry is unable to help so much, and we're trying to see what can be done.
**Tyler Benson** 13:49 Okay.
So…
have, I don't know how difficult it would be, but it might be useful if, there's some way that you can export, some profiling information on that startup period.
To help you identify specifically what part of the startup process is making it take a long time.
On the Java agent side, I imagine a lot of it is just the class transformations, but, the fact that… Sorry,
maybe less so, actually, because you are doing a small application, so maybe it's more on the… just… the overall Java agent is… is fairly big and takes a long time to initialize.
**Bhaskar Banerjee** 14:50 Quite possible.
And yes, I have not used Snapstart on this, any of these.
Just like I have not used Snap Start on the new regulators either.
**Tyler Benson** 15:01 Yeah.
**Bhaskar Banerjee** 15:02 Fold start.
So, when is Zirkin back?
**Tyler Benson** 15:14 After the New Year?
**Warre Pessers** 15:16 Yeah.
**Bhaskar Banerjee** 15:17 Okay, so… if we come back to the meat that is on…
So I guess there won't be a meet on third… on 1st, right?
**Tyler Benson** 15:32 Right. So, the next meeting will be on the 15th, I think.
**Bhaskar Banerjee** 15:36 15th?
**Tyler Benson** 15:37 Okay. Of January.
**Bhaskar Banerjee** 15:40 15th, same time, fine. We'll be here.
And let's see if we… most of our team is also out, but we'll see if…
We can have any further information on this.
**Tyler Benson** 15:51 Yeah.
I mean, I don't know that Serkin's gonna necessarily have a specific answer either. It sounds to me… are you saying that Java is probably the biggest problem that you're facing?
**Bhaskar Banerjee** 16:06 Yes, that is true.
**Tyler Benson** 16:08 Yeah, so,
I don't think any of us have really spent a lot of time recently on trying to optimize that, unlike Serkin with the JavaScript layer. So on the Java layer.
I think that we're open, if you have some time or some resources to spend on identifying ways to improve that, we are certainly open to… to suggestions. The other thing that you might explore is, finding
Ways to optimize, just the, the settings that the Java agent exposes.
I think that you could probably get a lot of, mileage just by testing it locally, and seeing how the different, cold start options and, sorry, the, sorry, the different, settings for the Java agent.
compare on running it locally instead of doing everything in Lambda. Because I imagine that the, the performance is going to be fairly, similar, assuming that, you.
constrain the, the memory, configuration in a similar way as what you do in Lambda.
**Bhaskar Banerjee** 17:32 Right.
We'll gather some thoughts around that, and test… try testing.
**Tyler Benson** 17:39 Yeah. Cause, like.
I imagine that the way that you would need to approach this for optimizing the performance, is gonna be the same, whether you're running on a, you know, a self-hosted machine versus Lambda.
**Bhaskar Banerjee** 17:56 Agree, agree. It just, boils up quickly on Lambda because there are more cold starts, but yes, the actual challenge of the SDK's cold start is the same, whether I run it on an instance or I run it on a serverless, so…
**Tyler Benson** 18:11 Right. And so, the reason I'm suggesting trying to run it in an environment that you have more control over is I think it would be easier to get profiling data.
So if you can run it with a profiler to start… to show the startup, then you can, I think, help… I think that would help you identify, what some of the, the…
the CPU, or all the time… startup time is being spent.
**Bhaskar Banerjee** 18:42 Got it.
Thank you. Yeah. We'll, we'll try this.
**Tyler Benson** 18:46 And…
If you identify specific things that are taking a long time in startup, that also might, help you identify settings that you can use to disable.
So, for example, I believe that if you disable all the extra instrumentation that you don't need.
on the Java agent, I believe that that might have some startup improvements, because it doesn't need to do as much evaluation when it's trying to load classes.
**Bhaskar Banerjee** 19:22 I agree on that, but the reason we have not done that is there will be customers who need these instrumentations, and when they turn it on, they're gonna yell at us.
while comparing same with Neuralink, they don't have this such a challenge.
So, I'm… I'm not…
**Tyler Benson** 19:40 Does New Relic have as extensive of instrumentation?
**Bhaskar Banerjee** 19:45 Well, I have not compared every instrumentation, to be honest.
**Tyler Benson** 19:49 Yeah, I don't know what's in the New Relic Lambda layer either, but I imagine that they probably have a…
A smaller subset.
**Bhaskar Banerjee** 20:00 I have to check honesty, I don't have…
The details of what all instrumentations they support.
**Tyler Benson** 20:11 So…
Yeah, at the current point in time, the Lambda SIG is very much, you know, just keeping the lights on kind of stage, for staffing.
We
we don't really have… we're all volunteers at this point. I used to be more professionally supported from my company in being involved in OpenTelemetry, but that… my positions changed such that that's not the case anymore.
And, Warre and Serkin are both volunteers. Neither of them are…
Being sponsored by their companies to do this, so, when I was,
being sponsored by my company, I was, given a lot more flexibility and freedom to make big changes, because I was able to spend more time on it, but…
At this point, we are relying a lot more on, users, to bring, ideas and, mainly contributions to the table to help move the, SIG forward.
**Bhaskar Banerjee** 21:22 Got it.
Understood.
Thank you. I mean, let's go back and do some search on…
Running this locally, and see if we can mine some more information.
We'll come back.
**Tyler Benson** 21:39 Cool, yeah, well, we do appreciate you being involved in the SIG here. Feel free to, drop by any time.
**Bhaskar Banerjee** 21:46 Sure.
Absolutely.
Thank you. Stephen has his hand raised.
Stephen, guilty.
**Stephen Hong** 21:52 Yes, earlier there was a mention about some work being done on the JavaScript layer.
And I would be very interested in seeing that in the next meeting, if possible.
**Warre Pessers** 22:06 Yeah, this has been done in the past. I know this was a big effort on, Serkan's side, but, if he's there, he'll be able to elaborate on what exactly,
He's done back then.
**Stephen Hong** 22:21 Got it. From our side, some…
of our customer teams are using a Node.js lambda.
And they reported that when they switched to using ESM, the…
JavaScript lambda layer adds a lot of, code start.
So, I'll be interested in seeing if this, new JavaScript layer… Supports ESM more efficiently.
**Warre Pessers** 22:51 Well, currently, there's, like, no more ongoing efforts to, to do anything with regards of performance in the Node.js layer, so, you may have misunderstood what I meant, that, like, the work that Sergen has done, it's like…
probably half a year or a year ago. So…
If they are on the current…
layer version, and they are experiencing, a lot of cold start overhead, that'll probably remain.
So, yeah, we can look into that, because there is some ESM-specific stuff in the layer to support ESM lambda handlers.
**Stephen Hong** 23:33 Gotcha. Yeah, the Lambda layer that our customer teams are using are older versions.
I don't think they're using the latest, so there might be a chance that the performance might be better, but I'd be just interested in seeing.
What changes have been made, and maybe we can add more to it.
**Warre Pessers** 23:55 Yeah, definitely. That's good.
Nothing else from your end, Steven or Bhaskar?
**Bhaskar Banerjee** 24:07 Oh, I'm good.
**Stephen Hong** 24:09 Yep, so…
**Warre Pessers** 24:10 Mmm…
**Bhaskar Banerjee** 24:13 Thank you, I'll drop off.
And I'll see you next year. Wish you guys happy holidays and Happy New Year.
**Stephen Hong** 24:19 Happy Holidays.
**Tyler Benson** 24:20 I mean…
**Stephen Hong** 24:21 Thank you. Thank you.
**Tyler Benson** 24:24 Rory, did you have anything else you still wanted to talk about?
**Warre Pessers** 24:28 Not really, so, like, one of the, agenda items that Lucas had put in here is about this,
test suite for Lambda runtimes, I think that's actually, kind of similar to something I had already discussed with Serkin a little bit, or maybe it was Max, I don't remember, but it would be nice if we had, like,
Some sort of integration test for when we are doing a release, maybe, or to run on each
PR, maybe, to see that nothing's really broken in the layer.
**Tyler Benson** 25:06 Yeah. If you look at the,
the AWS, layers, the, for the, AWS distribution?
In their repo, I believe they have, yeah, the A.lambda layer. I believe they have some amount of, similar automated testing, set up, that when we kind of just… when we forked, from their, layer release, we kind of just didn't bring that along.
**Warre Pessers** 25:40 Yeah, I'll have to look into that.
**Tyler Benson** 25:42 Mainly because, we didn't really have… so I still don't know who's paying for the bill,
It might be the,
the, Linux Foundation, or CNCF, I mean.
that has, that we're using their AWS account, so they might have some appetite, to, you know, put a little bit of cost towards automated testing.
if it's gonna be small, I… I don't think they want to,
dramatically increase that bill size, though. So, I think it would be, beneficial to, maybe kind of talk to the governance committee, and figure out who owns it, and…
What, what kind of leeway we have with that.
**Warre Pessers** 26:44 Yeah, definitely. Like…
I just wanted to show this issue, because this is something that I created for this as well. And, like, my idea was to keep it as simple and as small as possible, of course, like…
just some sort of integration test to set up a Lambda function, invoke it, maybe do, like, a very simple AWS SDK call, check if the expected spans are there, and then just destroy that. I don't know if…
we could be able to maybe even remain in, like, the AWS free tier, because then I would assume that,
The committee would be on board with it, but we'll have to,
We'll have to check with them indeed, I think.
But yeah, so the main motivation behind this was that we had a couple of issues, I think back when you were, on holiday.
There was, like, an upgrade of… Something broke.
Yeah, there was an upgrade of require in the middle, messing some stuff up, and then…
A week later, the…
Node24 runtime released, and there was some CommonJS, specific stuff that broke there, so,
we did have, I think, two versions of the layer that don't… Didn't fully,
operate well, let's say.
**Tyler Benson** 28:19 Okay.
**Warre Pessers** 28:20 like…
also maybe to play devil's advocate, but we didn't mention that the layers support node 24 yet, so we published the layers still with only nodes 18, 20, and 22 supported, I believe, so…
In fact, we didn't really break anything, but of course, some people were expecting them to work on low 20…
experience.
**Tyler Benson** 28:47 Yeah.
**Warre Pessers** 28:47 24.
But yeah, that's been fixed in the meantime, but having some sort of test there would have been helpful. What I do nowadays is just test stuff manually,
Which is also an option if we have, like…
Very good samples in the repo, that are very easy to quickly deploy and verify.
Then that may be, a good alternative as well.
**Tyler Benson** 29:16 If we have some… a test suite that can run fairly quickly and use, relatively low resources, and we… even if we just run it on, like, a nightly build,
I think that that would be reasonable.
**Warre Pessers** 29:30 Okay.
**Tyler Benson** 29:31 Assuming that it doesn't add too much complexity to the, the build process.
**Warre Pessers** 29:39 Yeah, I agree. I'll make that an action item then.
And then… yeah, another small update on my end, so this had been,
how do I say this? Stalled little bits, like the SQS context propagation stuff, but I've been moving forward with a…
semconf issue that I had to open, it will be a small change there, and then I also,
am finishing the work for the JavaScript, AWS Lambda instrumentation, so…
That'll be, hopefully, early next year that we really can get that moving, but depends a little bit on
the SEMConf stuff as well, because I think they have…
A lot of open issues and a lot of work, so…
**Tyler Benson** 30:33 Yeah.
**Warre Pessers** 30:33 Things are a little bit slower.
**Tyler Benson** 30:34 Demon stuff's always a challenge to get anywhere with, so…
**Warre Pessers** 30:40 And that's it for me, nothing else.
**Tyler Benson** 30:43 Great. Well, keep up the good work,
I hope you have a good, a good break, and we'll see you back in January.
**Warre Pessers** 30:53 Yeah, you too, enjoy, the holidays.
**Tyler Benson** 31:00 Great. Take care. Thanks for, running it today.
**Warre Pessers** 31:04 Yeah, thank you, and then I'll see you, next year.
**Tyler Benson** 31:11 Yep, cheers. Bye.
**Warre Pessers** 31:13 Goodbye.

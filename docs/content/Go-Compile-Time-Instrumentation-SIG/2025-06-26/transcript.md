SIG: Go Compile Time Instrumentation SIG
Date: 2025-06-26
Duration: 42 minutes
============================================================

## Zoom Recording Transcript

**Przemyslaw Delewski** 02:45 Hello!
**Huxing Zhang** 03:00 Hi! How are you?
**Przemyslaw Delewski** 03:03 Fine. Thank you.
**Huxing Zhang** 03:08 How is your trip to Hong Kong.
**Przemyslaw Delewski** 03:12 It was great, so very beautiful city, nice people. It was great to meet with Ziming, so I am very happy that I was there.
**Huxing Zhang** 03:27 Cool.
**Dario Castañé** 03:50 Oh!
Oh!
**Kemal Akkoyun** 05:40 Hello!
**Dario Castañé** 05:43 Hello!
**Huxing Zhang** 05:44 Hello!
**Przemyslaw Delewski** 05:45 I don't.
**Romain Marcadier** 05:46 They!
**Przemyslaw Delewski** 05:55 Do we expect more people.
**Kemal Akkoyun** 06:00 I don't know. Let's check the calendar.
There's on that.
**Huxing Zhang** 06:13 I think we. We are fine, and we are ready to start.
**Kemal Akkoyun** 06:20 Give it a couple. I think we are mostly cool. He is the like. Who's the teacher today could be me. Maybe it's my turn.
I think the so.
**Huxing Zhang** 06:45 I think the original host was to me, but we have skipped the next meeting. I saw his name the one week before, but actually, we didn't have the meeting.
**Przemyslaw Delewski** 07:00 Yeah.
**Kemal Akkoyun** 07:04 Do you want to do it?
They mean it's.
**Ziming Liu** 07:08 For me facilitated.
Should I be the facilitator.
**Kemal Akkoyun** 07:19 Yeah, if you want too, boy.
But.
**Ziming Liu** 07:21 Okay. Let me check the check. The document.
**Huxing Zhang** 07:30 So maybe we we can combine these 2 weekly meeting minutes together.
**Romain Marcadier** 07:40 Yeah, I'm in the process of rearranging stuff around.
**Huxing Zhang** 07:46 Yes.
**Ziming Liu** 07:56 Can you see my screen.
**Przemyslaw Delewski** 08:00 Yes.
**Ziming Liu** 08:02 Yeah.
3.
So let let us review the actions for the previous meeting that should be here.
And the 1st it's we should add a pr to connect the the instrument framework and the the SDK, and I think I have already at the pr for this. I don't know should. Oh, there are some comments. I will resolve it later. Should I? Have a simple presentation for the for this Pr. I will show.
**Przemyslaw Delewski** 09:00 Yes, yes, please.
**Ziming Liu** 09:03 Yes.
**Przemyslaw Delewski** 09:11 Could you see my screen? Yes.
**Ziming Liu** 09:15 Okay, and I have done a refraction to for the project and the instrumentation model contains the all the instrumentation rule and the hook code.
For example, the Hollow World rules hooked up.
Main function of the of hook. The main function of think of of men, dot go, and the mandograph simply prints a hollowed string, and in the hook code we we'll use the SDK of the instrumentation api and instrumentation Api SIM codes to set to to build the instrument here, and we'll add a extractor of span name which means that when the instrumental is executed, we will generate a span named named Hello World, and the second is the span kind instructor, and it is, I think it is an internal span for the demo use, and the 3rd one is an you mocked uio attributes extractor, and the extractor will extract the the scheme and the URL path, and your query of the of the request, and the request is a object that may be from the framework itself of, for example, the net Http may have a object similar to the request that contains the ui path and parameters and the scheme and I just mocked these values here to make the demo most simpler. And the operation listener is is for the matrix aggregation. And I will use the A instrumentation Api to create to create a matrix that count that record the duration of the Http client invocation.
Yes, and we will use those extensions to build a instrument.
and the instrumental is constructed here.
and we use the instrument to do, start to create a span and use the and to make the span ended and report it to the remote and the maybe we can have a try.
We just execute the build.sh!
And the builder sh will firstly build a hotel binary for the compile time instrumentation, and we will go to the Demo Directory to do the compile time instrumentation and run the demo, and we can see that Some of the spans is printed to the Std. Out, because I have set the exporter to the Std. Out a trace, and both trace and matrix, and we can see that it is the matrix of Httv kind. And this is This is the this is the span that we generated, because yes, it has something like span name span id, and and some attributes like URL Path and the URL scheme that whatever?
Yeah, we can just use the instrumental SDK to generate the span matrix that follows all hotel spec.
Yeah, that is the P. What the Pr does.
**Przemyslaw Delewski** 14:35 Okay, so few comments or questions. So 1st of all, what we have in this Hello, board directories code that will be generated automatically right by the tool.
**Ziming Liu** 14:49 Yes, yes.
**Przemyslaw Delewski** 14:51 Okay. And the second thing is that I made a small fix to the build.sh! Because when I was when I cloned the repo it. It didn't build correctly, because it requires some dependency update, and we have to invoke, go mode tidy. So I I added this line into build 8.sh for now, manually. But of course this is something that we should do in our tool.
**Ziming Liu** 15:27 And.
**Przemyslaw Delewski** 15:27 So you can look at the pull request later. Then.
**Ziming Liu** 15:31 Yes, I will have a look at the comments.
And do you mean we should do the go more, Teddy, in the tour in in the compile time instrumentation tool was something else.
**Przemyslaw Delewski** 15:50 I think that was the goal.
If I am not, if I am correct, so.
**Romain Marcadier** 15:56 I think I think if we are introducing new dependencies in what we are currently building, then we need to manage running the government id on behalf of the user that that comes with potential pitfalls like this week, I've actually had feedback from a customer that if they try to run orchestra and PIN. They get an error that essentially comes from Google Tidy.
And that's because one of container D modules has been split in 2 again and then go mud tidy or like, go get dash you is actually not so hot at handling those and tends to fail, and then you have to manually sort them out. But I would say we should try to do the right thing, and informs the user how what what they're expected to do if if it somehow fails.
That was part of you know the conversation that we were having on the product design.
**Przemyslaw Delewski** 17:12 Yes.
**Romain Marcadier** 17:12 Brief where it was like.
If we do, if we do hotel setup.
and that essentially wires the new dependencies correctly, and then they are in go mode. But then, if we are in the mode where we want to do strictly, 0 changes to checked in code, then that means when we do the instrumentation we have to go through the tidy phase, so Go is able to resolve the dependencies properly.
**Przemyslaw Delewski** 17:42 And this is this is also the part of the documentation that we have already.
**Ziming Liu** 17:49 Okay.
cool any question about this. Pr.
so let's move on to the to next up.
And I think this is from Yang. And
**Yi Yang** 18:33 Yeah, I, I will break down the implementation tasks into smaller tasks today tomorrow.
And and I want, I wonder would it be helpful if I submit a code schedule that created created the overall workflow?
I will. I will leave all functions empty for the implementer to to complete either.
and and each function would represent a specific task. Do you think it makes sense.
**Przemyslaw Delewski** 19:26 Yeah. So so the the plan you plan to do that tomorrow right?
**Yi Yang** 19:34 Yes.
Tomorrow I will, I will. I will break down the implementation tasks into smaller parts. And I will submit a code schedule that create the over overall, workflow.
**Romain Marcadier** 19:55 Okay.
**Przemyslaw Delewski** 19:59 Do you think the is there something that we can discuss today, or should we? I don't know, discuss this asynchronously on Slack, for instance.
**Yi Yang** 20:21 I don't have any comments at present.
**Przemyslaw Delewski** 20:27 Okay.
**Kemal Akkoyun** 20:29 I think we either we can use issues or slack maybe slack is easier to discuss with the proposed tasks.
And then we can update this issue.
**Przemyslaw Delewski** 20:45 Sounds good.
**Yi Yang** 20:47 Okay.
**Romain Marcadier** 20:47 I agree.
**Ziming Liu** 20:51 Yes, I think we can. Write some libraries for like what?
The open time as you go, country dots, and we can write something like this because it is independent. With the compilation framework we can just use the instrumentation.
api and instrumentation simcom, to have a encapsulation of the of this.
for example, the Grpc and Net. Http. We can just encapsulate it, and after the compilation framework is down, we can just just make it works.
**Przemyslaw Delewski** 21:44 It can be. Do parallel, I think.
Yes.
**Ziming Liu** 21:49 So I will add the task the small task into these issues. And we may implement some important plug in, for example, the net Http, Grpc. And something else in the Mlp version.
and we can do that parallelly.
**Przemyslaw Delewski** 22:17 We can do that parallelly, and these tasks are independent. But I think that the most important thing would be to to be able to generate all the stuff from this from the tool right? So.
**Ziming Liu** 22:32 Yes.
**Przemyslaw Delewski** 22:33 Extended tool to manipulate ast, and also to to do this 1st stage, which is about updating dependencies.
**Ziming Liu** 22:50 Okay.
let me have an action action items.
**Przemyslaw Delewski** 23:03 In my opinion, one of the tasks might might be to generate something that you did manually. So you you created this Hello World Directory that contains this, this very basic demo. And we could.
we could have a code for that to automatically generate this kind of stuff.
That would be, for instance, one of the 1st step.
**Ziming Liu** 23:47 Action items, connection items.
**Huxing Zhang** 23:55 Maybe you can uncheck that box. You may will leave the checkbox open. Yeah.
**Ziming Liu** 24:05 I don't know how to use that.
**Huxing Zhang** 24:09 Never mind you. You can.
**Ziming Liu** 24:11 Like you see it later, you can just.
**Huxing Zhang** 24:14 Keep the notes. I think.
**Ziming Liu** 24:17 Yes, let's move on, and think the next is from Kamel, and facilitators should follow the easy to gain access, to let me open the issue.
**Kemal Akkoyun** 24:38 Yeah, it's just an example issue so to be be able to see the these like zoom passwords, you need to get access to that Google, Doc. And for that you need to open an issue like this. This is not also automated.
And and then, so there are. Yeah, if you see the calendar, it will tell you that this is the zoom account, too, and there is a password for zoom account, too, and you can use it for moderating the meetings this is for the for the previous incident that we had where we couldn't meet the people when we needed. So, yeah, I like, I have it right now. But I think, if I'm not around in the meeting I think any of the facilitators should have this.
**Ziming Liu** 25:31 Okay, I will try to try to do this.
**Kemal Akkoyun** 25:38 Nothing urgent. But yeah, just to be on the safer side.
**Ziming Liu** 25:43 Okay?
And release, Doc, this is Huang. Hushi, yeah, we.
**Huxing Zhang** 26:02 In the open telemetry community has not a common release like specification, and which defines how we do release a common like process say it covers the like versioning, semantic versioning, and how how frequently we do the release or to the like general ideas. But we actually, we didn't have release right now. And so the go compile time, instrumentation sick has not been list here. So maybe we can like follow. This just won't bring this up and we are ready for the 1st release. We can. Maybe we can follow this document. Yeah.
**Przemyslaw Delewski** 27:01 Okay.
**Kemal Akkoyun** 27:02 Sounds good. I think I'm trying to find out. Okay.
alright, there I exist. Okay, I'm like, I think we will release binaries, and we should check a project that actually release the binaries.
I think this is like collectors whatnot instead of like like getting an example from a a library, I guess.
But then, again, like we can do this whenever we have our 1st release, or whenever we would start cutting our releases.
**Huxing Zhang** 27:36 Yeah.
**Przemyslaw Delewski** 27:37 Yeah.
**Ziming Liu** 27:41 Yes, so I think. That is all the topics we should discuss.
**Kemal Akkoyun** 28:06 I think the most important thing is this, like splitting the tasks? I think we are. We should be like We shouldn't wait for the next meeting. And let's do this on slack, and we can also separate things in a larger chunks. And then the owners of those larger chunks can create their own issues. We have a project board to track those.
So I think let's get that out of the way and start like producing some code. I would say.
**Przemyslaw Delewski** 28:41 Yeah, that makes sense to start from the larger part.
split them into smaller, because probably this issues or tasks might might also evolve over time.
**Kemal Akkoyun** 28:58 I think so.
**Romain Marcadier** 28:59 Yep, which is actually also why, like, we probably don't need to overthink it too much. Like no thing. Nothing is going to be an inevitable problem. If we take a wrong turn there, we can always course correct.
**Przemyslaw Delewski** 29:19 Yeah.
**Kemal Akkoyun** 29:21 Agreed.
I think this should be just something that we prevent that, like 2 people working on the same issue.
**Romain Marcadier** 29:31 Yeah, exactly. And and it also is going to stimulate actual progress happening, which I think is a good thing.
**Przemyslaw Delewski** 29:39 Yes.
**Kemal Akkoyun** 29:45 There's the one.
**Ziming Liu** 29:46 Of course.
Okay, think let me let me split the task, and make it smaller and smaller on the slack.
and just a move forward to the 1st Mvp.
**Romain Marcadier** 30:13 Yep.
**Huxing Zhang** 30:15 I think it's worth discussing that what is the 1st Mvp version should include what is look like for the 1st time we see version or netcode.
What should they contact us.
**Przemyslaw Delewski** 30:32 Yeah.
So in my opinion, we should choose one of the library or framework like Http and provide instrumentation for that. So to have everything what's needed from the framework perspective and from the library perspective.
**Huxing Zhang** 30:52 Yep.
Sounds good.
**Romain Marcadier** 30:56 Yeah.
**Ziming Liu** 31:08 Okay.
that is net. Http server and the client. We can just implement the most frequently used Http framework that go native Http.
**Przemyslaw Delewski** 31:33 Yes.
**Ziming Liu** 31:37 Okay.
okay, any any comments, any more comments for the meeting.
**Huxing Zhang** 31:59 So we we should target this 1st Mvp, and when we split tasks, maybe we should target this Mvp. And to make sure all the things can be covered in this Mvp. Version.
**Ziming Liu** 32:17 Yes, we will. As something like What instrument does here, and use the instrumentation Api to encapsulate it.
In the 1st Mvp version, our will create the subtask. I will try to implement it.
One.
yeah.
And from the comparison framework perspective.
should we just follow the documents that we merged previously.
**Przemyslaw Delewski** 33:45 Yes, I think so. That that was the goal to to have our kind of specification.
**Romain Marcadier** 34:05 Note that if during implementation it turns out some of the stuff in the documentation needs to change like a Pr to the documentation is absolutely an option.
**Przemyslaw Delewski** 34:18 Yeah, this, this might always happen.
**Romain Marcadier** 34:21 Yeah, like I. But I just wanted to be like, extremely clear is that it's not like, we're we're not bound to that.
If it does not work because we didn't know everything at the time, so.
**Przemyslaw Delewski** 34:36 Yes.
**Romain Marcadier** 34:37 It should, it should guide the implementation. But the implementation might actually teach us about stuff that we thought wrong then, and then we should feel free to fix them.
**Huxing Zhang** 34:48 Right, yeah.
**Przemyslaw Delewski** 34:48 So, yeah.
documents describes our understanding at the moment when we were creating these documents. Right? So this might change.
**Romain Marcadier** 35:00 Exactly.
but I guess the idea is to try and keep the doc and implementation aligned.
**Przemyslaw Delewski** 35:11 Yes, that that that's for sure.
**Ziming Liu** 35:29 Cool.
and should we have time schedule for the 1st mip.
**Kemal Akkoyun** 35:50 You don't need to decide it right now. Let's start and.
**Ziming Liu** 35:54 Okay.
**Kemal Akkoyun** 35:54 Maybe in a couple of weeks we will know more, and then we can come up with some estimations or goals.
**Ziming Liu** 36:03 Okay.
right?
But so I mean more topics to discuss.
**Huxing Zhang** 36:23 No just want to share that. I was planning to travel to the United States for the Hotel Community day, but due to some policy company policy. I can't do that. So I just I have have to say that I have to cancel that trip to the hotel community day in North America. So that's a kind of things that the didn't want to see. But right, yeah, maybe it's for this this kind of time. It's bit harsh for us to like travel to us right now. Yeah.
**Romain Marcadier** 37:17 Yeah.
**Kemal Akkoyun** 37:18 Okay, that's.
**Romain Marcadier** 37:19 And definitely.
Yeah, I can definitely relate with the feeling, because I experienced the same when I was looking to go to Singapore or to Hong Kong, where it was just like sorry. That is literally just not possible at the time.
**Huxing Zhang** 37:36 Yeah, yeah.
**Ziming Liu** 37:39 Yeah.
**Kemal Akkoyun** 37:42 Okay. That also reminded me that we have another deadline for a for a conference. The observability day. This happens in the 0 day of Kubecon.
I think there's a deadline for it, and it is next Monday.
To be on the safer side. I want to submit the talk that we submitted to the Kubecon into this event as well.
Yeah, let's see.
So I know.
**Przemyslaw Delewski** 38:17 The same one. Right. This, the same proposal.
**Kemal Akkoyun** 38:20 Wow!
A same proposal, maybe tweak it a little bit. This is accepted for Kubecon, because if they don't accept that to the main track observable today is a good place to do this.
So let me check if you still opt. For this I can put your name as a second again.
**Przemyslaw Delewski** 38:40 Yeah, okay, of course, no problem.
**Huxing Zhang** 38:46 Yeah. And we normally do this. Yes, because, actually, the conference program committee recommend us to submit both to the main conference and the the co-locating event.
**Kemal Akkoyun** 39:01 Yeah.
and they are nice. Right now, if you got a talk accepted in co-located event, they give you a coupon ticket as well.
Wasn't the case before. So it's 1 of the easiest way to do this cool. I will do that as well. Hopefully.
**Przemyslaw Delewski** 39:24 Cool.
**Kemal Akkoyun** 39:28 You can aim to like, have a some sort of a Ga product by then. What do you think? Is it too ambitious?
I think we can do it.
**Huxing Zhang** 39:38 Yes, let's try to target for that.
I think we can take some.
**Przemyslaw Delewski** 39:43 I'm not sure if that will be ga, but.
**Huxing Zhang** 39:46 Yeah, actually, we can make something out. Yes, we can. Maybe at least we can. Demo.
I see.
**Przemyslaw Delewski** 39:53 Yeah.
**Kemal Akkoyun** 39:56 Okay.
aim for it. It's a good deadline, but we can talk about it here. You can use it.
**Huxing Zhang** 40:10 Okay.
**Ziming Liu** 40:13 30, at 10 o'clock.
**Huxing Zhang** 40:14 Thank you. I think it's all survey.
**Yi Yang** 40:20 Okay. Bye-bye.
**Przemyslaw Delewski** 40:22 Okay.
Thank you. Bye.
**Romain Marcadier** 40:25 Bye, good day.
**Kemal Akkoyun** 40:27 Bye, bye.

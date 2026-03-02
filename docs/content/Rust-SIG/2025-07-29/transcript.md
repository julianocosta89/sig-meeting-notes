SIG: Rust SIG
Date: 2025-07-29
Duration: 23 minutes
Zoom Recording URL: https://zoom.us/rec/share/yM1vUTqZyVx31LGOr7-kBHI9BiV2YmdUY147BrYM6a8qQNzellg7PWIrZpgGd26s.YIsR92mhzOQ_vtuz
============================================================

## Zoom Recording Transcript

**Utkarsh Umesan Pillai** 02:41 Hey? Nickel.
**nikhil bhatia** 02:46 Hi! Utkash.
**Utkarsh Umesan Pillai** 02:48 Hi, are you? I haven't seen you in the Sig meetings before. Is this your 1st time?
**nikhil bhatia** 02:53 Yeah, this is my 1st time, actually.
**Utkarsh Umesan Pillai** 02:56 Okay. Okay.
Usually
quite a few other people would join. But I'm not sure. Today looks like the other meeting is C. Joe lalit
young Yang. They aren't here and.
**nikhil bhatia** 03:14 Yeah, maybe.
**Utkarsh Umesan Pillai** 03:16 I'm not sure if they're gonna join this this one.
**nikhil bhatia** 03:19 Okay.
**Utkarsh Umesan Pillai** 03:21 Yeah, but you can
probably tell a little bit about yourself, and like what you're looking from the open telemetry dot rust sig.
**nikhil bhatia** 03:31 Yeah, sure. Actually, I'm an open source contributor. And I've done quite a lot of contributions in rust. Actually, I have open source contributed to Gitlab, where they had a gitlab query language compiler. So I had contributed in that. So I'm looking forward to contribute in actually rust and C plus plus both.
**Utkarsh Umesan Pillai** 03:53 Okay, okay, let's see?
**nikhil bhatia** 03:57 Actually er today, I was working on an issue in open telemetry, c plus plus SDK. So actually, I had a few questions. So.
**Utkarsh Umesan Pillai** 04:08 If I could.
Yeah. So that I think Lalit was
oh, the maintenance of one of the maintenance of the rust SDK is also maintainer of the C plus plus one. I think he would be the best person to answer questions related to the C plus plus SDK. But I can.
I mean, if it's a technical question, I probably wouldn't be able to help. If it's just like a generic thing. Maybe I can try.
**nikhil bhatia** 04:34 Actually actually, it should be also implemented in rust as well.
So.
**Utkarsh Umesan Pillai** 04:39 Okay.
**nikhil bhatia** 04:40 I was actually going through all the sdks today. So this resources detectors are there. Right.
**Utkarsh Umesan Pillai** 04:48 Yeah.
**nikhil bhatia** 04:49 In those. Actually, I was implementing for containers today. So I could. I was researching a little bit so we can get the container id like in the semantic conventions. There are like, we need to collect information about 4 resources like containers, hosts, processes, and services. So.
**Utkarsh Umesan Pillai** 05:13 I was working.
**nikhil bhatia** 05:13 The services. One sorry sorry the container one
so I was only able to collect the container id, but the remaining ones like. If we only use Docker inspect commands, then only we can get remaining other informations like, if you go into
this semantic conventions for containers, we'll find docker.image.id and docker.image.name. So using current file system of that docker container, we we cannot get the information. So we need Docker inspect command for that. So my doubt only was about that.
**Utkarsh Umesan Pillai** 05:55 Oh, as to like how you can retrieve that information.
**nikhil bhatia** 06:00 Yeah.
**Utkarsh Umesan Pillai** 06:03 Not sure if we already have a docker resource data detector in the last contract.
Have you checked that.
**nikhil bhatia** 06:13 Sorry.
**Utkarsh Umesan Pillai** 06:15 I say, I'm not sure if you already have a resource detector for Docker in the.
**nikhil bhatia** 06:19 Yeah.
actually, there was an issue in that so the Maintainer like he was, I think his name was mark. So he kept an issue that we need to implement these all things.
and I checked it in Rust. SDK as well. These were not implemented only that resources for services.
**Utkarsh Umesan Pillai** 06:40 Yeah, yeah. So the SDK wouldn't do it. This is not like, there are some core resources which will happen. So you're aware of the.
**nikhil bhatia** 06:50 Okay. Yeah.
**Utkarsh Umesan Pillai** 06:51 Of the content repo, and, like every language, will have its core repo, which is where the SDK and Api and Otmp exporter would reside. And then there's also a
a contract repo which is meant for people who try to add
or like build on top of open telemetry, like either instrumentation libraries or they have their own resource detectors that they wanna use.
or yeah, or their own exporters. They want to export to some other back end. It could be anything aws, azure or whatever just giving an example. Even anything is anything works but
the yeah. So this kind of thing, like the Docker resource detector. This won't be
in the main repo. You can chop, you can check rust contrib, or I don't know if c plus plus contrib repo has this, but
I know that in open telemetry.net there was something like
something like this in the.net. Contribut report. Let me hmm.
**nikhil bhatia** 07:59 I saw this even in go SDK in the main core. SDK thing.
**Utkarsh Umesan Pillai** 08:07 In the main project.
**nikhil bhatia** 08:09 In the main, I'll send you the link, actually.
actually seeing this go thing. Only I started to implement it, implement it in C, plus plus core thing.
**Utkarsh Umesan Pillai** 08:48 See?
Okay.
yeah, I'm not sure it doesn't
sound like the goal repo is the right place for this.
But
I do see the the container. go.co file that you sent.
Hmm.
I mean, yeah. I don't know why go. People decided to keep it in the code repo, but
hosting is not the primary issue here, like you can host the library in the the code for it, in the contribute profile.
**nikhil bhatia** 09:51 Okay.
**Utkarsh Umesan Pillai** 09:51 Yeah, and is, if you think go is able to do it, then
what kind of Apis are they using to retrieve that information?
**nikhil bhatia** 10:02 Actually go is also not go in. Go SDK, also they are only getting the container id, but not the remaining defined things actually
like he's so the.
**Utkarsh Umesan Pillai** 10:26 Sorry I don't hear you. Now. Are you saying something?
Hello Nikhil
Miguel! I can't hear you.
**nikhil bhatia** 11:13 Hello!
**Utkarsh Umesan Pillai** 11:14 I hear you now, I guess.
**nikhil bhatia** 11:17 Yeah, actually, there was a connectivity issue. So.
**Utkarsh Umesan Pillai** 11:21 Okay.
**nikhil bhatia** 11:22 In go SDK the file which I shared. Line number 26.
there is a file name called Process Self and C group.
So from that file we can retrieve the information of container id.
**Utkarsh Umesan Pillai** 11:40 Okay.
**nikhil bhatia** 11:42 So only he is doing only that, but not the other things which are defined in semantic convention.
**Utkarsh Umesan Pillai** 11:49 You have a link to that semantic conventions thing.
**nikhil bhatia** 11:52 Yeah, I have.
So this is the link for that semantic conventions.
**Utkarsh Umesan Pillai** 12:25 Check.
Oh,
So see, here's the thing. The status for this section is still in development. So that's probably one of the reasons why.
it's not being actively worked upon in the language implementations.
So you see the status section just below resource.
If you click on, develop and it will take you to a table which lists all the different statuses and what they mean
what they mean. So that is.
I mean, if it gets stable, then everyone is supposed to implement it
required to implement it rather. But yeah, for now, I think.
And other than that, let me see. For example, you just okay.
so what does it say about container? Additionally, the following detector names are reserved for built in resource. Vectors published with the language
container load attributes.
What do I?
Yeah. So I mean, see the even if you look at that container markdown file, right? I think a lot of this is
even this one is in development, status and.
**nikhil bhatia** 14:20 Yeah.
**Utkarsh Umesan Pillai** 14:21 And
let me see.
I think there used to be such a thing as recommended versus required, so all of them seem to be.
Let me see the requirement level. Yeah.
So technically, if they are
not, I mean, if they are required, then the Instrumentation Library, or whoever ends up providing those resource detector has to
provide those columns
or recommended. You can see what that means. But yeah, I think I would say, mostly it's a thing about the status, but you can still add, like I mean, if you find a way to do that, you can add it. I sent you the link of the.net resource detector.
I'm not sure if they have more stuff than container id for the for their
resource to get through.
**nikhil bhatia** 15:27 And also, I was like thinking, this is a like, this is taking so many lines of code. So actually so, it is divided into 4 parts, right container, host and service and process. So there is a main issue for this. So can I break down this into like 4 multiple pull requests. Like.
is it? Okay?
Of course, I actually sorry to say, but you might not know, because it is like c plus plus SDK. So.
**Utkarsh Umesan Pillai** 16:02 You're asking the Cs plus report right?
**nikhil bhatia** 16:05 Sorry.
**Utkarsh Umesan Pillai** 16:06 You're asking whether you can do that in the C plus plus report I divided into.
**nikhil bhatia** 16:09 Yeah, yeah.
**Utkarsh Umesan Pillai** 16:11 I mean the specification should apply to any language.
And, by the way, maybe I should share my screen, like I think, hey, yong, Yang, let's see, you've also joined.
**Zhongyang** 16:22 Hey? I'm not sure what we're talking about, but.
**Utkarsh Umesan Pillai** 16:25 Yeah, let me share.
So we have Nikhil on the call today. He's joined us for the 1st time. He.
**Zhongyang** 16:35 Welcome!
**Utkarsh Umesan Pillai** 16:36 He contributes to the C plus plus repo, or is looking to contribute to that, and I think
even lost
con contribute to even even the rest people. His question was around. By the way, do you guys see my screen.
**nikhil bhatia** 16:53 Yeah, I can see your screen.
**Utkarsh Umesan Pillai** 16:55 Like. Do you see the browser, or what do you see.
**nikhil bhatia** 16:57 Yeah, I see the browser.
**Utkarsh Umesan Pillai** 16:58 Okay, yeah. So this question is mainly around, like the resource detectors. So within the SDK repo, what I was at least aware of was.
We only need like the service name thing
because service name service version. These were stable, and the other
the other things. I was not really sure if we want to push that to the SDK right now.
But specifically, if you, there's a demand for it in c plus, plus, maybe I would say like
if Lalid was here, I think we could have just asked him what he thinks is the right thing to do here, but
probably ask the sequel specific itself
as to whether they want it to be added to the code repo, or if this is going to be
contract repo project.
But.
**nikhil bhatia** 17:58 Sure, sure.
**Utkarsh Umesan Pillai** 17:58 Yeah.
And then I mean, you can ask about the number of Prs, or like how you want to split it.
**nikhil bhatia** 18:07 Yeah.
**Utkarsh Umesan Pillai** 18:10 Cool.
**nikhil bhatia** 18:10 Actually, yesterday was our meeting, but due to time mismatch, I couldn't attend that special interest group of C plus.
**Utkarsh Umesan Pillai** 18:18 So you can always also just post your message on the slack channel. There'll be a hotel Cvp.
**nikhil bhatia** 18:25 Yeah, I'm I'm in that channel.
**Utkarsh Umesan Pillai** 18:30 Oh, you've already posted your question, Ajan.
**nikhil bhatia** 18:33 Not question like I was just giving my introduction yesterday, so.
**Utkarsh Umesan Pillai** 18:37 I see. Okay, okay.
okay, yeah. I mean, if you post your question, then I can also ask Lala to like.
Look for look up.
**nikhil bhatia** 18:48 Yeah, and.
**Utkarsh Umesan Pillai** 18:49 To join the channel and.
**nikhil bhatia** 18:50 That's my question today, surely.
**Utkarsh Umesan Pillai** 18:52 Yeah, yeah, I I can ask Lalib to look out for your question. There.
**nikhil bhatia** 18:56 Yeah.
**Utkarsh Umesan Pillai** 18:58 Yep.
**nikhil bhatia** 19:00 Thank you very much. Shipkash.
**Utkarsh Umesan Pillai** 19:03 Sure. Yeah.
**nikhil bhatia** 19:05 So I'll be leaving right now. So.
**Utkarsh Umesan Pillai** 19:08 Okay.
Cool.
**nikhil bhatia** 19:12 Bye. Thank you very much.
**Utkarsh Umesan Pillai** 19:13 Okay.
hey? Yong, yeah, soon. I don't see anyone else
joining today. I don't believe they will schedule or lalit or.
**Zhongyang** 19:59 Yeah, I'm kind of haven't been pulled closely, and that's on me. But is there anything
and walk stream that's actively going on?
I think we're pushing the I think we still block on the Tokyo thing because their response is being slow.
Other than that. I don't see anything, Major, going on.
**Utkarsh Umesan Pillai** 20:23 Yeah, yeah. Other than that. It's just some Pr select which people have been reviewing. Anyway.
**Zhongyang** 20:33 I think a few of them just need just needs named fakes and merge.
I'll do another pause. I think I did a pause. This weekend to check the one that's been that is okay to merge. But I'll take another pause. Just look at the one that hasn't been.
Have them ask the link, and see if anything we can do. Just
pair the name to check and merge it. No, because there are some of them. Just it's just snacking. I say, I don't think we can do anything about that. So.
**Utkarsh Umesan Pillai** 21:09 Yeah.
Yep.
**Zhongyang** 21:12 Okay, that's all we got, as we can reconvene next week.
**Utkarsh Umesan Pillai** 21:17 Yeah, sounds good.
**Zhongyang** 21:20 If it's like.
I'm thinking we should move the meeting by a 2 have tough one meeting every 2 weeks, so people can gather at the same time.
**Utkarsh Umesan Pillai** 21:33 Yeah, you're saying, like, once in 2 weeks.
**Zhongyang** 21:37 Yeah, cause I see, like I wasn't able to attend last week. But see, he was in.
see you and the scholar was here last week, but we weren't here last week, so.
**Utkarsh Umesan Pillai** 21:49 Yeah.
yeah, maybe. Sure. I think I'm open to that idea. It's just something to check that. Like, does the
community guidelines allow for it, like, maybe I don't know if there are people outside
or like people who just wanna looking to contribute or ask questions.
Maybe it's easier for them to like have a weekly thing, but something to check with the hotel community guidelines. I guess.
**Zhongyang** 22:19 Yeah, that's a good point. People will be able to to basically, oh.
basically, it's like office hour, like, say.
**Utkarsh Umesan Pillai** 22:30 Yeah, yeah, I mean, yeah, anything goes basically in that 1 h slot, either when the project is in
development phase. Then there's enough stuff to talk about like the milestones and everything. And once it goes into like the maintenance mode, then yeah, then it becomes kind of like office hours.
**Zhongyang** 22:52 Yeah.
**Utkarsh Umesan Pillai** 22:53 Yeah.
**Zhongyang** 22:54 Good point, all right.
If there's nothing else to talk about unless we're gonna call you today.
**Utkarsh Umesan Pillai** 23:01 Yeah, sounds good. Thank you.
**Zhongyang** 23:03 Thank you.
Hi!

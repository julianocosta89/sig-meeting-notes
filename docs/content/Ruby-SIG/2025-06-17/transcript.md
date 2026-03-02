SIG: Ruby SIG
Date: 2025-06-17
Duration: 22 minutes
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 00:07 Good morning, Hannah.
**Hannah Ramadan** 00:10 Hi, Kayla! Good morning! How are you?
**Kayla Reopelle** 00:13 I'm doing well. How are you?
**Hannah Ramadan** 00:14 I'm good.
**Kayla Reopelle** 00:40 The oh, hey, Shawn!
**Xuan Cao** 00:47 Bye.
**Kayla Reopelle** 01:02 Okay, let's go ahead and get started.
Oops.
Alright. So
I did not make it to the spec sig this morning. But let's see what they talked about.
So there were a few things that got stabilized with logs.
Okay, the event name parameter was stabilized for longer. Dot enabled.
and
the No. OP. Logger dot enabled was also stabilized.
**Hannah Ramadan** 02:03 Kind of random. But do you happen to know what it takes for something to become stabilized like other
check boxes? Or it seems like kind of a vague just like, Oh, it's table now.
**Kayla Reopelle** 02:16 Yeah, there is a let's see. So my understanding of what the process is is that
you need to have, I believe, at least 2 prototypes of the feature in different languages that you know can or cannot be deployed. And then you need to have the spec.
Pr with the text receive approval, and after that point,
I think that things can can go stable but
I feel like it would probably still be a good idea to figure out where exactly that is posted, and I can do that and and share that with you.
Later on. But yeah, my understanding is 2 prototypes, and then Pr approvals.
**Hannah Ramadan** 03:09 Okay, nice. Yeah. I can also dig for that. That's somewhere. That's interesting.
**Kayla Reopelle** 03:14 No, it might be in the community repository. The open telemetry community repository.
**Hannah Ramadan** 03:20 Okay.
Oh.
**Kayla Reopelle** 03:37 Okay, yeah, it's not popping up
anywhere immediately. So yeah, that that's that's what I have heard. And I don't know, though, what it takes to get kind of that initial
Pr merged. That would, you know, allow you to see a feature in development, because I think that that also needs to get approved. But I don't know if it requires a prototype before it can.
It can get merged.
Because, like, if you look at both of these. Prs, it's just changing kind of, you know, something that's like
from development to, you know, stable. So this.
**Hannah Ramadan** 04:16 3, 3.
**Kayla Reopelle** 04:17 Change itself has already been in that text for a while.
Let's see, Browser Sig. Phase one is approved. 1st meeting will be this Thursday at 8 30. Pacific.
To Pr to define hotel maturity levels.
Which is that so?
No explicit status development stable deprecated. Those were the old ones. Oh, nice. Okay. So now there is development.
Alpha beta, release candidate, stable, deprecated, unmaintained.
That is super helpful. So at some point we should update our documentation to make the State the status of
to make the status of metrics and logs more clear.
I guess. Was it merged? Oh, it's still just open. So maybe that's
little too ambitious. So maybe we shouldn't update quite yet. But
right? What else we got here?
Okay, kind of continuing on that severity number. Pr, that I brought up a little bit ago about like, what's a valid severity number value.
and having attributes support complex values is still under discussion. It looks like this is still the same. Pr.
Oh, that might be how it works! Hannah! The the Oteps are like proposals.
4 features
**Hannah Ramadan** 06:35 That then would get merged into the specification.
Okay.
**Kayla Reopelle** 06:42 I believe it looks like, though this is still under Otep, so maybe I'm not quite on there. But I know yeah. Oteps are are some sort of proposal.
And this is a thing I don't know if either of you need to worry about it. But just so you're aware. Cncf slacks. Workspace is changing this Friday. It was kind of like a last minute surprise for everyone. That
we are getting moved onto the free plan for slack, so that will only retain 90 days of message history, and some like apps and workflows will have to be disabled. I don't think that we have any special apps or workflows for the Ruby
Hotel Ruby Slack, Workspace. But there has been some discussion about, like maybe moving on to discord or some other platform. So
there's yeah. There's a few things.
that yeah, maintainers will need to think about. So I have this on my list to take care of
this week in terms of saving files and PIN posts, but if you have any
private channels that you want to save, or Dms that you want to save.
There are ways to back those things up that it looks like they have not
linked here. But if anyone's interested in that I can dig up the other link that was posted, I believe, in the Maintainers Slack Channel, which is open to anyone, so you could also find it there.
And what's this last one central release?
Kyle,
looks like, okay, looks like this is just kind of your standard release policies.
Seems like Ruby is mostly right, but we'll
might need. I'm gonna drop a note for myself to verify that stuff
alright cool anything else on that spec. Say that people want to take a closer look at.
**Hannah Ramadan** 09:20 Yeah, not for me. Actually does. Otap is like, is that open telemetry proposal? Just the acronym.
**Kayla Reopelle** 09:27 Let's see. Oh.
**Hannah Ramadan** 09:29 I definitely see it around, but I tend to ignore it. But.
**Kayla Reopelle** 09:34 Open telemetry, enhancement, proposals.
**Hannah Ramadan** 09:38 Cool. Okay.
**Kayla Reopelle** 09:40 And so this repo was merged into the spec repository. So you can see the proposals in this directory.
**Hannah Ramadan** 09:48 Nice. Okay.
**Kayla Reopelle** 09:50 Yeah, which? Yeah, there might be some good information here about how things get merged in as well.
Sweet. Okay, So
starting with core. Yeah, I I reviewed this. I feel comfortable with it. Thanks for opening the extra issue. Sean. Is there anything else that you wanted to do with it before I merge it? Or are you ready for me to merge it in.
**Xuan Cao** 10:24 No, I don't.
I don't think there's anything to do.
**Kayla Reopelle** 10:31 Cool.
Sounds good.
Alright? I will.
I guess. Yeah, that should be fine to release, because it's just more like we have some extra code right now in the SDK
that needs to be removed for the
or I guess it is there any cleanup that needs to be done. Still, related to the instrument
that was around for an exponential histogram? Or was that all? Just in the last pr that got closed.
**Xuan Cao** 11:11 I think this has just include everything.
**Kayla Reopelle** 11:14 Okay, sweet, thank you.
So I'm get released ready.
Anything else in core that people want to talk about today.
This, this Pr is going stale on purpose. They weren't aware that views were available, and I've pointed them in that direction. So I think we're just gonna let this disappear.
I know you're not an approver on this repo, Sean, but if you have time to take a look
at this, this is really just fixing a typo that I found where the
name of the file was different than the name of the class.
And so this this kind of fixes that discrepancy.
And I'll I'll try to pass it over to Matt. As well. Let me do that on here, so I don't forget
Alright!
Don't think there is anything else on here. So next what is the next most important pr in here for you, Shuang, for me to review. Do you think exemplars, or Async.
or something.
**Xuan Cao** 12:50 Oh, oh, I think the I think will be more
more interesting. But I think I need to the merge and the without any conflicts. Yeah.
**Kayla Reopelle** 13:07 Cool. I will let you do that, and then, when it's ready, just let me know, and
then I'll take another look.
**Xuan Cao** 13:18 Okay. Thanks.
**Kayla Reopelle** 13:24 Alright. And then over here we've got some opt-in files. Thank you for your patience, Hannah.
Nice forgotten approval from Eric, too. So I'm gonna go ahead and update this branch. I think some things will fail because we currently have
some failures with Kafka. But I'm hoping that it will all be okay, anyway, I believe auto merge is working now where it'll wait for the Ci to pass.
So let's let's just hope that is true, and if not, then I will have learned my lesson. Okay, cool.
That seems good so far.
Yeah. Fantastic. Okay, awesome.
And then
and Hannah, I guess you want these changes?
released like as soon as possible. Or did you want to wait until more?
More of the gems were ready.
**Hannah Ramadan** 14:46 I would like to see how far I can get with some of the other gems. If
if all goes well, I I feel like I might be able to get a lot of them done this week, if not all of them. So I think it might be worth it just to have it all in one. Go.
**Kayla Reopelle** 15:03 Okay? Yeah. Since we've already passed, I believe, like the kind of standard
time for an auto release.
we could. We would probably wait until next week.
There's a fix or something immediate that needs to go out.
**Hannah Ramadan** 15:20 Yeah, although I am having a memory of like talking, maybe I think it was probably to you at 1 point about like maybe
oh, miss out, just in case like someone reports something. So we're not so. Maybe it is better to do that sooner than later, as they test, as if you will
**Kayla Reopelle** 15:39 And.
**Hannah Ramadan** 15:40 Before making changes to all of the libraries. That's probably the better call.
**Kayla Reopelle** 15:51 Awesome. Sounds good. Thank you.
**Hannah Ramadan** 15:54 No, thank you. Yeah, perfect.
**Kayla Reopelle** 15:56 And then this guy, what was this 1? 0, the 0 code instrumentation. Thank you for making those text updates. I wanted to check in and see if there were any
any of these conversations that you think are still open and need to be addressed like it looks like this one has been fixed and is outdated.
So I'll mark this one as resolved.
where do you think you're at with this conversation? Is there more that needs to be decided with Ariel.
**Xuan Cao** 16:32 No
**Kayla Reopelle** 16:33 Okay.
**Xuan Cao** 16:34 Come!
**Kayla Reopelle** 16:36 Cool. Alright, then I will resolve this one as well.
Okay, how about this one?
**Xuan Cao** 16:48 there is a. They have a auto updates, but I'm not sure that not 100% certain what works for ruby?
but I can spend some time to look at.
Oh, there's this this M. File.
**Kayla Reopelle** 17:06 Okay.
Alright. I'll leave that one then. And that makes sense
and thank you for fixing that
and it looks like that one also got fixed, since it's outdated.
And you took care of this one, too.
Okay, have. We have a feeling that this Mongo is related to something else that's going on are. Now that you've made some changes related to naming and things.
Is there? Is there anything else in your mind? That needs to be fixed
before we merge like, did you want to take care of some of that version updating research first, st
or do you.
**Xuan Cao** 18:04 no, because that version updating is is only on their side. So basically, I think how their our language other language work is so that they
they look into the the ripple, the file for each different language, and then they
then they decide if they need to update. So
is. It's not related to this. Pr.
**Kayla Reopelle** 18:28 Okay, sounds good. Then I am comfortable approving this.
would you check in with Ariel to see if he is comfortable with this, since he's also reviewed it.
**Xuan Cao** 18:44 Yeah. Yeah. Oh, awesome.
**Kayla Reopelle** 18:45 Okay, thank you.
Sweet. And then hopefully, we can get that merged and test it out.
**Xuan Cao** 18:54 Yeah, is it? Just one thing, I think, is related to this 0 code.
So there's a person that he reached me out. He I'm not sure if you guys know this repo called Open Time Machine Injector.
**Kayla Reopelle** 19:10 Hmm!
No.
**Xuan Cao** 19:13 I think this guy opened the Pr, that is something related to the 0 core.
And then he, he basically just copied everything from oh, on the vehicle. And then.
**Kayla Reopelle** 19:33 Okay.
**Xuan Cao** 19:36 I think. From from his point, I think he think he's okay. So think it's another like assurance that's gonna work. But anyway, anyway.
to check about.
**Kayla Reopelle** 19:51 Interesting. Okay, so does he have a gym. Spec is this, I guess this isn't released from a gym.
**Xuan Cao** 20:00 Yeah, I'm not sure I haven't looked into very deep, very deep.
I don't know how your installers also, I guess he just so he he! He does have the ultra instrumentation. Rv, file that
do other work.
So so, Kerry, he doesn't need to like our like open to do everything. Just he just needs a file.
**Kayla Reopelle** 20:27 Okay, okay, interesting.
Cool.
And is he asking for reviews, then, on this, like from from you or.
**Xuan Cao** 20:46 Oh, he, he asked me, how do I test the 0 our 0 code? I I say, I just I just told him that I tested from
like pure rails app without any modification, because just to test out if
it can work. If automated solution. It can work out on the fresh rails, app.
**Kayla Reopelle** 21:08 Okay.
interesting.
right? Well, that was everything I had on the agenda is there anything else that folks want to talk about today.
**Hannah Ramadan** 21:50 I didn't have anything.
**Kayla Reopelle** 21:51 Okay?
And let's see, I guess popping into contrib one there anything else?
Yeah. So if if anyone is interested in interacting with the Kafka Ci.
Seems like there's some issues here.
Eric Mustin chimed in on slack, and said that he would also take a look at it. But if anyone else has experienced this, and you might have an idea of what's going on. Feel free to chime in on this issue.
Alright. Well, cool, then.
If that is it, then I think we can wrap things up here and see everybody next week.
**Hannah Ramadan** 22:52 Perfect, amazing, thank you.
**Kayla Reopelle** 22:54 Cool thing.
**Xuan Cao** 22:55 Thank you. Bye.
**Kayla Reopelle** 22:56 Bye.

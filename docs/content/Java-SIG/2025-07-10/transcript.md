SIG: Java SIG
Date: 2025-07-10
Duration: 46 minutes
Zoom Recording URL: https://zoom.us/rec/share/TaPzl4oyUU-CBu05M7byeHwgNnoLh_YeV8t2-oVmGVoGAqW1KxUZRA-zA4bSbWCp.3OF99qHiLnT09E2d
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 03:46 Hey, Steve, hey, Hosheen.
**Huxing Zhang** 03:50 Hello, Tusk, how are you doing?
Yeah. Fine.
**Steve Rao** 04:18 Yeah, maybe before the agenda. Yeah, I have a suggestion.
How about setting a a alert on Hotel Java? Seek group on slack to alert someone if they are interesting in a no matter in a pack back link a meeting or general meeting. They can join. Yeah, the meeting in the future.
**Trask Stalnaker** 04:53 Yeah. Have you seen other slack channels? Set that up.
**Steve Rao** 05:00 I thought, J. And I, yeah, there is a 3.rd
**Trask Stalnaker** 05:04 Can I? Okay.
**Steve Rao** 05:05 Alert. Yeah, to alert contributor. If they are interesting this week, they can. Yeah, maybe join the meeting by related Zoom Link.
Something like that.
**Trask Stalnaker** 05:24 Yeah, let me look at what they've done.
**Steve Rao** 05:30 Yeah. Maybe you can check Hotel Jane Jane AI to instrumentation.
**Trask Stalnaker** 05:38 Yeah.
**Steve Rao** 05:39 Yeah.
**Trask Stalnaker** 05:39 I'm looking at that. I see they have one an alert to
if they want to discuss something to add to the agenda.
Let's see.
**Steve Rao** 05:53 Yeah, I I send it to the alert. Yeah.
On meeting chat.
**Trask Stalnaker** 06:05 Please like this message, if you want to discuss.
Okay, yeah, yeah. I can do that.
**Steve Rao** 06:17 Okay, yeah, maybe yeah.
**Trask Stalnaker** 06:20 Same, the same message, basically.
**Steve Rao** 06:24 Hmm, yeah.
**Trask Stalnaker** 06:30 Let's
so we want slack remind.
**Steve Rao** 07:23 Okay, yeah. You also use copied.
**Trask Stalnaker** 07:27 Of course. Remind message we want
and occurrence every make.
No, they do. They do 11 pm. The day before.
Or okay, so basically same time. So we would do when is this actually scheduled for?
Oh, do we even have this? We do great, sure.
**Steve Rao** 08:37 Yeah, I will, either. Yeah, maybe we can. Alert a hand of one day.
**Trask Stalnaker** 08:44 Wednesday.
**Steve Rao** 08:46 Yeah.
**Trask Stalnaker** 08:50 Okay.
Slack.
Okay.
**Steve Rao** 09:02 Yeah, maybe we yeah, we
we don't need to add, yeah to we.
yeah, maybe we we can replace the yeah, the meeting is canceled to the zoom link. Yeah, maybe. Yeah. It's it's more convenient for contributor to join the meeting. Maybe.
**Trask Stalnaker** 09:40 Right?
Yeah, I'm just checking here. Remind, what is okay?
What channel?
I used to test it.
Remind me. That's the keyword. Remind me just testing it
before I do it in the Java Channel.
it doesn't like the Utc. Okay, so that's 1 thing.
Emily. And okay.
next occurrence is July
16.th Okay?
So the only thing is how
how to and add Utc time zone to make a reminder
temporarily.
Okay.
**Steve Rao** 12:00 Okay.
**Trask Stalnaker** 12:01 Okay, no, that's doable.
Okay, cool. I think I got that. Let me copy over
cause I think I need to do it.
I need to do it next week, because right now, when I did it at the next scheduled, it was off cycle of every Other week was gonna start next week.
**Steve Rao** 12:39 Okay.
Yeah, maybe for a pack or for general, yeah, they are. Yeah, both are good, maybe, I guess.
And.
**Trask Stalnaker** 13:01 Well, we pretty much. We always have.
**Steve Rao** 13:05 Yeah, maybe we can replace. Yeah, if nobody like, it's a call. It's a council. We can replace the text with a zoom link.
Yeah, if someone not familiar with how to join the meeting. Yeah, maybe.
Yeah, something like that.
Yeah.
**Trask Stalnaker** 14:07 So do you want? I mean to please like this message
like cause it seems a little different. The Jim AI. Folks, it seems like. Sometimes they don't have it, and sometimes they do so. It seems like you want something a little bit different.
**Steve Rao** 14:27 Yeah, yeah, maybe we can. Yeah, adjuster to text, according to our situation.
**Trask Stalnaker** 14:39 Yeah, do you want to? Just since you have something in mind? Do you want to just edit this and
next week?
**Steve Rao** 14:52 Yeah, maybe it's yeah, maybe it will. Alert.
Yeah. And that's time. Yeah.
**Huxing Zhang** 15:01 I think we we just want to remind someone, if he has interested to join this meeting
like 30 min before the meeting, let just send a message to let them know that we have a meeting here, and then you can join.
**Trask Stalnaker** 15:20 Thursday, 8, 30,
yeah.
**Steve Rao** 15:27 Let's see.
Yeah, it's okay.
**Huxing Zhang** 15:30 8 30. I think it's a 9 9 Am.
**Trask Stalnaker** 15:34 Oh, yes, yes, the reminder will be at 8 30, reminder.
Apac Javasig Apac meeting, starting in 30 min.
**Huxing Zhang** 15:50 Right.
**Trask Stalnaker** 15:52 Zoom link, and we could add meeting agenda
under Java. Sig a pack, Java sig
cool?
So actually, I don't trust to run this after next.
Wednesday.
So the alternating
or to do in case I
oh, I know I'll set a reminder. I should really use this more.
Remind me sad Apac. Reminder what I want to do.
And Thursday.
July 17.th
**Steve Rao** 17:56 Hmm, yeah, maybe.
**Trask Stalnaker** 18:00 Slack bot approved of that.
All right.
cool, alright. Enable disable instrumentation dynamically.
**Steve Rao** 18:15 Yeah.
**Trask Stalnaker** 18:16 Yes, the so let's see, Jack Shirazi.
So the elastic folks are working on this.
**Steve Rao** 18:32 Yeah.
**Trask Stalnaker** 18:34 And they have implemented
they've implemented some stuff to be able to do this
via a distro right? But we definitely want to support this? The. So the problem is, what is the back channel? Right? What is the dynamic? How do you tell it to dynamically update the config.
**Steve Rao** 19:16 Hmm.
**Trask Stalnaker** 19:19 Sue, right? There's a couple of options.
Now, are you wanting? So there's 1 option, which is, we could pull like the config file.
**Steve Rao** 19:33 Yeah.
**Trask Stalnaker** 19:34 And if somebody updates the config file, then we could respond to that
but more likely people are gonna want to have Central be able to do that from their centralized console.
monitoring tool.
**Steve Rao** 19:52 Yeah.
**Trask Stalnaker** 19:53 And so for that, what we will support eventually in the in vanilla is OP. Amp, which will
so there's various pieces of this coming together.
If you've seen the work happening over here.
This will allow us to. It's kind of a communication channel from the control plane down to the Java agent to
make those kinds of changes. The OP. Amp protocol itself doesn't really say what
the how to all it says is. Here's the you can send data down.
but it doesn't say what that format should be.
So what we are, what we've discussed in the Sig
has been to use declarative config
to send the Yaml declarative config basically, as the content.
**Steve Rao** 21:11 Hmm.
**Trask Stalnaker** 21:12 But a lot of that is sort of to be worked out. Still, that's just like
long term direction.
**Steve Rao** 21:24 Okay?
Yeah. You mean, it's a up Amp implementation. Yeah, it's a a default.
support. For when in a Java agent.
**Trask Stalnaker** 21:38 Right?
Yeah, that will be the vanilla Java agent for
distros. They may already they may have a different back channel.
Like elastic, has an existing back channel. They so they are gonna support that
maybe someday in the future OP. Amp will be widely spread
and they'll support OP. Amp, also.
But same for you. If you have, for example, an existing back channel, you could in your distro you could do the same thing. They're doing
instead of using OP. Amp, so that's
one of the problems. The other problem is just allowing
more stuff to be dynamic in the Java agent.
**Steve Rao** 22:33 Yeah, yeah, recently, yeah, we also in encounter this issue. Yeah, because we want to. Yeah, as you know, we migrate from our old version to destroy.
And yeah, we do some experiments based on extension. And we can yeah, modify something. Yeah, on spend now, and we need to support disable in or enable
specific instrumentation.
Yeah, yeah, maybe we have some requirements with elastic elastic fog. And we also? Yeah, I have
brief? Yeah. Look on the approach of elastica.
Yeah, yeah, I, yeah, my, I just want to know, yeah, is there any plan to support it in running a Java agent? Yeah. And
yeah, something like that.
**Trask Stalnaker** 23:48 Yeah, so sooner. What we can do in vanilla
sooner. That will be good is
adding support to the SDK to update things dynamically.
**Steve Rao** 24:11 Yeah, yeah.
**Trask Stalnaker** 24:11 Yeah. Man.
**Steve Rao** 24:14 Yeah, I spoke.
**Trask Stalnaker** 24:15 Don't.
Yeah, we don't need to have OP. Amp for that.
**Steve Rao** 24:23 Okay.
**Trask Stalnaker** 24:25 And so I think this here.
**Steve Rao** 24:30 Yeah, yeah.
**Trask Stalnaker** 24:30 And this mutable.
**Steve Rao** 24:32 Yeah, yeah, this is a pr.
**Trask Stalnaker** 24:34 Yeah, so this is how they are doing it right now, I believe
that. Or maybe this. Let's see discussion here.
Yes. So they removed the original implementation and added this on.
**Steve Rao** 25:03 Yeah. But I thought the code of elastic destroy
still use reflection to update the state status.
**Trask Stalnaker** 25:19 Okay.
they may not have updated. Or I mean, this is still has to be called by reflection because it's package protected.
**Steve Rao** 25:27 Hmm.
**Trask Stalnaker** 25:31 But if they're still I'm doing.
I mean they, you know. I'm not sure. Yeah, but it it's
let's see. Tracer enabled.
Yeah, Sue.
I mean that. Oh, yes, yes, so you can use. Here's the publicly accessible but internal.
So this is kind of ideal.
**Steve Rao** 26:16 Okay.
**Trask Stalnaker** 26:17 Think.
Let's see what is what's going on here. It's set tracer configure. Yeah.
basically, look at this. Pr, this is this is giving you sort of public
access to do that via an internal package, for now.
**Steve Rao** 26:43 Okay, yeah, maybe we need to do similar things with elastic fog. No. And
yeah, maybe. Yeah. In the future. If Manila Java agent support. Yeah, similar feature. And we can migrate the logic to use the support from Manila, Java agent.
**Trask Stalnaker** 27:12 Yeah, yeah, I think we would. Probably it would be nice. Yeah.
be interesting to see. I can ask Jack tomorrow if
cause would you? I mean, what would you do
in the meantime, if you had a yaml? The question is, can we update?
Is there a higher level way to pass in. Yeah, to update this dynamically.
I don't know if we've even let's look at that configuration repo.
I don't even know if they have that in the
if we have that in the declarative config, yet.
**Steve Rao** 28:19 Hmm.
**Trask Stalnaker** 28:20 So we've got tracer provider tracers.
Oh, okay, okay, so it's it's still in development.
But there is.
You can configure different tracers to be enabled or disabled.
**Steve Rao** 28:46 Okay.
**Trask Stalnaker** 28:47 So what would be interesting? Would be potentially to be able to pass in a new yaml.
**Steve Rao** 29:04 Hmm.
**Trask Stalnaker** 29:04 And through these and update the tracers dynamically.
**Steve Rao** 29:13 You mean to update config configuration. Yaml.
**Trask Stalnaker** 29:25 The do you?
You know, Yaml, opt out, Yaml, apply the Yaml right now. You, if you
propose something to the Java SDK.
**Steve Rao** 29:41 Hmm.
**Trask Stalnaker** 29:43 To take in a yaml dynamic at Runtime.
**Steve Rao** 29:49 Hmm.
**Trask Stalnaker** 29:50 And update at least loop through the tracers and update these things dynamically.
**Steve Rao** 29:59 Yeah, okay, yeah, yeah, it makes sense. I also of a.
yeah, think about this this method. Yeah, because it can control control a lot of things. Yeah, if that.
**Trask Stalnaker** 30:14 Yeah.
**Steve Rao** 30:15 Configuration is supported. We can control everything. Yeah, it can make the configuration update easily.
But
yeah. But maybe that is a problem. Yeah, if users ever, we don't have the permission to create a Yama Yama config configuration. Yaml.
yeah, maybe we can update.
**Trask Stalnaker** 30:51 If you do, you mean if you don't have permission to write a file to a file.
**Steve Rao** 30:56 Yeah.
**Trask Stalnaker** 30:57 That's okay. I mean, it doesn't need to be. It can be just in memory. Yaml.
**Steve Rao** 31:04 Tech.
**Trask Stalnaker** 31:05 Next.
**Steve Rao** 31:06 Okay.
**Trask Stalnaker** 31:07 Is better anyways.
Cause. That's what's gonna happen for the eventually for OP. Amp.
**Steve Rao** 31:18 Is, the Yaml will come down, and we'll want to feed that.
**Trask Stalnaker** 31:22 Into the SDK.
**Steve Rao** 31:26 Okay.
Yeah.
**Trask Stalnaker** 31:29 And you know the initial. Initially.
we would only support dynamically updating, you know, a couple of things.
but maybe over time, we can add support more and more things.
**Steve Rao** 31:46 Okay, okay, makes sense.
Yeah, okay, I, I can also, yeah, investigate this map. This approach of the meeting.
**Trask Stalnaker** 31:59 Yeah. And if you want to
open, I can ask. Let's see. Let me add, I'll I'll ask Jack tomorrow.
Just kind of briefly.
For his idea.
Api, for I see in your yaml
we're thinking tracers
cool.
**Steve Rao** 33:12 Okay, yeah, thank you.
**Trask Stalnaker** 33:14 Yeah.
Pushing.
**Huxing Zhang** 33:45 Yeah.
**Trask Stalnaker** 33:45 To know more about.
**Huxing Zhang** 33:46 Just came across this issue in meeting notes.
I just I wonder. I that's what we are looking for recently, actually in the background.
**Trask Stalnaker** 33:58 Oh!
**Huxing Zhang** 33:58 Is.
Actually, we will. We want to like, inject the
trace id into the HTML file
so that in the front in the front in the web. Web. Ui! We can have that trace, and we we will correlate this with some
web like like no Javascript logic there and then they will do something that, and they can correlate to this. Trace Id with our back
backend request.
So I I believe this is something we are looking for. I just want to know about this feature, and if you can share something more that will be
very helpful for us.
**Trask Stalnaker** 34:48 Yeah, so we actually this was developed, written by an intern that we had in our team.
**Huxing Zhang** 34:58 Oh!
**Trask Stalnaker** 34:58 A few summers a couple of summers ago.
So I I do know this feature fairly well.
So basically, you can give it
the snippet that you want to inject? The Javascript snippet?
Since we don't. At some point we'll have. We'll have a standard open telemetry
browser, Api, and so we can have a default, at least a default. Javascript snippet that
puts the open telemetry browser SDK in but for now
we don't have such a thing, so you have to have your own and.
**Huxing Zhang** 35:48 So it's configurable, right? So.
**Trask Stalnaker** 35:56 let's look
so and it's in the bootstrap here, we tested oh, you can see it's i don't know, if we have. I don't know how many, if we have many customers using it.
But we actually did implement add it to our distro. So you can see what we are doing.
So we snippet.
Yeah. So we have our snippet here.
so we just replace it with our connection string here with the users connection string, and then in this gets injected.
**Huxing Zhang** 36:59 Okay.
**Trask Stalnaker** 37:06 it. Let's oh, go ahead.
It's worth looking at. Let me see if we have tracking issue snippet. Okay?
So I forget where we added,
tests to like the tomcat and servlet instrumentations.
Serverlet. Okay. Here, Servlet, it's like Servlet, all
Jackson.
So from what I can tell you from some experience with injecting snippets is
hard to. There's a lot of edge cases that can end up breaking people's pages.
And so the more tests that we add the better.
**Huxing Zhang** 38:55 Okay.
Another concern that comes when you are going to like, intercept the response body, and you will pass that body and inject the
script. That will be some pro performance concerns for me.
So how? How? How do you think about that?
**Trask Stalnaker** 39:19 Yeah, so we, I think there's a couple of optimizations. If I remember, one is
we can look at the content type
header, and only apply that logic for text. HTML,
like we don't have to. So we don't have to create overhead on rest responses and other other things.
On
HTML, once we know it's HTML. Then we only need to parse up until, like the head tag. I think.
**Huxing Zhang** 40:08 Okay.
**Trask Stalnaker** 40:09 So we don't need to pay attention to to the whole body. We'll have to inspect the whole body.
But it's some. I mean it's a definitely something to
I don't think we re. I don't think we benchmarked it.
I think at Jfr.
Benchmark, I mean, I'm not. Gmh. Benchmark, you know, could help.
**Huxing Zhang** 40:46 Hmm.
I saw. This is kind of experimental feature in the
has all the Microsoft implementation been negative, contribute to the upstream or.
**Trask Stalnaker** 41:09 Yeah, no, we don't have anything
in our distro. That's not upstream.
Okay, but that said, I don't know.
I don't think we have a lot of people using it.
And so we we have not marked it as ga in our distro.
**Huxing Zhang** 41:39 You know.
Okay.
**Trask Stalnaker** 41:42 Mainly just because I I didn't feel like it had gotten enough usage.
**Huxing Zhang** 41:47 Yes,
**Trask Stalnaker** 41:48 So if you are.
can help with that also. That would be, I think, help that feature to move forward in the upstream.
**Huxing Zhang** 42:00 Yeah, we, we recently have some
user customer that may require they may have may need to have this feature. So we'll definitely have some feedback.
and I will do some investigation about this feature. Yeah.
cool. It's a cool feature, for sure.
**Trask Stalnaker** 42:22 Yeah.
**Huxing Zhang** 42:24 Thank you.
**Trask Stalnaker** 42:25 Yeah.
**Huxing Zhang** 42:26 So this feature is in the 2 2 dot 0 version of travel agent. Right.
**Trask Stalnaker** 42:33 Yeah, I think it's even. I think it's in one.
**Huxing Zhang** 42:36 One, okay.
**Trask Stalnaker** 42:38 One also.
**Huxing Zhang** 42:39 Okay, I'll check it out.
Oh, okay.
The next one is, we were going to have an event virtual event with.
**Trask Stalnaker** 42:51 Oh, nice!
**Huxing Zhang** 42:52 Dan.
and to to talk about the Alibaba's hotel journey, and it's it's maybe next week, next Wednesday. I think it's
and then we will talk about how we use the Dan want some use cases from Apac
about the auto adoption. So we have this going to have this discussion, this session. Yeah.
just the one to let you know about that.
**Trask Stalnaker** 43:25 Yeah, I'll I'll watch the I'll watch the recording after.
**Huxing Zhang** 43:32 Okay.
**Trask Stalnaker** 43:33 Since it's at one Am. My time.
**Huxing Zhang** 43:36 Yeah, it's Steve and me, yeah, we we are going to talk about that.
**Trask Stalnaker** 43:43 Nice, awesome
anything else you all wanna chat about today.
**Minghui Zhang** 43:57 Sorry I have a I have a little question I just want to ask, when do do you plan to migrate the messaging wrappers to Java instrumentation, or just merge it into the Java contribut repository first, st and have a further discussion.
**Trask Stalnaker** 44:25 Is there? Can I forget where we left off? But is that something? Can you send the
Pr to Java instrumentation?
Were you waiting for me to confirm with Lori.
Sorry I forget where we left off.
**Minghui Zhang** 44:45 Yeah, I I mean, I maybe I needed your confirmed first, st and I can send a pr, because if I just migrate migrate this Pr. To the instrumentation, and it seems not so. Meter. If you don't want to merge it into the instrumentation.
**Trask Stalnaker** 45:12 Oh, if it's not mature!
**Minghui Zhang** 45:16 Yeah, if you you if other members doesn't want to have the Pr in it.
**Trask Stalnaker** 45:27 Yeah.
Yeah. I just added it to tomorrow's Sig agenda.
And I will ask Lori, basically.
we'll chat about it, for I'll chat with him for a couple of minutes, and tomorrow's meeting.
Yes.
**Minghui Zhang** 45:47 Thank you.
**Trask Stalnaker** 45:47 Just to confirm that he is good with it also.
Yep. Sorry about that. I
**Minghui Zhang** 45:55 Never mind, thank you.
**Trask Stalnaker** 45:57 You know.
Cool, then have a good Thursday.
**Huxing Zhang** 46:12 Hey? Good bye-bye. Thank you.
**Steve Rao** 46:14 Have a good day.
Bye-bye.

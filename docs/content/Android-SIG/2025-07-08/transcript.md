SIG: Android SIG
Date: 2025-07-08
Duration: 24 minutes
Zoom Recording URL: https://zoom.us/rec/share/-UQ0yDvCtuokAW2KM8q_xvWY1WdD6i6DqUTbsr92RPmfLjestUkvP6Nt4KRdU5ql.cOtGWsja6ZD-BkSi
============================================================

## Zoom Recording Transcript

**Jason Plumb** 00:48 Good morning.
I'm using morning as the generic umbrella term for everywhere. Sorry.
**Cesar Munoz** 01:07 Hello!
**Jason Plumb** 01:09 Good morning! Good morning!
**Hanson Ho** 01:16 Hello, fellow! Black T-shirt wearers!
**Jason Plumb** 01:20 Hello! Mine's technically brown, awesome. So brown. It's wild.
**Hanson Ho** 01:26 I know want to be different sometimes. Yes, stick, stand out.
**Jason Plumb** 01:30 Gotta keep handsome guessing.
And okay, so for new people. Welcome, happy. You're here glad to join us. We have an agenda that is linked from the meeting
information the meeting invite. But I will also paste a link to it in the chat in case that's more convenient.
and
please feel free to add yourself to the attendee list and any agenda items that you have, or topics of interest, and if the agenda is little, a little light feel free to just chime in with voice or video, whenever you're comfortable
so we can, we can get started. I put this on there yesterday, because I think we're ready to do the release. I managed to get contrib done late last week, so
should be good to go. I have 3. We should look at the list of Prs. But I had 3 that I thought would be
kind of nice to have, and one of them that's mandatory. This one's mandatory.
So the 1st one is about the disk buffering. But I wanted another set of eyes on this, because I had to push changes to it. Oh, it already got approved. Good. Okay, so let's do that one.
And then this one, so
we can't. So this is I. I know I didn't want to do this? They're different. They're different things, right? So these these 2 types are different. And the underlying string values are different. So you can't value of on these enums. They're not compatible.
Unfortunately.
**Cesar Munoz** 03:19 I remember there well, I mean.
**Jason Plumb** 03:22 Do you have an example where that works?
**Cesar Munoz** 03:24 A duplication, because the the Jvm. Target that comes from Kotlin right.
**Jason Plumb** 03:30 It does.
**Cesar Munoz** 03:31 I think they should have a factory method where you just pass the number 8 and then give you the.
Anyway, I just
**Jason Plumb** 03:41 Yeah, I know.
**Cesar Munoz** 03:43 Let me check.
**Hanson Ho** 03:44 Can we use the tool chain or something like that
that allows you to specify one thing, and it kinda just make sure everything works.
**Jason Plumb** 03:54 I would love to know how to do that.
**Cesar Munoz** 03:56 I'm not sure if the tool chain
works for coupling, too. I haven't tried it. I know it works for the Java pod.
No.
**Hanson Ho** 04:07 I never know what works for, what sometimes it works for sometimes.
**Jason Plumb** 04:12 Yeah, so pre, I mean, this is the change, right? It's like, previously.
we didn't have this target. Jvm, this would be new. And then that target Jvm. Is passed into the Jvm target option, and previously we were just doing a 2 string on the Java version.
But when I tried it. I believe that failed. So I had to. I think there's even
well, whatever it it definitely did not work
when I just did a 2 string.
using the compiler options this way.
And I think it's because this this set method on compiler options is is now strongly typed, whereas before this is just a string
if that makes sense. So the type.
**Cesar Munoz** 04:58 Yeah, it is.
**Jason Plumb** 04:59 Yeah, the type of Jvm target is Java Tar. Jvm target. It's 1 of these.
And previously string was okay. So I think the.
**Cesar Munoz** 05:11 It's also that we know, because coupling options is the extension created by the android plugin.
whereas coupling and then inside options is created by the coupling plug. So it's it's
and I think, internally coupling option makes a call to that one that just added, there.
**Jason Plumb** 05:32 Yeah.
**Cesar Munoz** 05:33 So, yeah, you know, Gradle can be fun.
**Jason Plumb** 05:37 Yeah, that's 1 way of putting it.
**Cesar Munoz** 05:41 If I mean it's I think it's nice, sir, to have it in a single place, because it's like we can just update a number, and then
the whole thing.
Updates. But it's not a blocker, so let I'll approve it, and if I find something I'll I'll add it there like.
**Jason Plumb** 06:00 Okay. I mean, we also don't need to like block the build on this block the release. On this I just thought it would be a nice to have, because this is giving warnings like the warning. Say, this is going away soon. You shouldn't be using Jvm target. So these are like. This whole thing is probably going away.
**Cesar Munoz** 06:18 No, that's fine. I think it's it's also it won't cause any issues.
It's just I'm just thinking about when we have to update it, which probably won't be soon, anyway. So.
**Jason Plumb** 06:29 Cool. And so please have a look at the change log as well. It's really. Just, you know, notes of what changed. I used the action for it, which was pretty cool.
And then, I, you know, did some hand editing? There's a bunch of stuff that gets in there that is unnecessary. But for those who haven't seen this before, we have this pretty cool build automation. We have an action called drafted change log entries, and I ran it apparently 17 h ago. But it's nice, because if you look at the output.
it runs the the delta between the last release and the current one, and it just.
**Cesar Munoz** 07:06 It was very painful to make it work a great
like 10 prs. Until the final words.
**Jason Plumb** 07:13 But it works. And this is a very nice starting point. So I basically just copied this deleted all the stuff that you know doesn't need to be mentioned in release notes and kind of categorized it a little bit. So we have a couple of new instrumentations, some enhancements, and some tooling changes.
That's kind of where it's at.
Please review. And then, once that's approved, we can do the release process today, and we will get 0 point 1, 2 out.
after much ado, in 3 months.
**Hanson Ho** 07:47 Wasn't it 11? I thought I thought it was 11.
**Jason Plumb** 07:50 11, th the current version.
**Hanson Ho** 07:52 Oh, okay. Okay.
**Jason Plumb** 07:55 And we're we're currently publishing 0 dot 12 snapshot.
So if you're on snapshots, that might be what you're thinking.
**Hanson Ho** 08:03 That's finally working right?
**Jason Plumb** 08:05 I mean you can't browse them.
**Hanson Ho** 08:07 The publish is successful, and you could you could actually refer to them.
**Jason Plumb** 08:12 Yeah. Someone over here confirmed that.
**Hanson Ho** 08:16 Fantastic.
**Jason Plumb** 08:17 Yeah, it's great.
Okay, that's all I have.
We can also look at the list of Prs to see if there's anything else that people think need to be in there, but it looks like there's nothing new. So.
**Hanson Ho** 08:32 So as I added a link to to the tool chain stuff! We could have a look.
I thought it would work should work, but.
**Cesar Munoz** 08:42 It. It should work. I'm just not sure if it coupling supports it.
I mean, you should work for Java stuff. But yeah.
**Hanson Ho** 08:52 In theory. If you said it once, it should
permeate everywhere, otherwise you'd have to like. Do the Kotlin version, which kind of defeats the purpose of this, but have a look
**Jason Plumb** 09:04 Cool.
**Cesar Munoz** 09:06 Yeah, I'll I'll take a deeper look. Thank you.
**Jason Plumb** 09:10 Yeah, I agree that having it in one place would be nice.
**Cesar Munoz** 09:13 Yeah, that's.
**Jason Plumb** 09:21 Okay, does anybody else have any exciting topics they want to bring up today?
The repo has been a little slow, honestly, so hopefully, getting this release out will help with some of that
last time. We mentioned briefly that.
**GZ Gregor Zeitlinger** 09:38 That's fine!
**Jason Plumb** 09:39 Yeah. Gregor, Hello.
**GZ Gregor Zeitlinger** 09:41 I was briefly looking at the Pr. For the disk buffering, and I was wondering
if this wiring code is actually or should be, part of the main implementation.
because it sounded like this, is bringing everything to life.
**Jason Plumb** 10:00 Are you to this one.
**GZ Gregor Zeitlinger** 10:01 Just wanted to ask, yeah, exactly.
**Jason Plumb** 10:04 Okay.
**GZ Gregor Zeitlinger** 10:06 This is wiring multiple things up. And I was wondering if this should actually be part of the main artifact.
or what the reason was to have it split up this way.
**Jason Plumb** 10:22 You mean, have some of the functionality be in contrib and have some of it be an android? Or what.
**GZ Gregor Zeitlinger** 10:28 Move more to contrip, because it looks like the setup here is really part of
demonstrating how it works well together.
**Jason Plumb** 10:40 I mean, it's true, it's true. Now, you can't create these exporters
without these storages, and the storages are built off of a configuration. So yeah, there is still some wiring that has to happen.
But you're thinking there's opportunity to sort of do more of this and contribute.
**GZ Gregor Zeitlinger** 10:58 Yeah, because right now it's probably quite hard to use. If you don't have a look at how it's done here in Android.
**Jason Plumb** 11:06 Yeah.
yeah, especially in the use case where the same configuration is being used. And that was that was the thing I wasn't entirely sure of like. We started with a configuration we already have, and I didn't.
I don't remember the details inside here, but I'm assuming the same. One can be reused for all 3
because we passed the signal name. So they're probably isolated enough.
**GZ Gregor Zeitlinger** 11:29 Yeah. Oh, yeah.
**Jason Plumb** 11:31 So there's probably an opportunity. I mean, I think I see where you're coming from. I think there's an opportunity to just have, like one kind of more standard configuration or one standard exporter that's kind of responsible for doing all 3.
**Cesar Munoz** 11:47 One quarter for all trains.
**Jason Plumb** 11:49 Well, just like that wraps it right like, at least in the setup phase, like some sort of exporter or exporter creator that can do.
**GZ Gregor Zeitlinger** 11:57 Query, method, maybe.
**Jason Plumb** 11:59 Yeah.
**Cesar Munoz** 12:00 Factory. Got it?
**Jason Plumb** 12:02 I mean the the underlying, like interfaces are different, so it can't be literally one exporter, but some sort of like singular factory for doing all of this setup. Yeah, I mean, I think there's opportunity there.
It's too early in the morning for me to get a sense of what that might look like.
**Cesar Munoz** 12:19 No, but that's fair enough. I'll I'll keep that in mind with the
small refactoring that I'm planning to apply this buffering anyway.
**Hanson Ho** 12:29 In theory.
**Cesar Munoz** 12:29 Make it any easier.
**Hanson Ho** 12:31 In theory you don't need to be android to use this right. Everything should be just completely usable from contrip. So almost everything should be there, and Android should just be bringing it in and say, Hey, we want to use it
unless there's some weird config that we have to, that we have to do. But hopefully, there isn't
like permissions, or you know, something like that.
**Jason Plumb** 12:51 Which I think that is true. Today, I think you can use this from non android. It's just that you have to go through the same setup, and it's a fair. It's a fair amount of work.
**Cesar Munoz** 13:00 It's
I'm gonna try to find a balance, because I also know that if we make things too smart, then probably can do stuff that maybe some people don't want to do so. For example, if we create an A
the factory that creates the 3 exporters.
I'm pretty sure somebody will come up and say, but I didn't use metrics. So this is, you know, consuming memory in my app, and I don't.
**Jason Plumb** 13:24 Right.
**Cesar Munoz** 13:25 Things like that. So
you know, let's see right? Maybe we can be a lazy factory or something like that.
**Hanson Ho** 13:33 Yeah, I think if you want to use this as a server side, they can look at the code copy of it. And if there's enough people using it. Then it's like, Hey, maybe then we do something about it. Until then it's like there's probably other things.
**GZ Gregor Zeitlinger** 13:49 Do we actually no.
**Cesar Munoz** 13:50 Yeah.
**GZ Gregor Zeitlinger** 13:51 Anyone else is using it. Have there been questions about it?
**Cesar Munoz** 13:56 About this buffering.
**GZ Gregor Zeitlinger** 13:58 Yep.
**Cesar Munoz** 14:00 Yeah, there was. There was an issue somebody created when trying to use this on a windows machine, wasn't it?
**Hanson Ho** 14:06 Windows. Machine. Okay.
**GZ Gregor Zeitlinger** 14:07 All right. Yeah, right.
**Hanson Ho** 14:11 Like, for like a Java desktop client.
**Cesar Munoz** 14:15 Yeah, I think, I guess. Yeah, I I don't know if they mentioned the details, though. But yeah, they were trying to use any windows. So it definitely wasn't Android.
**Jason Plumb** 14:28 This is us, this is us! What is? Was it closed.
**Cesar Munoz** 14:35 Let me see again if I can find.
**Jason Plumb** 14:39 I mean, I don't know who this person is, and they hadn't, you know they they improved it by adding the event name to the log record.
I think they ended up implementing this. Yeah.
But aside from that, I'm not. I don't know which one you're talking about.
I got the link.
and nothing works on windows, anyway. So I'm not too concerned about it. Straight up, broken.
**Hanson Ho** 15:02 I'm trying to say, just because it's Java doesn't mean it'll work.
**GZ Gregor Zeitlinger** 15:08 Interest.
**Jason Plumb** 15:10 Okay, I, wanna, this is, this is a total digression. But our agenda is very light. I wanna digress a little bit about windows because it really is a problem. Okay? So I'm working on a completely unrelated Pr has nothing to do with Android.
Check this out. So the the tests all fail on windows and like, why are they failing? I've had. I've sprinkled a bunch of debug like logging in here just to see what happens. But we have this thing
in a test that says, get resource. It's just trying to load a config file using the standard Java get resource. So in windows the resource looks like this.
And if you convert that to a file like the, you know, URL, dot file name is what we're using. Here's the file name.
and it's using forward slashes, even though it's windows. But then, like, you know, the user's home directory is just like with backslashes that's cool.
like, consistently.
**Cesar Munoz** 16:04 Hmm.
**Jason Plumb** 16:05 I don't like. I don't know of a without doing, you know, several lines of Regex or something. I don't know how to like
handle files and windows consistently with Linux, like I've been doing this stupid job for 25 years, I should know how to do this. Maybe, anyway, that's my! That's my aside rant.
**Cesar Munoz** 16:24 Or is this a little confusing to me?
**Jason Plumb** 16:26 Hi.
**Cesar Munoz** 16:26 Even once read somewhere that it apparently windows can support. Forward slash
for bats, too. I don't know but it's it's it's all confusing.
**Jason Plumb** 16:38 Modern shell can. Yeah, I'm not. I'm I don't know if Java is happy with it, though, anyway.
**GZ Gregor Zeitlinger** 16:44 Go has the same problem. You have to use a special function to change standard to system delimiters. This is how they do it.
**Jason Plumb** 16:56 Yeah, path dot separator and our file dot separator, whatever that stuff is. Yeah.
**GZ Gregor Zeitlinger** 17:01 Yeah. Yeah.
And you usually forget to do that until someone tries with windows and files a bug.
**Hanson Ho** 17:10 If if there is desire to make this always compatible windows, there should be tests that run on windows when you make it just a regular change on stuff, but there isn't. So that that tells me how much that use case is is prioritized.
**GZ Gregor Zeitlinger** 17:28 I have added a windows test to contrap.
so that it doesn't happen again.
**Hanson Ho** 17:34 Oh, cool!
**Cesar Munoz** 17:35 I am.
**GZ Gregor Zeitlinger** 17:39 And it actually revealed a couple of things like resources not being closed, and windows is more strict about that.
**Hanson Ho** 17:52 Yeah, is there any like additional mention of support like for the Java SDK, so I know there's like bits on Android, because we put it in there. But like does it talk about like different different runtimes, different environments, or it kind of just like, you know, assumed to work unless proven otherwise, or or the other way.
**GZ Gregor Zeitlinger** 18:15 Good question. I have to see if it mentions anything
unless otherwise noted. All published artifacts support Java, 8 or higher does not mention operating systems.
**Cesar Munoz** 18:32 I think they mentioned Andre and and Gral Vm somewhere.
**Hanson Ho** 18:40 The Android explicitly. There's there's mention about Api versions and stuff like that and deshivering.
But windows is yeah.
**Jason Plumb** 18:54 So in case you didn't see it, this also happened.
This is like a pretty interesting bump
that's gonna be relevant to a lot of different projects and
the release notes. You know, this is, it's it's interesting because they're saying it's the 1st stable release since 2023. So cool like. That's an awesome milestone. We use this thing everywhere. So
it's cool. But the the 3 or 4 projects I saw this come into, not any of them broke. So it's like they they seem to have been
approaching this like at a at a nice slow pace. So that's good.
**Hanson Ho** 19:31 The alphas! Have been like pretty good in production for a lot of people already, and they wanted to do some more breaking stuff here by making it work in in kmp and native. But there's a bunch of stuff that made them kind of reverse course. So 5 is, I think less less
less of a big change than they originally wanted to be. A while ago.
**Jason Plumb** 19:58 Yeah, I that's that. That would be impressive if they had it like a clean room. Complete implementation that doesn't use anything from the Jvm. Huh?
**Hanson Ho** 20:07 They're very close, like there's just a couple of things, I think, forgot what they are, Jamie, I remember, but optimizations and stuff like that, but it's like they were. It was. It was like
close.
But they reverse course a while ago and did cut a release. So maybe 6.
**Jason Plumb** 20:27 Yeah, cool. I was also
these release notes. I read this Rfc. For the 1st time as well. It was new to me, and it has a funny, funny enough name that the marketing actually worked and got me to read it.
**Hanson Ho** 20:42 In Rfc. Oh, nice!
**Jason Plumb** 20:45 Yeah, it was new to me. I didn't. I didn't know about this. Rfc, so now I do.
**Cesar Munoz** 20:52 I did.
**Jason Plumb** 20:52 The.
**Cesar Munoz** 20:53 Either, and I didn't read it.
**Jason Plumb** 20:55 The Tldr is basically a convoluted way of attempting to reduce
user times for the user in terms of Dns queries, connection setup time choosing between 4 and 6 for ipv. 4 and ipv. 6 for networks. So it's like those are the 3 main approaches. And when when do you do things concurrently to make those times shorter for users
at the expense of network resource utilization.
**Cesar Munoz** 21:27 Okay? Attempts. Both.
**Jason Plumb** 21:29 Yeah, anyways, new to me, there didn't seem to be, you know, too much else that was
too intense. But anyway,
feel free to add any other topics, because our agenda is light, and if we don't get any, then we will end a little bit early.
**Hanson Ho** 21:46 Is there a client one today, or is is this the off week.
**Jason Plumb** 21:53 Let me answer that it is today.
**Hanson Ho** 21:58 Okay.
**Jason Plumb** 21:59 According to my calendar.
**Hanson Ho** 22:07 I don't mind some extra time back if there's nothing.
**Jason Plumb** 22:09 No, I think that's cool. There is one new issue and our build failed. So this
probably needs to be resolved before we do a release.
What the heck happened here.
**Hanson Ho** 22:25 Snapshot, womp, womp.
**Jason Plumb** 22:30 Oh, boy!
**Hanson Ho** 22:34 4, 1.
**Jason Plumb** 22:36 Huh!
**Hanson Ho** 22:37 Yeah, I was just gonna say, Huh.
**Jason Plumb** 22:40 But like just on the compose click.
that's weird. In any case, I think we don't need to be publishing shaws of our signature.
I think this came up in another repo like this. I think that this is Asc is a signature file.
and then we're doing it. I think it's just standard, but not like we can browse it anymore. Let's see.
if we go.
Who?
I don't even know how to browse right now.
Well, okay, we will have to figure this out. Maybe I will rerun the job and see what happens.
And then let's see what this is.
Is this a dupe I feel like this was brought up before.
Why are they on, O Alpha.
**Cesar Munoz** 23:41 Oh, yeah, it looks like Ham.
**Jason Plumb** 23:47 Yeah, this is, this is what we think will be fixed already. Right.
**Cesar Munoz** 23:51 It should.
or is it an older one?
I'll have to check.
**Jason Plumb** 24:01 Well, we can ask them to retest with the new version if we get it published, I mean when we get it published.
**Cesar Munoz** 24:08 Sounds good.
**Jason Plumb** 24:09 Okay?
And I could still attempt to build because that was failing on snapshot publish. I assume the normal publish is going to work fine, and Sonotype will have no problems ever.
Okay?
Well, thanks for joining us everyone.
I will reach out. I will reach out if I hit any stumbling blocks. Are you around today, Hanson, to help out if if things get weird.
**Hanson Ho** 24:43 I am ping me directly.
**Jason Plumb** 24:45 Okay, cool.
Thanks, everyone.
Thank you. Bye, bye.

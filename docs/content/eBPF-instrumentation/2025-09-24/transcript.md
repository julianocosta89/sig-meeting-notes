SIG: eBPF instrumentation
Date: 2025-09-24
Duration: 24 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:28 Hey, Mattia.
**Mattia Meleleo** 00:30 Hello, Taylor, how are you?
**Tyler Yahn** 00:32 Doing well. How's it going?
**Mattia Meleleo** 00:35 Could be going better.
**Tyler Yahn** 00:38 Yeah?
That's not good.
What's, what's on the agenda for the day?
just work.
**Mattia Meleleo** 00:48 Yeah, do they just work?
**Tyler Yahn** 00:50 Yeah.
Did you have a good weekend?
**Mattia Meleleo** 00:55 Yeah, sort of.
Didn't do much, but it was relaxing.
**Tyler Yahn** 01:02 Yeah, no, that's always good. Are you by the coast at all?
**Mattia Meleleo** 01:06 Yeah, it's 10 kilometers, pretty much.
**Tyler Yahn** 01:08 Oh, okay, yeah. That's not too far. How often do you go?
**Mattia Meleleo** 01:13 Almost never. I, I, like, more than Good to meet you.
**Tyler Yahn** 01:19 Nice, yeah.
Yeah, I used to… I used to live in Florida, and it was, like, yeah, like a 10-15 minute drive, and I… I think I probably went, like, a handful of times. I used to never go, I just… yeah. It's funny how, like, when it's always there, you just never go home.
**Mattia Meleleo** 01:32 Also, the bad thing is that when it's actually good to go to the beach.
There is so much people that…
Let's say you don't wanna go anymore.
**Tyler Yahn** 01:45 Yeah, no, that's fair. I hate crowds at the beach. Like, that's… that's the worst, yeah.
I think that's kind of, like, my favorite part about the Oregon beach, is, like, it's so cold and windy, and it's, like, kind of inaccessible, too, that just nobody really goes. Like, I mean, that's not true, like, there's definitely people, but not, like, there.
And, I love it. Like, I'm fine being in a jacket on the beach, and, like, I really enjoy it, so, yeah. I think you're right, I think it's the crowds that ruin it for me, too, yeah.
**Mattia Meleleo** 02:16 Hello, everyone.
**Tyler Yahn** 02:17 Welcome, everyone. Yeah, I see…
We're all joining. If you wouldn't mind, go ahead and add your name to the attendees list. I think Rafael's the only one. If you have agenda items you want to talk about, please add them there as well. We can go ahead and get started here in just a second.
Wait for more folks to join.
**Rafael Roquetto** 02:49 Nicholas, probably not joining. If he does, it's gonna be later. He's got a kinder conflict.
**Tyler Yahn** 02:56 Okay, he was the one I wanted to ask the question on, but I guess I'll ask you this question, then.
Okay. Well, if that's the case, we can, we can jump in here. I'll start sharing my screen, and yeah.
We'll kick it off.
Shoot, alright, well, let's actually… There was one thing I wanted to…
put on here that I didn't,
So, I see Mike's on the call as well. I was just reviewing this, PR, yeah.
Where Mike has actually added some documentation around the Auto SDK, which is something that Obi also supports, so I wanted to make sure we call it out here, just so that… if you haven't yet, taken a look at this, it's worth, please take a look at it.
it's a… it's a good thing to document. I think it also may, like, inspire some…
I don't know, thoughts on maybe how we can also, you know, bring more visibility into some of the features that this project has. So, yeah, like, I think this is a great first step, and there's probably a lot of other things we can do. So, yeah, if you haven't yet, please go ahead and take a look at that.
Mike, I don't know if you want to say anything else, I was just wanting to make some visibility in there.
**Mike Dame** 04:23 Yeah, just kind of same thing I said in the SIG call yesterday, we've had a lot of users that want to do manual spans, and there isn't really any good documentation.
on that, and there are actually some nuances, like, you know, I had some people confused by the tracer provider setup, at least the main thing, or the lack thereof that you need. So, I'm trying to cover, hey, here's how to do manual spans along with EVPF. It links to Obi. In the Obi docs, I think I linked to this, and did a whole bunch of cross-linking into the Go manual instrumentation, too, making it clear, like.
you know, if you're using eBPF for these manual spans, don't do this, do that, like, so it doesn't have to be a huge, very technical page. I think, like, some description on how this works is just cool for people to understand and know.
that whole, like, Boolean flag, that we set, and, you know, importing the tracer provider that we set up. But yeah, take a look at it. It's really just about how to do manual spans with the… it's… I think we didn't… I didn't think putting it under
directly under Obi made sense, because it really is more of a feature of that, like, the Go instrumentation framework, and the SDK is hosted there. But if there's any other recommendations for where to put it, or just different structure for the file, or, you know, technical things that I got wrong, feel free to leave a comment in here.
But, yeah, I'll wait for…
everyone to, you know, approve it, and you know, give it a thumbs up, and this can also just be a first pass. We can add more stuff to it, but this is basically the notes that I wish that there was a page that I could send to a bunch of different users that keep asking about it.
**Tyler Yahn** 05:56 Yeah. Yeah, exactly. Okay.
Perfect. Thanks again, for that one.
Next up, I wanted to check in on our, V01 milestone here. This is something that we have…
been working towards, I've got this last issue, it's evaluate what we can move internal before this initial release, just to minimize the surface area of any sort of packaging. Obviously, like, we're not at a stable point, so we can still change the packaging, but it does help to…
Minimize that, just from documentation perspective, as well as user expectation perspective.
So, what I've done, one of the big,
blockers is the importation of this code in Bela itself. So, went through, the Bela repository to try to find all the imports, which is here. You can see most of it is just coming from this package.
There is this one, import of the test collector, as well, but,
Yeah, so then from there, I went back into our repository to try to find…
What is left, essentially, looking at the package directory, and it looks like there is this, like, config and instrumenter package that aren't used,
I don't know how useful it's going to be to move those, but we can…
you know, I can take a look at that, and see, like, you know, moving these two packages to an internal package and then updating all the imports of them.
maybe… mmm…
isn't the most valuable, but it's probably worth taking a look. The other one that I had initially thought was just moving this test package internal. The problem, though, is this test collector package. There's a lot here.
That I think would be nice to just move into an internal package to not, increase the size of the API. I asked,
Nikola, and about this, import on the test collector package here in…
Bela, and he said that there's a… that he was open to copying it. Raphael, I was wondering, maybe, is this something also you can think of? Like…
If we just took that import and we copied in the import into the Baylor code, or made a, you know, a version of it there, is that something that's reasonable, or are we trying to centralize on this?
**Rafael Roquetto** 08:15 I… I don't know. To be honest, I haven't looked into this, but what I can tell you is that Nikola raised this issue internally this morning, and Mario.
said he's going to look into it, so it might be good to maybe sync with him as well. Thing is, this week, we were having some internal events at Grafana. I don't know, I think Mario might be in one of those, that's why he hasn't joined, I'm just speculating. Nikola had a different calendar
appointment.
But, yes, what I can tell you is that, this was raised this morning internally, and Mario is going to have a look.
Okay, yeah. So it might be easier to see everything. I'm completely out of context with this, I haven't had the chance to look into it.
**Tyler Yahn** 09:01 Yeah, okay, yeah, no worries. Yeah, like, it's not a big deal, I do think that, like.
like, this, it would be nice to get out of our API, so we aren't exporting all this stuff.
I mean, technically we are, like, you can always find it in the doc site, but, like, just having it, in the main, links, it's a little bit easier to just not have that.
So, yeah, alright, we'll… we'll work on that. This should be, I think, the last issue before we get 0.1.
initial release out, which is blocking the Helm chart stuff and a bunch of other things. So, yeah, that looks like something we want to try to do.
Oh, Maven, yeah. Sorry, I'm getting distracted, but I can also maybe take a look at the, the baila code and see if I can, figure out a place where we copy this to, but,
Yeah, I will sync with Mario on that one, thanks for the heads up on that.
**Rafael Roquetto** 09:51 Yeah, I don't know if Steven has anything to add, in terms of the tests or anything.
**Stephen Lang** 09:58 No, not at the moment.
**Rafael Roquetto** 10:00 Okay.
**Tyler Yahn** 10:03 Okay, more to follow up then.
Alright, last up, I just wanted to go over open pull requests, make sure we aren't blocking anything.
So, Steven, it looks like you have this, draft PR. Did we want to take a look at this, or is this still something that we're working on?
**Stephen Lang** 10:20 No, that one got stalled, and I haven't had the time to go back into it just yet, so there's nothing to look at there at the moment.
**Tyler Yahn** 10:29 No worries, alright.
This update all of the patch versions is a renovate fix. We still need to take a look at this. This is being, blocked by, failing the CIs, based on, I think, the Prometheus update, so this is still something to take a look at.
Mario's, replacing internal tools.
I haven't seen any movement on this, we've talked about this in the past few weeks, so I think we could probably skip over this one as well.
Similarly, I think it's stalled.
Mattia, I think this is the first one we'll talk about. This is, something I think I saw some movement on, recently, where you've split things up, if I'm not mistaken, right?
**Mattia Meleleo** 11:07 I don't recall about splitting…
But yeah, the tests are now passing. Also, I enabled some more tests that were disabled earlier, and those are mostly being executed in the 5.15 VM.
So it might… when we merge this, it might happen that, that specific, test could time out, because I saw that, right now the duration is, around 1 hour, 1 hour and 10 minutes.
But if we enable the context propagation once, it can go, like, to 1 hour and 30 minutes, or something like that. So I saw a timeout.
Just saying.
We should, we should probably improve that part.
**Rafael Roquetto** 12:00 Yeah, yes. Yes. maybe, and it's not a solution, but if it starts failing, if it's the timeout, yes.
I wanted to tell you that I will get to this today. I saw that you… I saw your comments, I just didn't have the time yet to go into this, and hopefully can get it over, across the finish line today, and then…
Be free with this.
**Mattia Meleleo** 12:25 Huh.
**Tyler Yahn** 12:29 Okay.
Alright, yeah, that's,
tests that take that long are kind of troubling, so I… obviously this isn't causing that, but, okay.
This is… this is unfortunate. So, okay, it looks like, we just need some more review from Raphael on this one, and we'll keep moving forward. Obviously, we gotta keep an eye on… maybe we need some more engineering in our… in our testing framework to just make this
pass, let alone we definitely need some engineering in our testing to speed things up, I think, so…
**Mattia Meleleo** 13:02 I tried to look into it a little bit, but the issue is that we need a VM for this kind of test, and most of the time is spent waiting services to boot up, so…
And, I don't know.
**Tyler Yahn** 13:16 That's, that's a good… yeah, I mean, that's kind of an expected problem, I guess.
**Stephen Lang** 13:25 Which workflow is this? Maybe I can take a look.
**Mattia Meleleo** 13:29 It's the 5.15 integration test in the VM.
**Tyler Yahn** 13:36 Just this, like, something like this, the arm, or…
**Mattia Meleleo** 13:39 No, the one below? The…
**Tyler Yahn** 13:42 Oh, this one, sorry.
**Mattia Meleleo** 13:43 Yeah, this was successful in 90 minutes.
**Stephen Lang** 13:47 Okay, that's the longest workflow by far.
There's another one, 50 minutes there, so both of the VM ones.
That's slow.
**Mattia Meleleo** 13:58 For some reason, that kernel is slower, I don't know why.
**Rafael Roquetto** 14:02 And the VM is configured to have, 5GB of RAM, maybe… Increasing that.
good… work. I'm just looking at the code here. Like, is this KVM?
for this, for the CPU, so…
Maybe it's just like the same, Mattia, it's the kernel as well, 515 could be, like, yeah.
Lagging, maybe it's a combination of everything.
But the… Maybe we could, as a pre-experiment, we could try increasing the…
the ran amount, from, I don't know, from 5 to 16 gigs or something, because we're running… still running, like.
Prometheus, collectors, and things like that. Maybe that's the problem? I don't know.
**Tyler Yahn** 14:50 So why are we testing a VM here? Like, it looks like.
**Rafael Roquetto** 14:53 Good question.
**Tyler Yahn** 14:53 Yeah, go ahead.
**Rafael Roquetto** 14:55 Because, we need to test a particular kernel version, so 5.15.
**Tyler Yahn** 15:03 Oh, okay, I see. I see what you're saying, yeah.
Huh.
Okay.
**Stephen Lang** 15:09 Maybe I could take a look at this as a higher priority than the Kubernetes one, because the Kubernetes tests there are, you know, 38 minutes.
**Rafael Roquetto** 15:18 And I was kind of going…
**Stephen Lang** 15:20 top-down in terms of duration of tests, so maybe I could look at these instead.
**Tyler Yahn** 15:25 Yeah, Steven, I would really appreciate that. I'm guessing other folks would as well.
If you have time, that'd be great. I mean, 90 minutes to 50 minutes.
excessive. I mean, 38 minutes is pretty excessive in my book, but this is kind of, like, unbearable, so, yeah.
**Stephen Lang** 15:41 Yeah, well, the longest… the longest we had before was 45 minutes that I saw. That was the ones that are now sharded, and if these are taking twice as long as that, then…
**Rafael Roquetto** 15:51 It might be something with the current configuration as well, because if you look at the 6.10, it uses the same, like, 5GB, and it's taking 50 minutes.
Which is not great in itself, but, you know, it's almost half.
Of the 90-minute one. The only difference between these two is the same root file system, same image, the only thing that changes is the kernel.
So it could be…
Either 5.15 is bad, or it's just a kernel config that we need to rebuild the kernel in.
And enable something.
**Tyler Yahn** 16:28 Yeah.
I mean, it could just be… yeah, I don't know, I think… I think Steven's gonna have to take a look, and dig into it a little bit.
Cause, yeah, I think it could be a bunch of different things.
Okay, I'll leave it, leave it there to Steven if you want to take a look. Obviously, please report back next week if you do find that you can't fix it. If you can fix it, obviously a PR or something like that would be great to see. So, yeah, we'll pay attention to that.
**Stephen Lang** 16:55 True.
**Tyler Yahn** 16:57 Okay, cool. Back to the PRs. Similarly, the Prometheus common…
the GoMano repo and the GoContrib are all blocked on… these are breaking our CI, meaning that our instrumentation for these is… looks like it's a little flaky.
Or it's just not working. This one's an interesting one. I do kind of wonder if we need to be a little bit more,
specific in what's being updated here. Obviously, like, this is updating the GO 17,
Test server, which it shouldn't be doing, which probably needs a renovate configuration to fix this.
I don't know if we can ever upgrade this hotel dependency based on that, though,
So that's a little, troubling, I guess, but it's not… I don't know. Again, like, if this isn't an exported package, I don't think that's really an issue, so…
We can, we can maybe touch on that in a little bit, but I think otherwise, like, removing, you know, these sort of changes to these test files, I think it helps, pass this testing, so… just more, more investigation needs to be done.
Okay. Mattia, use configurable large buffers for HTTP requests?
**Mattia Meleleo** 18:09 Yeah, this is the continuation of the discussion about header and body extraction. This is the… this addresses just the first part, so, sending large buffers for HTTP protocol.
Yeah, so I addressed the… I think, most of the comments from Rafael.
I have another PR in the work, which uses these buffers for GraphQL spans.
I think this one right now is sort of ready,
there were some, some more things to change in user space, but I'm doing some more refactoring in the other PR, so…
We can, delay those changes.
**Rafael Roquetto** 18:58 Yeah, I agree. I think we could do that. Like, again, I saw your comments, I didn't have time to reply this morning yet, but I think this one is pretty much good to go. The only question that I had was.
And maybe I, I…
I looked at it the wrong way. It was the… the buffer size, but I saw that you updated it already, so… I'll have a look, but yeah, we could get this in. I have… I also have a patch on top of this.
PR. So… this is not…
this is not a problem with this PR in particular, but I was profiling the large buffers again, based on the…
the profiles that you and Imrod upload uploaded to the, linked issue.
And… I saw that… Part of the bottleneck is an append buffer on user space.
Because it does a lot of reallocations. So I… I got your… your branch, and on top of that, I…
I wrote a, like, a small proof of concept that uses static buffers instead, and it really made, like, performance disappear. So, like, the bottleneck. I guess in my machine, which is a poor one, CPU usage decreased from 20% to, like, 6. So.
**Mattia Meleleo** 20:16 That's very good.
**Rafael Roquetto** 20:17 Once that gets merged out, we'll, raise a PR, and then you guys can review and make sure I'm not doing anything stupid.
**Mattia Meleleo** 20:25 Yeah, thank you.
**Rafael Roquetto** 20:27 Norris.
**Tyler Yahn** 20:30 Okay, so on this one, we're just looking… Rafael, you're gonna take another look. We also are looking for other reviews on this. If you have time, please take a look. Yeah, so this looks ready to… for another round of reviews.
**Rafael Roquetto** 20:42 Yeah, it's pretty much, good to go. I'm gonna look another… do another fast, but… yeah.
**Tyler Yahn** 20:48 Yeah, alright, sounds good
And then the last two are just updates, which I haven't taken a look at, but these are probably, well, tests are failing on this one, which is not a great sign, but who knows? I'll take a look at those later.
Awesome. Alright, that, I think, is the end of the agenda. Yes, it is the end of the agenda. So I'll pause here.
Ask y'all if you have any other topics you wanted to discuss.
If not, we can… we can end the meeting a bit early here. I know Mattia wants to get back to the beach, so, yeah.
Yeah, a little inside joke there, I guess, now. But cool, awesome. Yeah, we can end it here. Thanks, everyone, for joining. Obviously, see y'all in Slack or, asynchronously, but otherwise, I'll see you in a week's time.
Bye.

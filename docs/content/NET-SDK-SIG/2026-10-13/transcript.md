SIG: .NET SDK SIG
Date: 2026-10-13
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Martin Costello (Raintank, Inc. – Grafana Labs)** 00:59 Hey.
**Matthew Hensley** 01:00 Hello.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:04 Did you have a day off yesterday, or was it not in your state?
**Matthew Hensley** 01:08 No, it's a federal holiday, and Grafana recognizes all.
Or being tight holidays.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:17 Or had you just completely forgotten that it was a holiday?
**Matthew Hensley** 01:21 Yeah, per usual. And it's not a school holiday here, so… Everyone leaves the house, and I'm just like, oh, I guess I'll go… oh, no, no wonder Slack is quiet, because it was also a day in, Spain.
**Alan** 01:39 Hey, everybody.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:41 you.
**Matthew Hensley** 01:42 Hello.
**Alan** 01:47 How's it going?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:49 Not bad. How about you?
**Alan** 01:52 Not too shabby.
I guess.
That'd be a good time to say I'm gonna be gone for a few weeks, after… after this.
Gonna be in Mexico for… till the first week of November.
**Matthew Hensley** 02:07 Hmm.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:08 Oh, nice.
Escaping to the sunshine.
**Alan** 02:11 Exactly, exactly, except it's unusually sunny here, so… Maybe, kind of not, escaping it. It's just colder here than I think it would be.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:23 That's usually how summer holidays work for people in the UK. As soon as you leave the country to go somewhere sunnier, it'll be sunnier at home.
**Alan** 02:32 Yeah, yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:39 Brian said he can't make it today.
**Alan** 02:45 Yes, I saw that, and actually… And then I saw Peter's message, too, which I hadn't… Apologies, I hadn't seen until… Just a moment ago. But it looks like Raj had reviewed that PR from Steve regarding the SDK Options, and it sounds like… Basically, Raj's… comment on that echoes effectively what I… Would say, too.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:24 Cool. So, the only things I put on the agenda for today is, I had a chat with Piotr on Monday, and, we submitted the SDK repo to Anthropic's new free We'll scan your code with Mythos and tell you if we find stuff.
As a service. They haven't merged the PR yet. I don't know what the criteria to get merged is, other than we didn't get outright rejected.
But… Various PRs before and after the one I opened have been merged, so I don't know why it hasn't.
But, we'll see.
If you… let me know if you want it adding on to the CC list, Alan, and I can update the PR, because they want a list of emails for it, but the security email for hotel is, like, the primary contact.
**Alan** 04:23 Security email for… oh, is that… is that, who's… who's… Who receives the security email from Hotel?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:33 I think it's either the TC or the security SIG.
Oh, okay. But I think it's basically, like, you know, like, the security at hotel.
email if you wanted to, like, you know, say there was, like, a vulnerability, and you didn't want to use GitHub.
**Alan** 04:51 Yeah, yeah, yeah. Gotcha, gotcha. And you're just saying, like, you can add additional emails if needed.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:58 Yeah, in the… in the… the PR is, like.
one file.
And it's got, like, a CC list that your additional emails can go in there, so… But I did, I didn't.
Add you and Raj on in case you didn't want to get the like yet more notifications.
**Alan** 05:21 I don't think I need to be added. I mean, I guess the only reason why I'd be, like, I guess I'd be mildly curious, like, if it found something, kind of like, how does… How does it work? What does it look like? But I can learn that through The people who are actually paying attention more to the…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:41 I imagine if something did come through the email anyway, it would end up in the GitHub.
Yeah. Stuff anyway. But yeah, So, in their repo, to get onboarded, there's just a YAML file.
basically.
**Alan** 05:59 Gotcha.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:59 And then there were two other files, but you have the option of either putting them in their repo or putting them in our repo.
So they're in our repo, because then we can control it.
But basically, you just… you just give them a threat model doc.
Or I just threw something together, which was basically, these things are important, these things aren't.
And there's a Docker file, because they ask you to build the repo. And then after that, the model looks at it offline.
**Alan** 06:30 Hmm.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:31 So in theory, all we should have to maintain is that one line, which Renovate does anyway.
**Alan** 06:41 Hmm, interesting. Okay, that's cool.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:45 So, I think… I think we're over the no, you don't qualify hurdle, but I don't know… When it's gonna get turned on.
Because the PR's been open for, like.
Two days now, and there's, like… I put, as just as a comparison, I saw someone from Grafana added Grafana.
And they did it, like… 5 hours after me, and it got merged half an hour later, so I guess there's probably an element of… no… notoriety… To the people they're taking in to make.
**Alan** 07:19 Grafana has higher notoriety than OpenTelemetry? Gosh.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:25 Apparently. And there's lots of other things, like Homebrew, OpenClaw. I guess they're going for name recognition to start with.
To try and make their program look good.
And then we'll be… we'll be in the boring… Trunch after that.
**Alan** 07:44 Well, it sounds like the GC needs to work on this, like, name recognition problem.
you.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:54 But hopefully we'll get merged soon.
**Alan** 07:56 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:58 Also… There's a I've got a milestone open for the next release.
I think the only one that I'd definitely like to get in for this release is the top one.
Raj already looked at it yesterday, but there was, like, one comment from… Copilot, which I fixed, but I haven't had to review on it yet. The other ones are just opportunistic to get in.
Just because it'd be nice. But otherwise, I was planning on doing the release either tomorrow afternoon, my time, or Thursday, once, the weekly renovate run has happened.
And then, once that's done, I should be able to move the Donna 11 PRs.
out of draft.
Because the latest RC comes out.
In the next hour or so.
Sorry, need to update that.
But otherwise, should be… Pretty good to go, ready for next month.
Cool. I love it.
**Alan** 09:08 It's the drop logs thing. Was that mainly just like an ordering kind of thing when things are being shut down?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:14 So… Yeah, sort of. So… Prior to, I want to say, 1.15, HTTP client factory didn't get used for logs.
Then… Someone did a PR to make it work, then that caused a bug.
So we reverted it, and then fixed it, and then reintroduced it.
Then that caused another bug.
Which has also been fixed, that affected Blazer.
And now someone's found another bug that isn't new, it's been there since HTTP Client Factory got turned on. But essentially, if you have a very short-lived app, and it hasn't sent any logs yet, and then you shut it down.
It will try and flush the logs as it shuts down, but it will need to resolve the HTTP client out of HTTP client factory, which is should would come from a service container that's just been disposed.
Two fails, and then it can't flush the logs.
So, the PR basically just… there's a fallback path that's like, with HTTP client fails, just try and make your… do what you would do if HTTP client factory isn't here.
As, like, a last ditch attempt to flush the logs out.
**Alan** 10:30 Interesting.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 10:31 But I just figured, as there's a release this week, I might as well get that in.
Rather than have it wait till next month, even as it's been there for… even though it's been there for a while.
**Alan** 10:42 Gotcha. I mean, I can look at the PR, but I'm curious, what, what is it unique about logs? Why not? Why don't metrics and.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 10:48 So…
**Alan** 10:49 I've heard this.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 10:50 The crux of it is there's a circular reference.
or or it… when it was first proposed to put HTTP client factory in it, it created a circular reference. I can't remember the specific details, but, you know, it was, like, HT… essentially, it was, like, HTTP client wanted to do locks, but we needed a HTTP client to send the locks.
So there was, like, a circular dependency, so it didn't have HTTP client factory integration.
Then we did some stuff to, like, lazily resolve it, which broke the cycle.
But then that's created this, like, tale of unrelated… well, semi-related bugs.
**Alan** 11:33 I see, I see.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:36 So yeah, if, if, if you don't, if the HTTP client factory type isn't in your app.
Then it won't go down this code path that causes short apps to lose logs anyway.
**Alan** 11:52 Gotcha.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:52 But if you happen to have any library that brings that type into your library, even if you're not using it, it will self-discover it to set up HTTP client factory.
**Alan** 12:02 Yeah, which is like OTLP exporter.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:05 Yeah.
**Alan** 12:06 Yeah.
Got it.
Okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:16 Before we just do the boring bit of looking at the PRs and the issues, is there anything either of you wanted to talk about?
**Alan** 12:25 I don't have anything.
**Matthew Hensley** 12:30 Nope, I'm good.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:36 Just as a random aside, I saw the release notes for this.
today's .NET releases come out. I think it's that they must have… finally caught up with the, like, the AI issue vulnerability flood. There's 44 CVEs in .NET 10 today.
that have been patched. I think that's the most I've ever seen.
I don't know what they are, because, it was just the titles.
But it's a lot.
**Alan** 13:13 Does that mean AI is earning its keep?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:16 Who knows? Maybe they're all low, and they're just annoying.
Rather than important.
**Alan** 13:23 Okay.
**Matthew Hensley** 13:25 Be interesting to see that list, especially since 8 and 9 are.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:31 Oh, yeah, the 8 and 9 list.
is similarly long, and I think… This is the penultimate patches for those.
I think they get one last gasp next month if it's really important, and then that's it.
**Matthew Hensley** 13:49 Little.
Hopefully people start upgrading runtime versions.
It's, it's always been theoretically not a great idea to be behind, but now… Yeah.
Actual problem.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:01 What's another 44 CVEs to ignore?
Between friends.
**Alan** 14:08 That's right.
That's where AI will really earn its keep, is if it actually gets people to upgrade runtimes when we start, you know.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:17 Hmm.
**Alan** 14:19 Sloughing off, like.NET Framework users and whatnot.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:27 And let's see what's on ahead.
That's… What are you talking about since last week?
At… I've got a bunch of PRs that are just… to be looked at at some point. I did another… Speculative. Hey, try and find performance improvements. Dig.
One of which… This one, I'll just mention this one because it's quite chunky.
There was a to-do in the code somewhere that said the way that exponential histograms worked wasn't always accurate.
And there's something in the spec that says, oh, if you build a lookup table, you can avoid that inaccuracy.
So I had, excuse me, so I had Fable go off and do that.
And…
**Alan** 15:21 Cool. I think I probably wrote that comment because I implemented the, the.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 15:25 you.
**Alan** 15:25 Original exponential histogram support.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 15:28 So I'm just gonna open the test file. I think, I think it's this one.
Yeah, so there was a bunch… there was a bunch of test cases that were commented out.
Because the rounding wasn't right, so they failed.
Those all pass now.
But it does… it is, like, relatively chunky, because it adds about 500 lines of code.
And there's lots of maths in it. And… I've read enough of the PR and the justification to, like, understand what it's getting at, but I do not… understand the maths in a way that I could do an exam on it.
**Alan** 16:08 Yeah, yeah, yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 16:10 So this one's very much, I drove an AI and it did some stuff.
But,
**Alan** 16:19 That's pretty cool, yeah, the lookup table was… something I… I guess I understood in theory, but to your point about the maths, like, it wasn't anything that I…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 16:33 Yeah, so as this one's a bigger change, I'm not pressing for this one to get into the current release.
Considering the size, but.
Like, if you ignore the magnitude, it also makes it 50% faster, apparently, in many cases, but it's, like, 2 nanoseconds, so…
**Alan** 16:54 Cool.
Yeah, one of the, one of the things that… there's kind of, like, a… I'll put this in air quotes, unit test, somewhere in the code base that I'd written to kind of get at… How… much impact the inaccuracy actually had in my assessment. There's the unit test, basically, like.
in a way illustrates that. I don't know if you found that test or not, but it illustrates, like, where those inaccuracies can happen, like in the.
On the far edges.
And… I'd wonder what the output of that test would be now with this improvement.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 17:43 Unless it was the test I just showed, it's not leaping to mind as something I saw.
**Alan** 17:51 Let me see if I can find the PR. I'm actually, like, so long ago that I'm kind of…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 17:57 Is it… is it maybe this?
There's a big comment today.
**Alan** 18:05 E… looks… Like… yes, this looks like the test that I wrote, I think.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:26 Yeah, I guess it's this one.
**Alan** 18:30 Yeah, capture the analysis, but not, like, really. It doesn't… it doesn't fail, basically. Like, wherever there's an inaccuracy, like, it's not a unit test in the sense that it doesn't blow up, it's just meant to… Hmm.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:43 So… Right, so I think… In the course of doing that, it deleted the test.
**Alan** 18:50 Gotcha.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:51 The test output help and clean deleted, and I think you were using that to output.
the analysis.
Yep. So I'm guessing that it's made that test redundant now, because they all map.
**Alan** 19:06 That would make sense. Yep, yep, yep.
Great.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 19:12 It was like, it was like these bits. It was like, sure.
Lots of powers and locks.
**Alan** 19:23 The… the math actually, like, of how exponential histograms work, the math actually did make sense to me at one point. I had a… I still have it somewhere. I have a Google Sheet that.
I created that helped me understand.
how… The bucketing worked.
At different scales, and so on.
It's kind of a… essentially a learning tool for myself as I was doing this work.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 19:56 Yeah, I imagine it's one of those things that makes a lot more sense if you make it visual.
**Alan** 20:01 Yeah, exactly.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:05 I think that's the only… One that was interesting.
That is in the main repo.
And… That's waiting on Norm.
Here, I'll put it in.
**Alan** 20:19 Yeah, this was the original PR that I wrote analyzing that.
That gap, and kind of making a case for the… idea that… the… inaccuracies were… Irrelevant.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:38 Okay, cool. I'll take a look at that tomorrow.
**Alan** 20:41 But, I mean, the fact that We remove all inaccuracies and also improve performance at the same time is great, you know?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:48 Hmm.
Yeah, it was just because it was like single-digit nanoseconds, I didn't want to sell it as a performance improvement by itself.
**Alan** 20:56 Sure, sure, sure.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:58 But yeah, yeah, at least it is in the right direction, rather than… it's more accurate, but now it's three times slower.
**Alan** 21:05 Right, right.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 21:08 And… Oh, yeah, I'm guessing you saw it, Matt, but.
Did someone open the PR with all the Kafka metrics stuff?
**Matthew Hensley** 21:21 Yes, the, first Tap.
of implementing this. The contributor here sent me a commit a couple weeks ago that I… Went through and reviewed and asked if they split it up. It was… All the changes in one, and it was… Little difficult to look through the, plumbing here.
double-check some stuff. So, I'm looking through it, it looks pretty okay. I just need to verify some weird behaviors with the Kafka driver.
And… Also have to try to figure out how to resolve.
some behavioral differences from the Java driver, because why would they be the same?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 22:10 And I think.
Otherwise, that's it.
Unless anyone's got anything else they want to chat about?
**Alan** 22:20 Sounds good.
**Matthew Hensley** 22:21 Don't… there was that one, It already got merged, but the Redis, like, adaptive polling interval, hopefully that.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 22:33 Oh, the one you did, yeah.
**Matthew Hensley** 22:35 Yeah, it's just… it's super basic, you know, because the benchmarking, that Covert did.
really work.
with, the .NET instrumentation because of the buffering here, so… In certain circumstances, it doesn't wait anymore.
And I'll go ahead and start flushing spans.
And the most typical ones. So Fortunately, there's still some just structural problems about… Doing my chills, but luckily we're… Talking with the… Maintainers are the drivers, something about that.
But did Charlize get us on that, the benchmark charts.
The one they did.
**Alan** 23:23 Cool, this fixes the, issue that you were talking about a couple of weeks ago.
With that, it was another vendor.
**Matthew Hensley** 23:29 Yeah, yeah, they did a, like, a… you know, soak test, where they had a mini HTTP API that hit Redis.
And because the instrumentation polled every 10 seconds. They were hitting the API so hard, they were overflowing Like, the span… Batch buffer that we have.
**Alan** 23:53 Yeah, yeah, yeah, that's right.
**Matthew Hensley** 23:54 They just didn't get anything useful out of it. So this is… An attempt, if they're doing… not using many of the options, like the filtering, it'll flush in a reasonable manner now.
**Alan** 24:10 Cool.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 24:13 If you want to, do a new release for it earlier, Matt. We can do that, like, today or tomorrow, unless you want to wait until I… Do you compete?
Release a Palooza.
Tomorrow or, Thursday.
**Matthew Hensley** 24:28 No, it's not urgent by any means.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 24:32 Okay, I'll roll it into the 20 wave when I do that then.
**Matthew Hensley** 24:39 Sounds great.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 24:43 Cool. Well, if that's… Everything, we can call it a nightly meeting.
See you next time.
**Alan** 24:50 Thanks, y'all. I'll see you in a few weeks.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 24:53 Oh yeah, enjoy Mexico.
**Matthew Hensley** 24:55 Thank.
**Alan** 24:56 Okay.
Take it easy.
Bye bye.

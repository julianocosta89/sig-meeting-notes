SIG: .NET SIG
Date: 2026-01-06
Duration: 39 minutes
============================================================

## Zoom Recording Transcript

**Matthew Hensley** 01:36 Hello.
**Martin Costello** 01:39 Hey, Matt.
Is it in your neck of the woods?
**Matthew Hensley** 01:46 warm.
It's a balmy 16 Celsius today.
**Martin Costello** 01:54 Oh, you… we've swapped positions then, because it's currently minus 4 here.
**Matthew Hensley** 02:00 Yes, yeah, duh.
Now that winter's started, we have to get warm again, and then it'll plunge.
Shortly.
**Martin Costello** 02:11 Yeah, I'm sure you'll be back winning the It's Cold competition soon.
**Matthew Hensley** 02:15 Oh, yeah. Oh, yeah, I'm… Well, maybe not. The Canadians can keep their air. We'll be good.
**Martin Costello** 02:35 If you're the other person who has the dock open, then I'm not sure who else might turn up, if anyone
Because reviews have been very quiet the last few days.
**Matthew Hensley** 02:46 I do not have the, node stock open.
**Martin Costello** 02:50 There we go, it was probably Alan.
**Alan West** 02:55 Ew.
**Matthew Hensley** 02:56 Hello.
**Martin Costello** 02:57 Okay.
**Alan West** 03:00 I was just put…
**Martin Costello** 03:02 Good, thank you. I was just pondering whether anyone else was gonna show up.
And it's also when I have the dock open.
Yeah, I don't know. I don't… I mean, I'm here now, but .
**Alan West** 03:14 I don't know… Other people's plans.
Let's see… Oh, Miraj is here now.
Heroes.
**Rajkumar Rangaraj** 03:30 Hey, Len. Hello, everyone. Happy New Year.
**Martin Costello** 03:34 N.
**Alan West** 03:35 Happy New Year!
**Rajkumar Rangaraj** 03:40 I won't be able to share, I joined in from a mobile device, so today…
**Alan West** 03:46 Sure, I can take it. I can…
There's not much to share, but I'll share my screen.
I don't have a lot to talk about, but I would like to get a release candidate of the sequel instrumentation out, maybe this week.
I think we're pretty, pretty set. Martin, you, you, you gave a…
the most thorough review of Steve's work in improving the SQL parsing stuff.
I took a look at it, too. I feel like it's in a… it's in a better place.
But do we have anything else that we…
**Martin Costello** 05:07 There was something I saw, I think it was yesterday, and I found it by accident, and it was a PR that you'd been tagged into, Alan, but I don't know whether you'd seen it or not. I saw there was… a change was made to the Java instrumentation.
For an issue where sometimes it might lock a password.
And, I think Trask typed you on it.
And if maybe that's something we'd need to check for.
In the sanitization on our side as well.
**Alan West** 05:44 Okay.
**Martin Costello** 05:46 Let's see if I can find it.
**Alan West** 05:47 Yeah, if you could find it, that'd be great. I'd probably have to… Scour through.
Alerts, or whatever.
That I've gotten…
Problem is now, I can't remember which repo led me to find it in the past. If it was Trask, it might… and it was Java, and it was a Java repo, it would probably be the Java Instrumentation repo, I think.
**Martin Costello** 06:23 I think, yeah, that's where the… oh, I found it there. It was, I found it via a Dependabog PR that was updating the Java agent, and I looked at the release notes, and then it was sort of, like, from here to there to there, to there, to there, and then I saw the PR.
**Alan West** 06:40 Gotcha.
**Martin Costello** 06:41 Mr. Pierre.
**Alan West** 06:47 I wonder if I can… There's a way to…
Does this work? I'm just making things up now.
No.
Convention is a thing.
mentions.
**Martin Costello** 07:14 I'm just gonna see if I can find it. There we go.
In the open circuitry Java Instrumentation repo, it's PR15607.
**Alan West** 07:43 Cool, okay.
Alternative, instead of trying to remove just the password.
**Martin Costello** 07:55 It might be that this is specific to a SQL variant that isn't SQL Server.
Because it talks about SAP.
But it looks like it has, like, a dialect where you can do things without quoting passwords.
**Alan West** 08:24 Interesting. Is this actual, like…
whatever the syntax of the dialog, would this, like, unquoted, these would be the actual passwords? Is that your understanding?
**Martin Costello** 08:34 That's how I read the diff. I don't know about SAP.
I don't usually look at the Java stuff, but it looked like something that…
probably isn't specifically catered. Like, like, if it… if it isn't a problem for us, it's probably…
By accident, rather than by design.
**Alan West** 08:59 Yeah, that would make sense, but… but if it's not quoted, I'll bet you that if, you know, we were to…
feed this string into our current parser, it probably… I would… I would guess that it would not…
sanitize these things. But that said, yeah, I think that we need to figure out if this is actually a problem for SQL Server, because this doesn't… this doesn't…
look… like, SQL Server type of thing, so it might not be a problem.
**Matthew Hensley** 09:30 I believe, SQL Server has a similar syntax for, like, remote tables or linked servers, whatever it's called.
Where in the query, you pass credentials, and then can forge a query to another server.
**Alan West** 09:45 Gotcha. Well, that's the thing that we'd need, right, in order to vet this stuff out, is the,
The test suite that we've been building upon, right?
we want.
we want real, real stuff. Like, I don't necessarily want to add stuff to that test suite that we're not writing instrumentation for, but if we come up with
actual, like, T-SQL statements, that we want to add to the test suite.
Because… at least at this point in time, because we're looking to ship the SQL client instrumentation.
If you can… if you… do you have a link to something like that, Matt?
**Matthew Hensley** 10:29 Yeah, I'm looking it up now.
I'll add it to the notes.
**Alan West** 10:34 Cove.
Yeah, yeah.
again, like, this is… my impression has been, like, we're not building a SQL parser, you know? And so…
that's why I've always had, like, the… I've always been more inclined to be, like, super conservative and do, like, best faith effort type of thing.
That said, as we discover new statements, because, like, I don't think any of us
know, you know, the full spectrum and depth of really any of these dialects. But if over time we…
Add new, test cases, essentially, if we find
problems, then I think that we can, you know, continue to chip away at that over time and basically improve our best faith effort. That's essentially been my philosophy.
If other people's philosophies differ, you know, that we can discuss, but that's kind of been the driving thing in my mind as we've been kind of pushing this forward.
**Martin Costello** 11:47 Yeah, so I don't… I don't think this is a new…
Sorry, it's not a new bug, it's not like it used to work, and now it doesn't necessarily, so I don't think it should stop the RC.
**Alan West** 12:01 Yeah.
I mean, unless it's… unless it really is, like, you know, this is legit, we could expose passwords, like, right? Like, that would be…
If we could find an example like that, then I'd be inclined to fix it before RC, but…
I also don't want to, like, you know, spend a lot of time trying to, like, search… search for that.
I prefer to kind of move move forward.
**Matthew Hensley** 12:27 I added links to two stored procedures that are built into SQL Server.
Both can, take credentials. It does use kind of like a parameter.
For the procedure, so I'm not sure if those are getting sanitized.
So, might be okay, but… Definitely a good test case.
**Alan West** 12:47 Yeah, if the, if the, if it's quoted…
If wherever a password might show up, if it's quoted, then I'm…
reasonably confident, yeah, like here, like, I don't know what this looks like.
Remote password.
We could certainly add this test case, but because it's quoted, I'm… I'm reasonably confident that it's gonna sanitize it just fine.
That said, I'm not the expert in the sanitizer anymore, because it's been pretty significantly reworked by Steve.
So, you know, I can't say,
Like, 100% confidence without actually, like, adding the test case, but…
But, yeah, things like this…
I'd… I'd welcome just small PRs,
Adding to the test suite. If it works, Great, thumbs up, like…
add it to this test suite. If it doesn't work, and if it's not, like, a…
If it's… if it's not a huge, like… Pressing security kind of concern.
Martin, you came up with a good idea.
A while back… Which was to…
Let's see if I can just, open up the… that's not where I'm gonna be.
It gets under shared, right?
**Martin Costello** 14:25 Oh, the fuzzing stuff.
**Alan West** 14:28 No, no, no, no, I was… you came up with this idea of, like, as we add…
Actually, I think they're buried here, because these are the test cases that aren't yet in the semantic conventions, but…
the idea that we can add test cases here super easily, and if they work, like, great, you know, more test cases, the merrier. If they don't work,
And… we don't have an immediate, like.
fix for it, I think it's still good to start committing them. And you had this idea of, like, just adding an additional…
Field to these test cases, which is, like, you know, skip.
**Martin Costello** 15:02 Oh, yes, I remember that.
**Alan West** 15:03 Something like that.
in that way, you know, we can, as we have these conversations, you know, Matthew finds something here, and we're like, okay, like, let's add this. We can add it, if it doesn't pass, you know, we can just, like.
add a PR that just has at least the test case, right? And then open an issue and say, like, hey, this is a… this is a test case that needs to be…
Addressed, and then that way, you know, we don't lose track of, you know, where… where we're at.
I like that idea.
Anyways, okay, yeah.
I'll take a look at this. Thanks for sharing that, Matt.
And… Otherwise…
Yeah, I think I'd like to see if we can… we can achieve this this week. Ship in the first release candidate, letting it sit out there for a week or two, maybe?
And then, hopefully shipping a stable version.
Anything else to talk about? You mentioned the fuzzing stuff,
Martin in a Slack chain. I hadn't really had a chance to look at that, but…
**Martin Costello** 16:29 Oh, yes.
So…
There was a thing in the .NET 10 release notes that was about, oh, we've made some changes to the JIT to do with bounds checking, and that we can align them and make things more efficient.
So I had a quick scan through the code last month to see if we could get rid of any of them, and the long story short was no, because the compiler isn't smart enough to align the BAME checks in the places where the unsafe
code is being used. But then that… then, flash forward about another two weeks, I saw there's a… there's a… it's not a neighbor check, there's a check in OSSF scorecard that, at some point in the future, I don't know when it's going to start marking down the
Libraries that use unsafe…
in their code. So then I thought it'd be… might be a good idea to put fuzzing around the bits of code that use unsafe.
And the main culprit of that is the Geneva exporter.
And… whilst I was digging around in that, there's a few places where it's got unsafe and it doesn't check the bounds of stuff, and…
my knowledge of that side of C-sharp is not good enough to know whether or not that's a… it's a problem or not. Like, because the way the code works at the moment is it just does a bounds check and catches the index out-of-bounds exceptions, rather than checking it explicitly.
But some of them are in a safe context with, like, pointers.
And I don't know whether or not that's bad, hence the questions that I put in Slack.
The other day.
There was more… more of an abundance of caution, just in case. Oh, actually, yeah, there is a way to do something really gnarly with that, that's bad.
Sorry, I do have a branch…
in my fork to add fuzz tests for the Geneva,
Exporter, and then we can discuss whether or not
some of the balance checks we want to keep that I've added or not from what the first test fleshed out, but I didn't want to open a PR and make… and push it up, like, very explicitly, if there was, like, an unresolved… is there a bad bug lurking question?
**Alan West** 19:03 The Geneva exporter is essentially a Microsoft product, right, Raj?
It's, like, used internally.
**Rajkumar Rangaraj** 19:11 That's correct, Evan.
**Alan West** 19:14 And I think you, and if I recall, Blanche is still marked as the maintainer.
**Rajkumar Rangaraj** 19:24 Yeah, I'm the current owner of it.
Blanche is not working on that anymore, but yeah, I do. It's a very important component for us.
**Alan West** 19:45 I suppose you'd probably be the best one to speak to Martin's questions about that, but separately, I've kind of wondered…
Does it make sense for that component to continue to be in the contrib repository?
**Rajkumar Rangaraj** 20:00 Why do you feel, why that question is coming up, Anna? I just missed, just got sidetracked slightly.
**Alan West** 20:07 Oh, I just… you know, I mean, I'm looking at Martin, who doesn't work for Microsoft, and I'm seeing that, like.
the… if I understand you right, Martin, the main goal is, like, hey, you know, we've got this…
Like, security sweeping stuff that we're trying to apply as an open telemetry community.
To various things, and so this is one of the projects that you've been kind of, like.
Spearheading in the context of the… of the… Hotel.
NET repositories. And… We've historically not.
you know, had vendor components, in these repositories, and I'm just wondering.
I think that there was, like, some history there that made sense.
for the Geneva and, like, the one collector, there was some history that made sense in terms of, like, demonstrating
good patterns and practices in extending the SDK.
And I think that that was kind of the motivating…
factor in keeping them in the Contrib repository, and I wonder if that… if that… Factor is still…
**Rajkumar Rangaraj** 21:14 Right now, even…
it would be even more difficult. Those products being a stable product, finding a home for it, it's as good as changing the product name itself.
So it's a well-established one. So I think it's very too late to remove it from there, or find a new home for that. The moment we move out of the OpenTelemetry, we lose out that namespace. So it's as good as completely changing that product itself.
The branding for that.
That's where the biggest barrier is now.
**Alan West** 21:51 And to be clear, I'm not, like, necessarily, like, trying to…
**Rajkumar Rangaraj** 21:54 No, I'm trying to…
**Alan West** 21:55 I don't have a… I don't really know the story.
**Rajkumar Rangaraj** 21:58 To be honest, like, historically, I don't know why it has ended up here. So, currently, I'm warning that part, but I don't know the actual reason why it was made as a part of the Contrib repo. Because I recall we removed the Application Insights SDK from the Contribo a long time back.
But I had no idea why genuine was made here, what was the decision and everything.
probably our main need to speak with Siju or Blanche to understand the context of it. But I think even if we lead a discussion in that way.
It's too late, I believe. Like, we won't be able to remove that, considering the… it's used by almost all the internal .NET projects uses this. Microsoft internal…NET project uses this package.
**Alan West** 22:57 Yeah, gotcha.
Anyways, I don't know if that,
is useful information to you, Martin, in terms of, like, you know, how…
**Martin Costello** 23:08 F…
**Alan West** 23:09 important these components are for anyone other than Microsoft.
**Martin Costello** 23:14 It's an interesting context, although in some ways it makes getting an answer to, is it a problem?
Maybe more important, because if it's in everything, And there is a bug.
It'd probably be prudent to fix.
**Rajkumar Rangaraj** 23:30 What is the bug, Martin? Like.
**Martin Costello** 23:33 It's not… that's the question, is it a bug? There's some code somewhere that, in an unsafe context, doesn't bound check something.
And it's whether or not that is a problem, is the question that I asked in Slack.
**Rajkumar Rangaraj** 23:48 Let me take a look at it and respond back to it.
**Martin Costello** 23:55 Because, yeah, if there's a risk of it, you know, doing a buffer overrun or something, then it probably needs fixing.
**Rajkumar Rangaraj** 24:01 Yeah, I don't think there are any issues, so it has to meet the security standards, this product. If not, it's going to impact the complete Microsoft.
So, I don't think there should be any bug in that, especially in the unsafe part. If it is there, it would have been caught very, very early stage. So, let me take a re-look and update you on this luck.
**Martin Costello** 24:25 Okay.
**Alan West** 24:27 That's interesting. Are there… are the… whatever…
security vetting process you have at Microsoft, are they using, like, tooling or whatever that you believe would have
It goes through the… the… everything goes through the scanning and all. We, like, the…
**Rajkumar Rangaraj** 24:46 the product is not used, though. We take the NuGet from there, and again, we re-sign internally for the internal needs. So, kind of, we clone and do a resign of this project, so it runs through all our pipelines, which need to meet
It goes through our whole internal pipeline process, so if anything is there, from a security perspective, it will definitely cache there.
**Alan West** 25:13 Gotcha.
I guess where my mind was going, and it doesn't sound like this is probably gonna be the case, but, like, I wonder if there's…
Any tooling that we could apply earlier on, essentially, like, in, the… contrib repository.
That would basically signal that this is… this is safe.
Because, right, that's kind of the… that's… that's essentially the high-level goal, right, Martin?
**Martin Costello** 25:41 Yes.
Yeah, because also what points to…
asking the question, is, like, the class… I think it's the right… the same class where I did it. Like, if you search for the word to-do, there's, like, 10 lines of code that will say, to-do. What should we do when this is invalid?
Which no one's ever clearly come back to and answered the question.
**Rajkumar Rangaraj** 26:06 So, who reported this issue? Is there some tool that ran, and it reported.
**Martin Costello** 26:10 No, no, no, no, I was writing fuzz tests for the Geneva component because it has unsafe contexts in it, so I thought it was a good candidate. And then, through looking at the code, I was like, huh.
So, the reporter is me.
**Rajkumar Rangaraj** 26:28 So, that product has been especially designed for high-performance scenarios. So, you will see all the tweaks that could have happened to that product. If you go through even the PRs, which is in the past, how… why that got added in this repo itself, there would be a lot of conversation would have went on on that.
**Martin Costello** 26:48 Yeah, I figured it was for performance reasons.
**Rajkumar Rangaraj** 26:52 Yep.
**Martin Costello** 26:58 But then that sort of flips around to the blog post I mentioned earlier for .NET 10, which is like, lots of code does things with unsafe that… for performance, but actually…
It's better now, so you should have the safety.
So… You know.
**Alan West** 27:24 Yeah, interesting stuff.
Did I understand, though, maybe I misunderstood this, but was this also in part motivated by, something that the whole hotel community is doing, in terms of, like.
Secure.
**Martin Costello** 27:41 So, I know Piazza's been doing work to improve the scorecard score.
And I made a change a few weeks ago.
So that a future version of the scorecard action will understand the use of FSCheck as a fuzzer, which means we get a tick for do we do fuzzing?
**Alan West** 28:05 Which would improve the score.
**Martin Costello** 28:08 And then while I was poking around in that repo, I happened to notice that at some point in the last few months, but it isn't… as far as I know, it's not currently enabled.
They added a new rule that checks whether unsafe code constructs are being used.
And it's for two different languages, and I can't remember what the other language is, but the other… but one of the two languages was C-sharp, and the check just scans for use of unsafe… unsafe true, whatever the compiler flag is, and then you get a demerit, because you're using unsafe code.
**Alan West** 28:42 Gotcha. And is this, so this… yeah, I've not paid super close attention to the scorecard stuff that Peter's been doing, but…
the…
I believe, if I'm not mistaken, it's all somewhat tied to OpenTelemetry trying to graduate to, like, you know, a higher status as a CNCF project.
**Martin Costello** 29:05 That's my understanding, yeah. I think it's, like, one of the many, many checkbox items on a checklist somewhere about the graduation.
**Alan West** 29:16 And do you happen to know if, like, at this point in time, we… we as just, like, you know, the… the owners of the .NET stuff.
do we…
have to do stuff in order to… for the community to make that… that leap? Are, like, we basically holding them behind in… in a way if we don't do this?
**Martin Costello** 29:37 I'm not… I'm not aware of anything we're doing that would, like, spoil it for everyone.
But I think there's, like, a common… there's… I meant to go to the SecuritySig meeting yesterday, but it's right at the end of the day for me, and I just didn't feel like it yesterday. But,
maybe it's something that Trask would know more about, so I'll… they do the security sync every two weeks, so I'll try and attend
the next one, which is in, like, 2 weeks. And, maybe…
I can ask about it there, but I think there's, like, a sort of a…
Under… undercurrent, just in the background, trying to make all the schools better effort.
Because I think that's where things like using CodeQL and using Dependable, or Renovate, and all of those sorts of things come in.
And, things like the branch protection rules and other things.
**Rajkumar Rangaraj** 30:36 Oh, yeah
Yeah, if I recall correctly, if unsafe is a concern, even our OTLP exporter and the Prometheus, what we had.
That also uses unsafe. I remember adding unsafe code to the OTLP exporter for… to improve the performance.
So, the SDK also… not only the contrary report, the SDK repo also has… Issues related to it, then.
**Martin Costello** 31:02 Yeah, yeah, I think, I think there's definitely cases where
It's a bit of a blunt instrument to just go… unsafe bad.
But,
in the context of other things like that blog post I mentioned, and I think they're trying to remove a lot of unsafe from .NET itself.
That it's probably a thing that, over a long period of time.
would probably be preferred to be moved away from, whereas if it just came in now, it would probably be, oh, no, no, but it's fine. Especially if it's audited and checked.
**Alan West** 31:49 Cool.
**Rajkumar Rangaraj** 31:50 Yeah, one other small thing I have it for the entire team here. There is a long pending PR in the repo, the SDK repo.
Earlier, we had… we provided a feedback saying that, like, I think, Alan, you said, exposing the internal, implementation about that.
the… Contributor has fixed that, and it's again ready for review.
So, it's worth for us to take a re-look at it. Martin, you might have looked into it, like, I would recommend you to take one more time, a deeper look into it, because it touches the core part of our SDK. So, let's all review this and see if we can move this towards closure.
And then if you find some time, just go through this one, too.
**Alan West** 32:50 Okay, I'll do that. Yeah, I think my main concern was that there was new public API being exposed, and I was basically questioning whether we could avoid that.
**Rajkumar Rangaraj** 32:59 Yeah, still there is a public API, but it's not… they are not exposing at least the internal implementation right now.
Gotcha. One other thing, what I understood, like, about this, one of the internally, one of the PM pinged me, he said it's a very important thing, that OpenTelemetry.net can be used with, the Blazor apps, once this is released.
So, the… he was trying to explain me it's a bigger milestone, and a very good thing to add to the project. So, I did not have the context at all of this. I got… I got pinged several times, but I did not look into it, and then he provided a context of why this is important.
**Alan West** 33:40 Yeah, Blazor is… I think when we talked about this a long while back, one thing we discussed was…
and I don't know if this PR went on to do this, but… we…
would we feel comfortable, like, right, once we… once we… once we, say, ship this PR, would we feel comfortable, you know, basically stating, we support Blazor?
even though we don't have, you know, integration tests with Blazor. And is that something that we… want to…
do before really taking, like, a, you know, making a strong statement that we support Blazor.
**Rajkumar Rangaraj** 34:24 Yeah.
So, at least in this PR, whatever the, like, it's not directly speaking about the Blazor, or we added a support for Blazor. I think it's an… they kind of…
enable the implementation that is needed for the Blazor at this point.
I think that's a step forward. Whoever comes and contributes may need to have an end-to-end
stuff's added, including the integration test tool, for us to call out that we support Blazor.
**Alan West** 34:59 Yeah, fair enough. Okay, well, yeah, I can take another peek at this.
**Rajkumar Rangaraj** 35:06 I think it looks like there is some…
Questions in the chat. Let's take a look.
Okay, I'm just… Martin is giving me… Some inputs for us.
Because this is the one, only one topic I wanted to bring. That's all I have it.
**Martin Thwaites** 35:36 Oh yeah, hello, long time nossi.
I was just dropping in the chat about the Blazor stuff, because it's been of interest to me for a long time. I basically did what was in here. This is, like, the third attempt to remove the threading support and move it over to tasks, and even with that, Blazor didn't work out the box.
So… Yeah, I'm not entirely sure that this would fix it on its own.
**Rajkumar Rangaraj** 36:02 If you could find some time and provide some feedback on this period, it would be helpful, Martin.
**Martin Thwaites** 36:08 Yeah, I mean, this… I mean, I have seen this PR before, it's an innocuous…
change. I'm just saying, from a Blazer perspective.
**Rajkumar Rangaraj** 36:18 Okay.
**Martin Thwaites** 36:18 This might be a, you know, a, path,
part of the journey towards doing it, but it isn't going to be, to Alan's question, something where we can just go, we've done this, now we support Blazor.
**Alan West** 36:34 Yeah, good insight. Yeah, I kind of figured that that was going to be the case, but
Is there actually, like, a… Haven't looked at this PR in a long time, is there a,
What's the actual, like, changelog announcement?
Here… Actually, it doesn't look like there is a changelog yet, so…
**Rajkumar Rangaraj** 36:57 Yeah, no changelog, and the PR description has not been updated. It's still the old implementation details are present there.
**Alan West** 37:05 Okay, yeah, so then we should…
But anyways, that's… that's something we should ask for. Because we should at least know, like, especially if we're adding a public API, right? We should be…
Clear about what we're communicating and what we're actually, like.
Whose problems are we actually addressing with just this piece of…
Of the thing. It'd be nice to articulate that in the changelogger.
And the PR description, as you point out.
**Rajkumar Rangaraj** 37:33 Yeah, my only worry is that
it touches the very core, hard part of the exporting mechanism, so…
**Alan West** 37:41 Yeah.
**Rajkumar Rangaraj** 37:42 It needs a detailed review, yeah.
**Martin Costello** 37:51 it… excuse me… it's buried… it's buried away in the way GitHub hides.
old conversation points. But there is a…
link back to the ASP Netcore repo.
from this PR, I'll put the… I'll put the link in the, in the agenda, just because it's easier to find it that way than try and find it yourself on the UI.
And it's about real multi-threading in Blazor WebAssembly, so it's, like, tagged onto from there.
So I… so I think it's, like,
other Martin said, it's like, it's a stepping stone towards…
some Blazor enablement work, but it isn't, like, the single magic bullet that makes everyone's dreams come true.
**Martin Thwaites** 38:41 Yeah, basically what they're doing is they're gonna enable task support in Blazor. They're not gonna enable the thread pool. So because we use ThreadPool.
They won't be able to use it, so…
But yeah, this has been going on. It was supposed to be in .NET 8, and then it was… it's been progressively bumped.
from .NET versions ever since.
But yes, it will be task support, so we have to support task rather than ThreadPool in order for that to work.
**Alan West** 39:12 Gotcha, okay. Yeah, good context.
Alright, well, is there anything else on people's minds?
Okay Let's call it a day.
Talk to y'all soon.
**Rajkumar Rangaraj** 39:36 Thanks, everyone.
**Martin Costello** 39:37 Bye.

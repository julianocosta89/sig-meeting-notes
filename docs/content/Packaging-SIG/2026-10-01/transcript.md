SIG: Packaging SIG
Date: 2026-10-01
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Csaba Gyorgyi** 00:01 Progress.
Hi.
**Denys Sedchenko** 01:03 Hi, how are you?
**Csaba Gyorgyi** 01:05 Thanks, I'm doing great.
**Denys Sedchenko** 01:09 How staff on Ubuntu side?
**Csaba Gyorgyi** 01:13 Well.
We have the injector in the universe.
And we are very happy about it.
**Denys Sedchenko** 01:23 Oh, nice, nice, nice.
I have a question. Is Universe frozen in time when, like, Ubuntu version… new Ubuntu version ships?
**Csaba Gyorgyi** 01:35 What do you mean by frozen in time? If you mean that, You cannot, like, do big updates, then yes.
So everything you do must be an SRU unless you have a very specific exception, for example.
like browsers have it where obviously you cannot maintain the same old version for a long time.
**Denys Sedchenko** 01:58 Mmm.
So basically, like, if a new, like, basically it's just security patches.
**Csaba Gyorgyi** 02:07 Basically, or very important bug fixes that make it unusable or Back fixes that are safe to do.
So those are okay. And you have to do a thing called Sru. This is the process for it.
Where you propose that, okay, this is the bug, this is what I want to change.
And this is why it is safe to do the change, and it won't break, people set up.
**Denys Sedchenko** 02:40 And what if, for example, there was a vulnerability?
For, like, one year.
And affects multiple versions.
And the fix was fixed in the next major version.
Which, like, and… That fix is applied, like, to the code that was heavily refactored.
**Csaba Gyorgyi** 03:01 Hmm.
That.
**Denys Sedchenko** 03:03 You cannot easily just… you cannot easily just backport the fix.
**Csaba Gyorgyi** 03:07 Yes, I am sure that the security engineers have a playbook for that, but the usual solution is that A.
Security fixes are backported.
I don't know what happens if you cannot easily do this.
But I am sure they have a plan for it.
**Denys Sedchenko** 03:41 Hey.
**Antoine Toulme (Splunk Inc.)** 03:48 Right?
Everybody?
Let's see…
**Denys Sedchenko** 03:54 Let me fill the agenda.
**Antoine Toulme (Splunk Inc.)** 03:57 Yep.
**Denys Sedchenko** 03:59 Okay, who we have here… Please fill out the attendee section.
Okay.
**Antoine Toulme (Splunk Inc.)** 05:34 Okay, so, Benny filled the Packaging Doc.
Anything for discussion, folks?
If there's nothing, I will add something.
**Denys Sedchenko** 06:05 Maybe there are any updates regarding Kakao Hosts?
about infra…
**Antoine Toulme (Splunk Inc.)** 06:11 No, I mean, you've seen the thing from Austin, right? He's like, we're working on getting access, so he can give us access. I haven't heard anything since that.
**Denys Sedchenko** 06:24 No updates on my side.
**Antoine Toulme (Splunk Inc.)** 06:28 Okay.
I do have… Sorry.
I have a Pr for you all to review.
Finally got a chance to, address the feedback.
Just took 2 months.
Open that in the doc as well.
Also, just curious, like, how's the HumberTap work moving?
Is… is that something that people here are watching for?
No.
Okay.
**Denys Sedchenko** 07:23 Yep, please repeat the question if you didn't get that.
**Antoine Toulme (Splunk Inc.)** 07:28 So… just also want to understand that Damien Mathieu is one of the… original maintainers of this SIG, he was away on Pat Lee for a while, but he's back. And one of the things that he has been working on is to set up a home brew tab for macOS to install utilities for the OpenTelemetry.
and he added Ocb. There.
And I dared him to put the collector as well.
Homebrew is very lightweight, so it's just a, you know, a few Ruby scripts, and then you pretty much go download stuff from wherever it is on the internet.
Do I understand?
just a very different proposal from Debian RPMs, right? Of course, but… The hard part is how you manage the versioning and update the versions as they become available. It looks like it's got that down with some Build?
I was wondering if anyone here is… Looking into that, is there interest?
**Denys Sedchenko** 08:36 I can test it on… have a spare Intel VA machine and also ARM machine to test.
But yeah, partly some people use it.
**Antoine Toulme (Splunk Inc.)** 08:51 Yeah, it's interesting, right? It's brand new, so I don't expect that there's been that much use of it.
I'm just in general, like, interested to find out more about, like.
If you had this on Mac.
What would you install?
Would there be a collector? Right now, he's installing the builder for the collector, which is… Meh, right?
So…
**Denys Sedchenko** 09:18 Ideally a collector because like Building the collector using, like, the builder will take a lot of time.
Plus, you need to have a… toolchain installed.
**Antoine Toulme (Splunk Inc.)** 09:32 Yeah, I agree.
**Denys Sedchenko** 09:33 A lot of developers have Macs, and like, if they want to play with it.
like, having a Mac version is useful.
**Antoine Toulme (Splunk Inc.)** 09:43 So I don't know if there's a roadmap to be had there or a discussion that we're not having, but for what it's worth, if you were not aware, there is a homebrew app now. It's available.
it's a low-stakes type of thing, right? And, it's, you know, a little different from our mission of getting everything out so that people can use it in production on Linux boxes and Windows and whatnot, but… This, this is available.
**Denys Sedchenko** 10:10 And by the way.
**Antoine Toulme (Splunk Inc.)** 10:10 you.
**Denys Sedchenko** 10:13 People who are using immutable Linux distros also using Homebrew because it's the easiest way to actually get a package manager in those environments. They also appreciate that.
**Antoine Toulme (Splunk Inc.)** 10:24 I heard about that, but it's like Gentoo people or something.
**Denys Sedchenko** 10:27 Not just, like, for example, Steam Deck, you know, the gaming console.
It's running Arch, but it's, like, read-only.
Or like Fedora Silverblue, for example.
**Antoine Toulme (Splunk Inc.)** 10:42 Are you going to install the collector to use profiling to find out where your Steam game is slow? That's fun.
**Denys Sedchenko** 10:50 Apparently people are running Kubernetes clusters on that thing.
**Antoine Toulme (Splunk Inc.)** 10:54 Oh yeah, it was like a PlayStation 3.
**Denys Sedchenko** 10:57 Yeah.
**Antoine Toulme (Splunk Inc.)** 10:57 Clusters of them. Okay.
And to… the more the merrier, right? We want… we want this software to be ubiquitous, so… why not? It's just not the use case I signed up for when I started.
Okay, cool. Anything else, folks?
Everybody okay?
We're just waiting for… The powers that be to give us access.
**Denys Sedchenko** 11:26 Caba mentioned that we got the collector in Universe.
**Csaba Gyorgyi** 11:31 Injector.
**Denys Sedchenko** 11:33 Sorry, injector.
**Antoine Toulme (Splunk Inc.)** 11:35 Okay, that's cool.
Sorry, I missed that.
How did that happen?
And are you going to update it every two weeks till the end of times?
**Csaba Gyorgyi** 11:46 I mean… I don't really understand the question. I mean, we worked on it in the past few months.
**Antoine Toulme (Splunk Inc.)** 11:53 Yes.
**Csaba Gyorgyi** 11:54 And… it went through all the processes that it had to went through in order to get into Ubuntu Universe, and it will be in Ubuntu Stonking.
**Antoine Toulme (Splunk Inc.)** 12:05 This is Justin.
**Csaba Gyorgyi** 12:06 The injector, so no language specific anything.
just the injector written in SIG.
**Antoine Toulme (Splunk Inc.)** 12:15 Okay, so is it exactly the Debian RPM that we defined for the injector, or did you change it meaningfully so that it would pass the validation?
**Csaba Gyorgyi** 12:24 So, it should be the same.
Okay. So, obviously, we had to package it according to… Ubuntu standards, so we couldn't just use FPM.
But, we run it with, the upstream Docker integration tests and it worked.
**Antoine Toulme (Splunk Inc.)** 12:51 What is, when is this release? Go ahead.
**Denys Sedchenko** 12:55 Sorry.
One small question. How, like, you generate, Csaba, you generate the Debian source files in order, like, to build it, to submit it to… To the builder, how different is that?
Debian source… how different are those Debian source files from what we actually generate, Bill? Because we also…
**Csaba Gyorgyi** 13:17 Hmm.
**Denys Sedchenko** 13:18 going.
**Csaba Gyorgyi** 13:18 How do you even generate Debian source file? Don't you just use FBM that spits out a DEB?
**Denys Sedchenko** 13:27 We didn't do that yet, I forgot.
No.
Okay, never mind. Apologize.
**Antoine Toulme (Splunk Inc.)** 13:44 Okay.
Hi. So… When is that release? So we can also coordinate and make sure we make a big deal of this.
**Csaba Gyorgyi** 13:54 It will be in Ubuntu Stone King, which is 26.
Then? I don't know what's the exact release date, but then.
**Antoine Toulme (Splunk Inc.)** 14:06 Talking to 16, okay.
You stayed… About 15th of October?
final release.
**Csaba Gyorgyi** 14:24 If that's what's in the release schedule, then yes.
**Antoine Toulme (Splunk Inc.)** 14:29 That's what's in the reschedule.
**Csaba Gyorgyi** 14:32 So that's pretty cool. If nothing blocking comes up there, yes.
**Antoine Toulme (Splunk Inc.)** 14:37 I see, I see.
**Denys Sedchenko** 14:38 New LTS version or not?
**Csaba Gyorgyi** 14:40 No, it's not an LTS.
**Antoine Toulme (Splunk Inc.)** 14:43 Yeah, that's it.
**Csaba Gyorgyi** 14:44 2604 was an LTS, and the next LTS will be 2804.
**Denys Sedchenko** 14:55 Antoine, we also discussed with Csaba how the secure… like, how those packages that are universe, how they actually got updated.
Like, for example, LTS version is released, you install the injector one year, like… one year is passed, whether you're going to get an update, and, like, Csaba told that, like.
From what I understood, you only will get, like, important bug fixes and security updates, so, like, people can be, like, stuck with the old functionality.
**Antoine Toulme (Splunk Inc.)** 15:30 And my question would be, then, who… Who's maintaining… who's making the patches? Is that you?
Sabah?
Will you be making those?
**Csaba Gyorgyi** 15:41 So, one correction that I would say, I wouldn't phrase it like they get stuck with the old functionality. The main goal in Ubuntu is to provide a stable experience. So, if we were to update into a newer version.
Then maybe you are breaking someone's setup who is relying on that particular version or on that particular Behavior.
So… And in universe, basically, there are no guarantee for anything.
But if you want to do a bug fix, then there is a process called Stable Release Update, where you basically say that, okay, this is the bug, you explain why is it so important to fix, and that the fix won't break.
Someone else is set up, and when it gets accepted and released, then you will have Basically, an update.
But, the way you should think about it.
is that one of the promises of Ubuntu is that it remains stable, and not just in the sense that it won't crash, also that it will provide you a consistent behavior.
So you cannot, for example, just jump major versions.
If you have… A small bug fix that is really important and has a has a big impact, sure, you can do it. I am not that familiar with security fixes, so I cannot talk much about it, but I know that that's a different process.
If you have a security issue and it must be patched.
**Denys Sedchenko** 17:23 Saba, are you the maintainer of the package, or it's someone else? And I assume we might need to be… stay in touch with the maintainer, so, like, to actually discuss, like, hey, this actually would make sense to be included in an update. This is important.
**Csaba Gyorgyi** 17:40 So, in Ubuntu, there is no maintainer.
So, if you look at the… opt info output, most of them are owned by the Ubuntu developers team. So there is always a team ownership, and it's not like Sina is the maintainer or I am the maintainer.
Technically, anybody with upload rights to that package can make changes. So, for example, our mentor, is a core dev.
And technically, he can upload anything he wants.
**Antoine Toulme (Splunk Inc.)** 18:18 See.
Thank you for that.
Okay, thank you for this. This is awesome news. Do we want to push this news to the world with some release blog post when this releases?
Something like that. Just make sure people get appraised that we're making steady progress.
**Denys Sedchenko** 18:45 Probably definitely like Ubuntu is one of the popular.
**Antoine Toulme (Splunk Inc.)** 18:49 This is it.
**Denys Sedchenko** 18:49 Docker images and also the server operating systems, one of.
Yeah, maybe this can be a cross post between, like.
Canonical's account and our account, like, a collaboration. So we'll get two acts of engagement.
**Antoine Toulme (Splunk Inc.)** 19:11 Okay.
If you have any, link, Csaba, to the work, any official package description, when it becomes available, can you please, post it on Slack when you get a chance? And then… We… we can very quickly draft a blog post, and put it for your review, and then we can… we can cross-post that between the accounts, if you want.
**Csaba Gyorgyi** 19:36 What kind of materials would you like to see?
**Antoine Toulme (Splunk Inc.)** 19:41 Just you have do you have a public URL to the package description on the internet?
I know Ubuntu usually does that. I'm just making.
**Csaba Gyorgyi** 19:48 You mean the Launchpad link, that?
**Antoine Toulme (Splunk Inc.)** 19:52 Yeah, I'll take it on.
**Csaba Gyorgyi** 19:53 Brilliant. We can.
Post that kind of thing.
**Antoine Toulme (Splunk Inc.)** 19:59 Okay, yeah.
That's awesome. So, and… Do you want to do more than the injector or do you want to just stop there?
**Csaba Gyorgyi** 20:09 Well, that's a great question. So the context is that it's only the two of us, Sina and I, who are working on it as a side quest.
So… No, so just treat us like kind of A volunteer.
people, so don't expect, like, any big amount of human resources invested from our side.
And currently the language specific stuff has so many dependencies that we cannot satisfy, that it would take years to package all of that, even if it's possible. So, I can talk very long about the challenges here.
But so far, we are happy with the injector, and we don't want to start on language-specific stuff unless we see that, okay, it can be done with a reasonable amount of effort.
**Antoine Toulme (Splunk Inc.)** 21:12 I was more faking the collectors and languages, because the injector is only as good as if there's a collector nearby to pick up the data anyway, right?
**Csaba Gyorgyi** 21:21 Yes.
**Antoine Toulme (Splunk Inc.)** 21:22 So, unfortunately, we're gonna need to build a… find a way to make it so the collector is available through that, and the collector is already being deployed as a Debian archive.
So our goal right now is to start to own a Debian repository to make it easy for people to download and install stuff, and we'll get there. This year, I promise, as soon as we get access to things and we manage to kind of get everything wrapped up and all that. But we.
If you can, looks like if you cannot import a Debian package made by someone else, you would have to kind of source it yourself, right?
**Csaba Gyorgyi** 22:02 You mean someone wants to put it into the ABN?
**Antoine Toulme (Splunk Inc.)** 22:06 Yep.
**Csaba Gyorgyi** 22:07 So actually it will get into Debian unstable and to testing. So it's not kind of like a third party repo.
**Antoine Toulme (Splunk Inc.)** 22:17 Might as well.
**Csaba Gyorgyi** 22:20 because.
**Antoine Toulme (Splunk Inc.)** 22:20 the.
**Csaba Gyorgyi** 22:21 It's in Debian.
Then Ubuntu takes many, many packages from Debian.
**Antoine Toulme (Splunk Inc.)** 22:28 Yeah, you mentioned that before. Yes.
but then we.
**Csaba Gyorgyi** 22:32 If it's indeed in Debian, that's a different story.
**Antoine Toulme (Splunk Inc.)** 22:38 Yeah, I just don't know where to start with Debian, how to get involved and how to.
**Csaba Gyorgyi** 22:44 I don't know it either, I don't have the expertise.
**Antoine Toulme (Splunk Inc.)** 22:48 Yeah, I think you said that. Okay.
**Denys Sedchenko** 22:51 As far as I know, they're still using mailing lists, like, they're… Communication.
A bit hardcore.
**Antoine Toulme (Splunk Inc.)** 23:01 I think we should stick to our guns and just deliver first our own package repository for Debian RPMs. And then we iterate on that until such time it makes sense to push it to official places because it's too much scope.
We won't be able to do both at the same time.
I certainly don't have time.
Anyway, thank you.
Okay, is there anything else we should talk about?
I found the link to your Launchpad item, by the way.
I'll put it in the notes.
worth a…
**Csaba Gyorgyi** 23:37 Thank you.
**Antoine Toulme (Splunk Inc.)** 23:38 Blog post and announcement.
When stumpking is raised.
Okay.
**Csaba Gyorgyi** 23:47 Thank you.
**Antoine Toulme (Splunk Inc.)** 23:50 Well, thank you for your work.
It's pretty cool.
Alright, anything else, folks? Or we can cut it, Dodie?
Going once, going twice.
Going 3 times… Have a good rest of your day, evening. Take care. Thank you so much. Bye.
**Csaba Gyorgyi** 24:16 Thank you. Bye.
**Denys Sedchenko** 24:17 Bye.

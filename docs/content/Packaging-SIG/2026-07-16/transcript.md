SIG: Packaging SIG
Date: 2026-07-16
Duration: 38 minutes
============================================================

## Zoom Recording Transcript

**Denys Sedchenko** 06:56 Hello?
**Michele Mancioppi** 06:59 Hi.
**Denys Sedchenko** 07:03 How are you?
**Michele Mancioppi** 07:05 Oof.
I'm quite excited today. Maybe the day we got the 1st draft release.
**Denys Sedchenko** 07:13 Great.
**Michele Mancioppi** 07:16 Let's see if there isn't one.
**atoulme** 07:26 Morning.
Good morning.
Evening for you.
Hello.
Okay.
So.
Well, do you go?
**Michele Mancioppi** 07:49 We want to give another minute to Douglas, or maybe Ted to join.
**atoulme** 07:55 No.
Let's do the… Let's see this. So I got the doc up.
**Diego** 08:03 a…
**atoulme** 08:05 I'm just gonna start the nodes for today.
Okay, we got an agenda.
All right, so the way it's supposed to go is we have an agenda doc.
Stuff you want in there.
**Denys Sedchenko** 08:49 Can you give me… give us, please, one minute to add items to agenda?
**atoulme** 08:54 Yes, yes, of course.
You can, if that happens again, just go ahead and create the agenda before the meeting, if you want. This way, you can secure a spot.
**Michele Mancioppi** 11:32 I guess the agenda is complete.
**atoulme** 11:38 all right and I I don't see anybody else joining at this point so let's go all right.
**Michele Mancioppi** 11:43 That's good.
**atoulme** 11:45 Okay, go ahead.
**Michele Mancioppi** 11:46 So we have… Had, couple of months working on a on a couple of Prs.
I don't. I'm going to share the screen.
Number 10 and number 18, which are closely related with one another. Number 10 is the SPAC.
Of the the 1st version of the All the packages, and it went through… A good amount of reuse, I want to say.
And the next one is the first implementation, with, Support, to, push A first draft release with packages deployed on GitHub pages.
Now, my question to the sync is, do we want to start merging stuff?
**atoulme** 12:48 Yes, I'm in favor.
**Denys Sedchenko** 12:54 Agree as well.
If like something comes up, we can fix it later.
**atoulme** 13:01 Yep.
**Michele Mancioppi** 13:03 That's… Bastian Diego, you also want to.
to say something about this.
**Bastian Krol** 13:12 Hi, sweetie.
**Michele Mancioppi** 13:18 Then, let's go.
Yeah, I think we can put a bit more code for it here.
Since we all had our hands just didn't go through the, Do you want to put me the list of co-authors?
For this historic commit.
**atoulme** 13:51 Sure, she must, I really, I'm okay with this.
You're taking the glory with this one, but here's my name.
**Denys Sedchenko** 14:03 Give me a minute.
To find my corporate email as well.
**atoulme** 14:11 It's a good sign. It's a good sign if you don't know your corporate email.
**Denys Sedchenko** 14:16 Oh, my GitHub's private one. Like a private email. I will give you the private email.
Or it should be a corporate.
**Michele Mancioppi** 14:25 Whatever you please.
**atoulme** 14:26 It, it is.
We don't judge you.
But,
**Michele Mancioppi** 14:48 Do you think anybody else should be?
**atoulme** 14:52 No.
**Denys Sedchenko** 14:57 Maybe Jack as well. He also left some amount of reviews.
**atoulme** 15:01 Oh.
**Michele Mancioppi** 15:02 Whereas there's yeah, not.
**atoulme** 15:09 Peter.
**Michele Mancioppi** 15:14 Can you… can you add me the,
**atoulme** 15:17 We fight it.
**Michele Mancioppi** 15:19 Email track.
**atoulme** 15:20 I have a There's three Java somewhere.
Okay.
Check.
Yep.
All right, here you go.
**Michele Mancioppi** 15:45 Well, that's the GitHub user no reply. That's not exactly.
**atoulme** 15:50 It won't work.
**Michele Mancioppi** 15:52 That's not the best practice.
**Denys Sedchenko** 15:56 Just a moment. Just a moment. Here is corporate email.
**Michele Mancioppi** 16:04 Thank you.
**atoulme** 16:05 There. Appreciate it.
**Michele Mancioppi** 16:13 And also, many, many thanks to, Christian from Canonical, who left a lot of very useful review comments.
That really helped.
**atoulme** 16:28 Thank you.
**Michele Mancioppi** 16:28 Matthew Tri.
**atoulme** 16:31 Thank you, Michele. You should breathe in this one, sir.
**Michele Mancioppi** 16:35 Well, this is the first one. Now we have the big one, because this is Markdown.
And…
**atoulme** 16:42 Yep.
**Michele Mancioppi** 16:43 This.
There's the the monster one.
Oh, no, I have to rebase.
**atoulme** 16:52 Yeah, I thought there was a chance this would happen. Is there… okay. Hi, Dad.
**Michele Mancioppi** 16:58 So I'll rebase. Meanwhile, you can continue the discussion of copper for the packages.
**atoulme** 17:06 Let's do it So we have…
**Denys Sedchenko** 17:10 Yes.
**atoulme** 17:11 Go ahead.
**Denys Sedchenko** 17:13 Should I share the screen then?
And we will do… Absolutely. One moment.
**atoulme** 17:20 Exploring.
**Denys Sedchenko** 17:20 Just a second. Where is it? Where is it?
Okay, so basically, I was working on a Fedora Copper POC, Which is based on a different.
Repo from Michele.
So, like… We have OpenTelemetry packaging and we have OpenTelemetry packages.
So I used open telemetry packages.
Fork of Michele, I had to fork it because Copper requires a different way to basically package RPM stuff, not in a way like how they actually branched it initially.
Small disclosure, I had to use CI and assistance because I'm not a… Copper Packaging Guru.
As this is a proof of concept, I skipped an automation. My goal was just to get the packaging work.
Yeah.
So basically there is a, repo that you can actually try on Fedora or any Red Hat distro.
That ships… Basically, open telemetry method package.
But it has… Other packages under the hood.
So, builds are successful.
And also left some instructions how to actually test it or install it.
**Michele Mancioppi** 18:59 So, you fucked off the, early implementation stages of the packages before I had way too much fun with, go to create tests and packages and, test containers and so on.
**Denys Sedchenko** 19:14 Yeah, I assume it also used, Zig build system.
Your… your repository.
**Michele Mancioppi** 19:24 No, I, yes, yes, but, I.
The, the current one actually gets the injector from, from releases.
**Denys Sedchenko** 19:33 Yeah, so it might be a bit out of date, but this is just a proof of concept to show that actually it works.
The build pro like the building and actually distribution happens on the copper side. So like I basically, I just had to, like there have a CLI, I basically have to use a CLI just to trigger the build and I had to specify from what repo it needs to be built. That's why I had to actually create the fork with my changes.
**Michele Mancioppi** 20:07 So, if, I mean, we're going to merge PR18 in a… In a few minutes.
The, what do you think is… Would it take to, To try and port the, The slightly changed way of building packages.
**Denys Sedchenko** 20:29 Mmm.
If approach didn't change dramatically, It shouldn't be really a problem.
**Michele Mancioppi** 20:37 It did change a bit. It went from FPM with a bunch of shell scripts to an FPM in Go.
So there is now GO in the toolchain. There's also test containers.
for testing stuff, although, if I recall correctly, when you forked off, I had a bunch of Docker commands in Shell.
So… I hope it's not, it's not too difficult.
**Denys Sedchenko** 21:04 Mmhm.
My concern is basically… that, Copper is using different ways to actually build and package stuff, like some Copper-specific tools… So… Like, if we transition to copper.
We might need to switch one approach to build packages to another one.
But… If the… after, like, the PR is merged.
I can create, like, a fork.
with a smaller amount of changes, so, like, it will be easier to distinguish what are your changes and what are my changes, and basically take a look at the div. Right now, the div is quite huge.
But yeah, then I can, like, create a second POC.
I'll show you again.
but please like try to test what I already have at the moment and take a look maybe I missed something.
**Michele Mancioppi** 22:05 I, I think I did try to… to spin up a Red Hat container and pull the packages, and… I had not seen anything weird.
It felt pretty much what I expected.
To be fair, very little of the structure of the packages itself changed.
The, biggest delta is how we build them and test them.
And now we have a Python package with some… So we have a system package with the Python distro.
And we have some Python packages nested in our repo because… the long story of we don't want dependencies, gRPC, blah blah blah, so Diego made, two exporters, one for XDP Protobuf and one for gRPC, and now they live in, in our repo because they're not upstream yet.
**Denys Sedchenko** 23:03 Yeah, actually, I spotted this during code review.
do, like, thanks, first of all, for leaving, README to explain all of the background for that.
A question, like, do you know, like, whether there is some kind of, like, a timeline when the changes will be upstreamed?
To… to our organization.
**Michele Mancioppi** 23:29 They are, so the changes are in our organization.
Believe in open telemetry in our repo.
They are no longer. They're no longer fetching from from Diego's repository.
**Denys Sedchenko** 23:44 Because in the PR, actually, like, the repo with the Python packages was a fork from OpenTelemetry, but it also was a specific branch of a fork.
**Michele Mancioppi** 23:57 Yes, but a couple of days ago, I actually mainlined those packages and their tests into the system packages repo.
**Denys Sedchenko** 24:09 Then can you also then can you please update your PR to actually update at least the read me mentioning from what.
From what place those packages were took.
Like, what?
**Michele Mancioppi** 24:21 That is something that I indeed might have forgotten.
Do you remember where that was?
**Denys Sedchenko** 24:29 Yeah, so basically, in the Python's vendor directory, there is a README that's saying that, like, those packages were obtained from a particular branch of Diego's repository.
**Michele Mancioppi** 24:40 Yes… I mean, that is technically the notice, right?
**atoulme** 24:49 Is it an Apache 2 license, not this thing?
**Denys Sedchenko** 24:52 No, no, it's in a README document. README.
**Michele Mancioppi** 24:56 I am not seeing… So if you let me share the screen, I can… Sure.
**Denys Sedchenko** 25:05 One moment, how do I stop sharing here?
**atoulme** 25:08 No, you didn.
**Denys Sedchenko** 25:09 Sharing is still visible.
**atoulme** 25:12 You, you are, you have, you have stopped sharing.
**Denys Sedchenko** 25:15 Okay.
Disclaimer… I looked at your, like, I did the review on a Tuesday, so maybe you pushed something.
**Michele Mancioppi** 25:26 Yeah, no, no, the packages were originally imported.
Since they are developed… since then, they are developed here. This repository is a source of truth for the chain for the foreseeable future.
**Denys Sedchenko** 25:41 Then can you, like, remove that, remove that, like, that place was that originally were imported from Diego's repo, and just say that, like… Those packages are from a particular place.
**Michele Mancioppi** 25:54 I'm sorry, I do not understand how you want me to change, because what you said sounds like what you already have.
**Denys Sedchenko** 26:02 Okay, never mind.
**Michele Mancioppi** 26:04 No, I'll go. Please. It's explain.
**Denys Sedchenko** 26:08 This sentence probably mislead me. I was thinking that, like, those packages were… are… were from the Diego repo.
I missed the second point that saying like that since then they moved to a different place.
**Michele Mancioppi** 26:23 I am also perfectly fine deleting this paragraph.
**Denys Sedchenko** 26:28 Or maybe like rephrasing it that packages are obtained from the OpenTelemetry Python, from OpenTelemetry's organization.
**Michele Mancioppi** 26:38 I mean, those packages, like what ends up in the things, is built in the CI of this repo.
**Denys Sedchenko** 26:44 Okay.
**Michele Mancioppi** 26:45 We are not fetching the source code anymore.
This, like, the code literally lives here.
That's true.
**Denys Sedchenko** 26:59 Okay.
**Michele Mancioppi** 26:59 You know what? We merge the PR, then. I'm happy to get the PR to fix that.
**Bastian Krol** 27:05 But isn't that a temporary mechanism anyway? I mean, they are not supposed to live in there forever, right?
**Michele Mancioppi** 27:12 Not forever, no. The, the… We should, I mean, we… Diego, maybe you want to talk about it.
**Diego** 27:28 Talk about where it's gonna live.
**Michele Mancioppi** 27:31 Yes.
**Diego** 27:35 sorry, I'm a little bit confused, alright. That's something that we…
**Michele Mancioppi** 27:42 I'll do the talk. Ideally, this we would leave in the Python S And, they, The discussion, as far as I know, is still in the early stages of effectively replacing the OTLP exporter.
Depending on Protobuf and gRPC with these ones, with all dependencies.
The, I don't know how long it's gonna take, but until then, we need these packages and we keep them here.
There is a third exporter that lives in a PR, not from Diego. This is from somebody else for HTML.
**Diego** 28:25 Lucas.
**Michele Mancioppi** 28:26 By Lucas, yeah.
That is also not merged, so that there were, like, entire CISO PRs, and I think the last one is still, is still to be merged.
When that PR merges and they cut the first releases, then we add support to our packages for in Python for, HTTP JSON as an encoding to… by… by adding to the, to the package the… that would be exported.
For Python, we will also need to keep an eye on a refactoring upstream, where Mike, from the, the Python sake wants to.
Move the configuration.
package, the Firebase configuration, to a separate package, and then when that version is cut, we need to effectively add another entry to the requirements of TXT when we upgrade to the later version of Python.
Did I forget anything, Diego?
**Diego** 29:31 Only that this exporter is now implemented in Python, so its performance is inferior.
which is, something we need to work on. We can try and implement it again using T, Ross, or something else.
Besides that, it's, it's equivalent.
**Michele Mancioppi** 29:58 I would argue that there is a lot of stuff going on in Python. For example, Alex Bolton has this idea of… Replacing the internals of the SDK with the C++ SDK.
And, I don't like that idea very much.
But also gives me pause about thinking of re-implementing another set of exporters, this time with a little more C.
I would keep it until there is some clarity on whether the prototype of Alex lands.
I would keep it like this.
First one.
**atoulme** 30:38 I think Alex went all the way to a talk about that, didn't he? I think it's been a little while since he first attempt.
Is this you?
**Michele Mancioppi** 30:45 No, it was brought up in the maintainer SIG recently.
**atoulme** 30:51 Okay.
**Michele Mancioppi** 30:52 In the Montana calls recently, yeah.
**atoulme** 30:55 So this has come up again. Yeah, I think he's got, this isn't just the… He actually has had the code for a while.
In… in… so it's not, like, just talk. There's… there is a real implementation for this, which is cool.
**Diego** 31:09 Yeah, there's a PR. Let me see if I can find it.
**atoulme** 31:14 Oh, thank you.
Yeah, so, it's very exciting.
Okay.
all right.
**Michele Mancioppi** 31:30 So I will give another last round of tests out of.
**atoulme** 31:35 Yeah, sure.
**Michele Mancioppi** 31:35 Absolute paranoia. And then if it works, we cut the first draft release.
And that will publish the repositories to GitHub pages.
Yes, sir. On the same repo, and there are instructions on… there will be instructions on how to to a federal customer. It will need to turn on all the security checks and signatures and stuff, but it will be usable.
**atoulme** 32:04 Okay, this is cool. All right.
We.
Okay.
I think this is worth a blog post. I'm just gonna put that out there, and I'm not trying to put work on anybody. I will… We can open an issue for that, but I think it's worth talking about.
Okay.
And we have 3 minutes left, and I think Ted's gonna item. Let's make sure he gets the time. Sorry, Ted.
**Ted Young** 32:35 Nope.
Just a little piece of administration, just so you don't get surprised by it next week, but we're switching out how we do Zoom. We've had this mishmash of, like, a pile of Zoom accounts, so that we could actually record everything.
And have an archive of the meetings, and it's always been super annoying. And the Linux Foundation is now, coming out with a way to handle Zoom meetings and recordings and everything across… all the different Linux Foundation projects. So, we're gonna be switching to that, so I'll just be updating everything. Just don't be surprised, next week when you go to log in, you're gonna get, like, a Linux Foundation page. If you already have an account, no big deal.
If you don't, it'll ask you to log in as an as a guest or you can make an account. I'd recommend going ahead and making an account. You can just attach it to your Google account. It's not a big deal.
**Michele Mancioppi** 33:37 I would like to open an issue about your issue.
**Ted Young** 33:40 Sure.
**Michele Mancioppi** 33:41 Don't you think that something is missing in between these two?
**Ted Young** 33:46 the… Which one are you looking at?
It's back in Project Triage.
**atoulme** 33:54 Oh.
**Michele Mancioppi** 33:55 Packaging. What is packaging?
**Ted Young** 33:58 Oh, yeah.
I will add it on here, but… But, point is, it's… we're, we're just swapping all this stuff out, just so don't… you know, when you go to… if you have this meeting, and I'll post this in Slack, but it's just some administrative bullshit. If you have this meeting copied onto your calendar, no one's gonna be there, in the… In the old Zoom meeting next week, so… Just an FYI.
**atoulme** 34:29 Alright, well, we'll be trying to watch for that. Thanks, Ted. Yeah. Okay.
All right. One down, one to go. Thanks, Viklav. Thanks, everybody, for the hard work on this. This is really awesome to see it coming through.
We can't go.
**Michele Mancioppi** 34:47 Do you want to spend one last word about the blog post? Because I agree, we should publish this.
**atoulme** 34:52 Yeah, I mean, of course. Look, I mean, it's just, I think this is worth talking about this first draft release, a big deal. We should also use that as a way to kind of set some roadmap. And frankly, one thing that you've been very good about pushing is that we need more people to try things out if we don't.
Then we're going to create some stuff that's not just like people who don't like it. So, I mean, I think I'm stating the obvious when I said that we should write something to communicate to people, let them know this is happening. Especially, and this is why I was just pushing on it this week because I don't want to wait until two weeks before KubeCon before we wake up and say we need to get people to know about this.
I know we're in the dead of summer, and there isn't going to be too many people. Hey, Ted, you got here.
**Ted Young** 35:40 Oh, I was going to say so. Blog post is great. Another underutilized resource is the our YouTube channel. And I think just a short video demoing how to use it and encouraging people to use it would would be an easy thing to slap up there.
**atoulme** 35:58 Oh, okay.
Yeah, yeah, okay. When you said YouTube, I assumed you wanted, like, a live conversation with, like, the end user SIG, but that's too much for me.
**Ted Young** 36:06 No, yeah, I feel like something we… I feel like we don't use our YouTube channel enough, and I think the kind of things that would be helpful to start posting there, like for… not for, like, every little feature, but for something big like this, where we're like, hey, end users, try this thing.
Like, just, like, a simple demo of… of how this works, would be… would be helpful.
If not now, then soon.
**Michele Mancioppi** 36:33 I would also gladly go on those regular shows that the community managers organize to talk about it.
**atoulme** 36:41 Okay, alright, I think all of the above, then. Okay.
Yeah, I mean, it's time, it's time to make those about it.
Yep.
**Ted Young** 36:51 Do it.
**atoulme** 36:53 Maybe.
Yeah, I don't know. I can, I can say, let's get that draft release out, then I think you can do… we can do blog posts, videos, and appearance on End User SIG, I think. Mikkel, if you want to cover that one, the latter one, the End User SIG, live conference discussion type thing, I think that's fine.
I can take care of recording a video with the draft release, and this way I can also, like, we can have a validation. It works from someone also, like, from that point of view. And then… I am happy to draft the… I think the blog post could just be, enclosing the YouTube video.
that's what it's about. It's like, here's a big announcement, here it is in action, now go try it out, right? CTA is pretty cool, and simple.
You should try this out today. Tell us what you think. And here's where you find the issues.
**Ted Young** 37:56 100%.
**atoulme** 38:05 Okay.
Anybody else? Anything else? We're good?
We… We're trying to cut over to the injector sig, so we gotta go.
**Michele Mancioppi** 38:17 All right.
**Bastian Krol** 38:17 Of all, right?
**Michele Mancioppi** 38:18 Exactly. Folks, we merged something that is massive, and I don't feel the hype.
**atoulme** 38:24 That's why we have to, we're gonna have to.
**Ted Young** 38:26 Tired.
**Michele Mancioppi** 38:29 I know it's hot like hell, but please hype.
**Ted Young** 38:32 Bye.
**Michele Mancioppi** 38:32 They've been working months for this.
**atoulme** 38:35 Yeah, that's true.
**Ted Young** 38:37 It's exciting, it is.
**Michele Mancioppi** 38:39 All right.
Bye, folks.
**Bastian Krol** 38:42 Bye-bye.

SIG: Security Governance SIG
Date: 2026-05-11
Duration: 38 minutes
Zoom Recording URL: https://zoom.us/rec/share/almVDRKGrRuUX1EfWxQ-kF7IVpJ3lAqtzE7lRrHhYI3U5sJYUNWxwtQk47t_zt04.0QmZEnQtFSA6hA88
============================================================

## Zoom Recording Transcript

**Jeremy Corley (Microsoft)** 01:08 Hey, hello, Ned.
**Nick Moore** 01:10 Hello, Jeremy!
How's it going?
**Jeremy Corley (Microsoft)** 01:17 Oh, Sorry, I can't hear you, one sec.
**Nick Moore** 01:21 Sorry, it might be me.
Let me check.
**Ted Young** 01:27 Hello?
**Nick Moore** 01:28 Ed?
How are you doing?
**Ted Young** 01:30 Good! See you, Nick.
Jeremy, nice to meet you. I don't think we've met before.
**Nick Moore** 01:37 I think Jeremy's having possibly audio issues.
**Ted Young** 01:40 A bunch of stuff.
**Nick Moore** 01:40 me, but I think I'm okay.
**Ted Young** 01:42 I can hear you, so… Probably fine.
**Nick Moore** 01:48 Makes a change.
**Jeremy Corley (Microsoft)** 02:08 Hey, hello, can you hear me?
**Ted Young** 02:10 Yep.
**Nick Moore** 02:10 I can hear you.
**Jeremy Corley (Microsoft)** 02:12 Oh, okay, great. Alright.
For some reason, I lost my audio there for a second.
Cool.
My video is also up.
There we go.
Hey, hello, So, let's see here, So, Let's see, so, obviously some new faces today… Going to check and see what we have.
Under the, Under the, issues… Awesome, meet you again.
Sign-in is taking a second.
**Ted Young** 03:24 Fair thing.
**Jeremy Corley (Microsoft)** 03:44 Let me share my screen.
Let's see… Cool. Alright, so it… We don't have… This is a… this pull request has been around for a little bit, I think I need to check with Riley on… Where he wants to take this.
This is some new recommendations on… Vulnerability management for maintainers, it's been… Open for a bit. And… several comments on, but I haven't seen what he wants to do with it, so I'll circle back with Riley and see if there's anything there, so… That's the only, open pull requests we've had.
And I'm not gonna go through all the issues and such, but, there's some… recommendations that come in, we can go through those. But, since you guys have joined, I don't know if there's some, anything that you guys want to talk about. Obviously, if you… feel free to introduce yourselves. I'm… I'm Jeremy Corley, I've worked at Microsoft under Riley, and, just… I'm one of the maintainers on the security SIG, Keeping that ball rolling, but how about you folks? Nick, did you want to start?
**Nick Moore** 05:31 Yeah, I'll go for it. So, I am Nick, and I am an employee at Grafana, with Ted.
And I've been at Grafana for three and a half years. I joined as a security engineer. I've moved my way all the way through. I'm currently a principal security engineer at Grafana.
Our team is very… traditionally has been quite inward-focused. We are very focused on securing Grafana's infrastructure and whatnot, but we've always had a desire to move more outside that and actually work to help improve the security of other areas.
I've got quite a broad range of security experience, I've worked on a lot of CICD security issues, I've, do a lot of detection and response engineering, do ins… fonts leading.
quite a mixture, to be honest. And code security and all the things in between, they all come up occasionally. Constantly worrying about third-party CVs and what we do about them, and how much we care, especially when they can't be triggered. But yes, so that's my background, yeah, and, Ted has, Ted reached out to me a couple of days ago and said about, actually, the SIG security Was looking for more contributors, and I've been wanting to get more involved. I had some previous involvement, I've… I worked a bit with the SEMConv.
So I know Trask, I know, Luke Miller, if you know Luke Miller, around when, I believe Splunk was introducing the semantic conventions, around security, I kind of got a little bit there. There's been a bit of back and forth as to how they actually take that forward, and I think there's a kind of being consensus now they're moving towards the OCSF-style, conventions instead.
kind of have said I could potentially get involved with that as well, but I also said the SIG security is also very relevant to my background and what I do, so I feel like I probably could offer help and Effort, if nothing else. There as well.
**Jeremy Corley (Microsoft)** 07:29 Yeah, excellent.
**Ted Young** 07:30 Yeah.
**Jeremy Corley (Microsoft)** 07:31 Yeah, that's… that's fantastic. Great.
Ted? Yeah.
**Ted Young** 07:36 Yeah, so I'm Ted, I'm on the governance committee, and I also work at Grafana Labs, as Nick said, and, I was talking to Riley, you know, just looking at different ways we can help shore up OpenTelemetry, and, you know, SIG security, you know, seemed like a one-two combo of, like, it's mostly Microsoft holding it down, and, you know, we always… Preferred it to get more, you know, of a… just, reducing that failure mode by having, you know, more organizations involved in various SIGs, so this was one, you know, I had identified as, like, hmm, it would be nice if we had more people paying attention to this. And then also talking to Riley, and it sounds like, you know, the… There's, like, a need to kind of, like, improve our recommendations for maintainers, also, you know, improve our tracking of, like, whether or not, you know, those recommendations are being followed, and then just, like, the deluge of… you know, increase in reporting and things like that, powered by kind of, like, AI, you know, nonsense. Like, just a lot more noise, especially, even in, like, the past month.
like, the noise volume has increased. So just having more hands on deck and just more… more security engineers involved just to deal with With the backlog of stuff.
So it seemed like a great, great way for us to maybe help, OpenTelemetry, and since… you know, more and more of our users, you know, and our customers at Grafana are coming in using, you know, vanilla open telemetry in some form, right? Like, working upstream is very helpful to us, because we have, you know, like, many orgs, like, we have some of our stuff gated where we have our own way of, like, doing our own releases and things like that, you know, if we We want to front-run any kind of problems, but… more and more of our users are just like, yeah, we're already running OTEL, right? So that, you know, we want upstream security to be as smooth and fast and responsive as possible, because that's just where our users are, so… So that's… that's our interest in… in joining.
**Jeremy Corley (Microsoft)** 09:59 Yeah, excellent.
**Ted Young** 10:01 Yeah.
**Jeremy Corley (Microsoft)** 10:03 Yeah.
**Ted Young** 10:03 Excellent. That's mostly what we're.
**Jeremy Corley (Microsoft)** 10:04 Yeah, so.
**Ted Young** 10:05 How do we plug in? Like, what's the best way for us to kind of get started on that front?
**Jeremy Corley (Microsoft)** 10:12 Right, right, yeah, and it's been sort of a challenge. So, Yeah, on my side, I've, I've, I actually had my 20th anniversary at Microsoft a couple days ago, but, and I've… I've had sort of a security focus, yeah, Yeah, thanks.
And… and, it's been… And I've been doing security, Microsoft's actually the company number 8 for me to make me seem even older. And… the… I did a lot of, like, DRM stuff and things like that, before Microsoft, and then, coming here, I had to step through Windows mobile phone and all that kind of stuff, but, but I got into a lot of, my… my background is honestly, like, in, like, PKI and a lot of those areas, and the… Riley on… on… now that I'm in observability with Riley, a lot of the things that we're… we're focused on is, the sort of supply chain security and things like that, right? Because it's one thing to get your transport security and all that kind of stuff right, but the, that's sort of almost a well-known, well-understood area, but, you know, a lot of these things, and particularly in open source, where you're kind of… asking people, hey, you've got this security problem, would… please, maintainers, would you mind going and fixing that, right? It's this weird, how do you… How do you set the level of importance in that, and… you know, make sure it's… and yeah, we're ending up in a world where, discovery is almost not the problem. I mean, it is a problem, as you were saying, there's AI slot coming in and giving you a lot of noise versus signal, But then there's just sort of, like, you know, how do you, you know, take care of some of those things? So it's kind of a crazy, crazy thing. And yeah, you know, the challenge we have with the security SIG is that in some ways, the most we can do in the chairs that we sit in, in that sense, is just make recommendations.
And, you know, we try to make those up through, you know, the TC and the GC and all that kind of stuff, and, you know, some rules get set, but it's still a really difficult, you know, piece to deal with, so, So, yeah, I mean, you know, the more, sort of, you know, people, particularly from different perspectives, again, yeah, with Ryan and I, you know, both being from Microsoft or whatever, it feels very one-sided in that sense, so… So that's great.
Yeah. Oh, and I see, Damien just joined, Hey, hey Damien, we're, we're just going around sort of doing a little bit of introductions, because there's actually not much on the actual agenda at the moment. Did you have, do you want to… Same thing, or did you have either issues or something you wanted to introduce yourself with?
**Damian Ogedengbe** 13:24 Hello, Jeremy.
I'm just here to learn from.
**Jeremy Corley (Microsoft)** 13:28 low.
**Damian Ogedengbe** 13:29 Your teams like you.
I'm a site reliability engineer, and I'm… I'm big on observability with AI.
My current, stock is, Signals.
being integrated with Claude to make observability easy and all of that, so I'm just here to learn.
From seniors like you. Thank you.
**Ted Young** 13:56 Me too.
**Jeremy Corley (Microsoft)** 13:58 Open.
Yet.
Alright.
**Ted Young** 14:03 Quick point of process, just so you know, for me, I can only stay for the first half of the meeting, then I've got to run to the next SIG.
**Jeremy Corley (Microsoft)** 14:11 Sure.
**Ted Young** 14:12 That I'm involved with, but I'm mostly here to kind of introduce Nick, and… And just kind of get a sense for how we can… you know, like, what… where are the areas where just, like, more hands on deck would be helpful, and where are the areas where we're… we have, like, genuine question marks, where it's like, we need to figure something out, and we don't have an answer yet. So I guess, if you don't have other agenda.
**Jeremy Corley (Microsoft)** 14:38 Right, right.
**Ted Young** 14:39 To get, kind of, like, an overview on those two fronts.
**Jeremy Corley (Microsoft)** 14:45 Yeah, sure. Go back to sharing my screen real quick.
Let's see, probably… the most… Interesting area here… So, under, in the security SIG, under the code area there, we have, you know, obviously there's the charter, and one of the things that we created a little while ago, you know, was all of our security response stuff.
And this is fairly, you know, standard, standard bits. And our… I'm trying to remember now, you know, we put some rules about how to deal with a CVE and all these kind of things, under, you know, under those elements. And it's actually, something I wanted to circle around with Riley. I mean, for the last few months, we've actually just been, You know, people have been putting in, some issues and some CVDs and things like that, but there were some, different issues that they want to deal with, in there, and we've kind of been responsive to that. But we've been having conversations about, yeah, how do we deal with this, you know, the supply chain problem? How do we, encourage maintainers to, you know, actually pick these up, because we've kind of got the set of rules in here of, like, you know, how we believe you know, something should come in, somebody… we're instructing users to create an advisory, and then maintainers, you know, should go in and pick those up and deal with those within a reasonable amount of time.
And, you know, it's very clear when, you know, looking at, like, how quickly those get taken care of and the various things that, you know, they, you know, there's a backlog in, you know, many of the different repos on those issues.
And so, I think… It's… it's just something we haven't tackled, you know, probably in the last 6 months or whatever. We've… we haven't really looked deeply at that part, but that is something that we need to, you know, kind of look into and figure out, you know.
how… what kind of process can we come up with? And, you know, yeah, what do we do about a repo that is… that has got, you know, a backlog of however many issues, or whatever? You know, what's… what's the, you know, what's the deal there? Do we… Have to start making rules about, like, okay.
you know, you can't make feature releases if you've got, you know, X number of, you know, things hanging out that are this old, or whatever it is, right? Like, you know, and is that productive, or, you know, is that a problem? You know, however… you know, we can do that. And some of this is going to be recommendations that we would make up to, you know, the TC or GCE, you know, kind of stuff, you know, those sorts of things.
So, But it's things we've only sort of vaguely talked about, but we haven't really, you know, dug into, so… That's… that's a little.
**Ted Young** 18:13 Nice.
Yeah, that's definitely helpful. I mean, SIG Health is something we care about, you know, on the GC. We try to have a liaison meet with the different SIGs, but it's still possible for a SIG to just get underwater, you know? And, it… So I can see this as one of the ways we find out.
Right? That, you know, a SIG is, like, under… has, like, the maintainer hour, you know, availability has, like, dipped.
you know, very low, or even to zero, because, you know, what's on paper doesn't necessarily match reality that month, or that quarter. Right.
Right. We're doing some cleanup right now, actually, to kind of, we have done an automated sweep just of, like, looking at activity, like, maintainer activity, for example, and… and, like, automated a request to move people to emeritus if it looked like they just… aren't active anymore, because that… that just happens, and then no one updates the roles, so we're trying to… to get a more accurate dial on, like, like, what is the actual maintainer. Jesus, how about that.
Sorry, you guys still there? Jesus.
**Jeremy Corley (Microsoft)** 19:37 Yep. Yep.
**Ted Young** 19:38 Man, speaking of bugs, like, fuckin' Telegram. Just the amount of… I get coming in through that.
but, yeah, so that's… that's… that's the thing we're trying to… to figure out, but I… we can… I… security's one of the areas where I have concerns that… you know, how do we identify that a SIG may not be able to keep up or respond effectively?
to a bug, and, like, how do we… I don't want to say, like, have a tiger team or something like that, but it's like, if we do get into this scenario where we've, like, wow, there's a problem somewhere, like, you know, some kind of serious CVE, like, how do we make sure it gets patched, and if it seems like it's not getting Patch for some reason, like, what do we… what is the actual next step there?
**Jeremy Corley (Microsoft)** 20:34 Right.
**Ted Young** 20:35 The area where I, by the way, have more concerns about the… I mean, I don't… it's, like, harder for, I think.
the amount of code is smaller, but the area is more vast, is contribib. In general, I'm trying to figure out, for instrumentation in particular, how do we… completely redo how we're approaching that, because so far it's been sort of, like, community-managed, you know, contrib, but, like.
OpenTelemetry just doesn't function without the instrumentation, right? So it's… there's a bit of a mismatch there, where we're saying, like, these are community-managed things, but actually, like… like, everyone does have to ship at least a subset of this stuff.
**Jeremy Corley (Microsoft)** 21:23 Right.
**Ted Young** 21:23 I don't know what the… in the past, what the security situation has looked like for contribib repos, like instrumentation, but that's an area where I feel like.
**Jeremy Corley (Microsoft)** 21:35 Yeah.
**Ted Young** 21:37 like, a bigger potential set of problems there, because…
**Jeremy Corley (Microsoft)** 21:42 Right.
**Ted Young** 21:42 It's even stronger between, like, the amount of potential maintainer availability versus the surface area.
**Jeremy Corley (Microsoft)** 21:51 Yeah, and the big issue we have there… so, a lot of the stuff, like, I did a bunch of initial groundwork when I was putting together the, you know, how we would respond to a lot of the issues and stuff, and when you go out and you start looking at other open source projects. Like, Kubernetes was one that, you know, a bunch of… we stole a bunch of the text from and everything in some of the process. But, you know, they both have more of a formal… like, they have a security response committee that, you know, actually you know, you know, they have a reputation and all kinds of other things, and they're very hands-on. But they also have, like, essentially one release, and kind of one repo, essentially, not the dozens and dozens and dozens of things we have. And then.
not only that, like you say, Contrib Repo is one repo, but it's, you know, this massive… multi-headed dragon kind of thing, and, you know, that has one release, but a zillion people, you know, sticking random things in there. And so, Yeah, it's kind of a nightmare from a, you know, that perspective, and, because, you know, with some of the other repos, you can say, oh, okay, you know, your release, you know, we're gonna… block you, or call you deprecated, or do something to you to say, you know, you're unsafe, and you need to get in a better state, and, you know, we're not going to give you an official release, you know, or something, you know, you could do that sort of on one repo, but yeah, like, contrib is not something… you know, you're gonna say, oh, because, you know, one exporter is messed up, do you block the entire everything from going out, right? Like, it just doesn't make any sense. So, yeah, that's a really difficult, you know, problem there.
And… and yeah, it's kind of crazy because, you know, for a lot of customers, if they, you know, do a, okay, I'm gonna just grab the, you know, everything install of OTEL, and then I just run a scanner on it, right? And, you know, they're not going to care that the security bug is in some random exporter that they don't really use, it's just, oh, my company policy says if this thing doesn't come up green, I can't put it in the production, you know? And so, you know, You know, that's… it's kind of a mess from that standpoint.
So, yes.
**Ted Young** 24:18 That was actually the third… that's a good point. That was the third thing when I was talking to Riley about this that he brought up, is, like, more and more, we have customers and end users running their own scanners, or, you know, they're working with… with Kratos or Palantir or somebody, like… like, there's more and more… You know, end users care about supply chain stuff, so they're running their own scans, and then how… if there's a mismatch between, like, what we think is important versus what their scanner is reporting, like, how do we… How do we res… keep track of those things coming in, and how do we, like.
Respond to them, you know, to be like.
Don't worry about that. Official… you can… here's the receipt we can give you to say you can officially not worry about this thing that your scanner is telling you about.
Why should you trust us versus your scanner, right? If we're saying that's not important, and your scanner's just saying it's red, like, how… other than just being like, trust me, bro, what… To… to improve that situation.
**Jeremy Corley (Microsoft)** 25:27 Yes, yes, yes, absolutely.
**Nick Moore** 25:31 languages you can reserve on things like GoVonCheck and things like that. The, those are… relatively precise tools that you can use to do that kind of assertion around it. I think it's fair to say there are sadly not that many languages that do feature tools as high quality as Govonchek, sadly.
But yeah, no, that is, false positives from… Static scanners are the bane of my life.
**Ted Young** 26:05 Yeah.
**Jeremy Corley (Microsoft)** 26:06 Don'.
**Ted Young** 26:07 I've got 4 minutes left before I have to run. I'm wondering what… in terms of getting, like, Nick set up, and everything, what are next steps there? What should we do?
**Jeremy Corley (Microsoft)** 26:17 Yeah, I, I, I have to talk to O'Reilly, because I think, I, I, there's… there's a short little process, I think, where, there's a submission of an issue and that sort of thing. I haven't done it in a while, so, and Riley's far more deeply involved in the process side of that stuff than I am, so, so, I don't know if you guys are already chatting with him, you may want to ping him and say, hey, you know, can you put me? Because he always knows exactly where to look in the docs to find that exact process. And then, yeah, and then, you know, we can set that, set that up as well.
**Ted Young** 27:00 them on… probably just through SIG Security on that channel, just to keep it transparent.
**Jeremy Corley (Microsoft)** 27:04 Yeah.
**Ted Young** 27:05 And .
**Jeremy Corley (Microsoft)** 27:06 Yeah, yeah.
**Ted Young** 27:07 Nick, are you a community member? That's, that's, like, kind of the first step.
**Nick Moore** 27:11 Yeah, I can't remember if I am, actually, because I started on that process, and I was doing it as part of SEMCOMF, and I'm not sure that actually got finalized in, so I think, I was talking to someone about it in SEMConf. I'm not sure if… where it went, because of the shift to OCSF, so I should make sure that happens if I'm not.
**Ted Young** 27:31 Yeah, yeah, that's the first basic security check is becoming an org member. That's through the community repo, but that is a good question, like, what's the easiest way to tell if you're an org member or not? I think that's probably… Let's see if I can tell… people.
I think it just means you show up in the people list.
Nick, what's your, what's your GitHub handle?
**Nick Moore** 27:57 K-E-L-N-A-G-E.
**Ted Young** 28:00 AVL…
**Nick Moore** 28:01 KEL, sorry, I'll send it in, chat, just to be clear.
There I am.
**Ted Young** 28:09 Okay.
**Jeremy Corley (Microsoft)** 28:10 Yeah, I think if you look at your profile in GitHub, under organizations, you should see them.
**Nick Moore** 28:15 Oh, yeah, that's a good way of checking, actually.
**Ted Young** 28:17 And I'm not seeing you as an org.
**Nick Moore** 28:19 No, I don't think I am. Yeah, I think that's…
**Ted Young** 28:21 step is in the community repo. You want to go to the community repo and become an org member.
**Jeremy Corley (Microsoft)** 28:29 Yeah.
**Ted Young** 28:30 And that needs, like, a second… someone outside of Brafana to vouch for you, so maybe that can be you, Jeremy.
**Jeremy Corley (Microsoft)** 28:39 Yep, good.
**Ted Young** 28:43 Yeah. This is one of the things I wonder if we want to start leaning on more, but this is more of, like, for maintainers to deal with the noise.
of, like… More and more, there needs to be a, like, is this a human?
that I'm talking to, has this person Has there been any form of, like, trust network?
you know.
**Jeremy Corley (Microsoft)** 29:05 Yes. Nick, you need to put your hand in front of your face like this.
Yeah, there we go.
**Nick Moore** 29:12 closed 5 on each five… six, no, yeah.
**Jeremy Corley (Microsoft)** 29:17 Excellent.
**Nick Moore** 29:19 My family is Welsh, and if you know anything about the… Exactly, yeah.
I make jokes about the number of fingers on Welsh people, but I'm okay, I'm good.
**Jeremy Corley (Microsoft)** 29:30 Great.
**Ted Young** 29:32 Okay, cool. Well, I've got to run, but this is awesome. I'll follow up with you all on Slack about next steps for getting Nick set up.
Have a good one!
**Jeremy Corley (Microsoft)** 29:43 Okay.
All right, thanks, Ted. Yeah, honestly, I don't know that we have, that much more unless, Nick, you or Damon, you had anything you wanted to talk about?
**Nick Moore** 29:54 Ted mentioned about potentially there being interest in… With the volume of submissions.
Or vulnerabilities, and… bug bounties, or… they're not bug bounties, obviously, in this context, but, that volume, about potentially interest in using AI to validate, at least to some extent, whether or not a vulnerability is real. What's the, what were you thinking in that… were you… I don't know if you were involved in that conversation or not, but is that something that was, Any thoughts around planning around it, or is it…
**Jeremy Corley (Microsoft)** 30:33 Right, right, Okay, I need to separate Microsoft Brain from, OTEL Brain.
**Nick Moore** 30:40 Absolutely.
**Jeremy Corley (Microsoft)** 30:40 There's, there's… Of course. It's something we're, we're hot on internally. So, in O-Tel, honestly, I have not heard anything about that directly. Now, again, I haven't talked with Riley about the Security 6 stuff in a couple of weeks, so I don't know if there's something that has popped up with that, but obviously it would be something that we'd be really interested in figuring out.
And part of the issue there is our limitation with the, with GitHub itself, about… what kind of triggering and stuff we can get, and how we can wire that in. I mean, obviously, it has some of its own AI tooling and its own triggering and all that sort of stuff.
And I'm certainly not an expert on GitHub on its own, so, you know, we'd have to do some digging around and see what we can trigger and how we can get it to run in internal.
To its own, you know, processes and all that kind of stuff. So, yeah, so I think that would be fantastic if we could try to get, you know, some of that, going, or… You know, even for some of the advisories, if, if there's a way to get GitHub to kick something off that takes a look at it and gives it some kind of, you know, quality grade or something, so that at least the maintainer, when he comes in and goes, oh, oh, this is a, you know, quality 5 thing, oh, that's probably okay, this is a quality 1 thing, okay, you know, this might be garbage and, you know.
You know, that kind of stuff, but Yeah, I think that would be… Really interesting if we could pull some of that off.
Because, yeah, I know there's certainly, even just for, people… firing off, not even advisories, but even, like, pull requests and things like that. You know, I've heard some complaints that the maintainers are getting a, you know, a lot of people are just like, hey, I had my AI tool run through the repo and find a bunch of random stuff, here's a pull request with my AI, you know, output.
**Nick Moore** 32:50 Yep.
**Jeremy Corley (Microsoft)** 32:50 Yeah.
So…
**Nick Moore** 32:53 someone where I had a chain today where they had found a four-stage chain that they found entirely with AI, and the first one was complete rubbish, and then this next one… it's like, well… okay.
**Jeremy Corley (Microsoft)** 33:05 Yeah, yeah, exactly, exactly. Yeah, so definitely a problem.
Cool, cool, yeah. So, yeah, I mean, honestly, at this point, we have a lot more problems than we have, sort of solid solutions. We've, you know, to be honest, probably for the last I'd say since the beginning of the year or so, we haven't been putting a lot of direct effort into the security SIG. You probably can see from the notes down below that, you know, I've showed up, nothing's happened, and all that sort of stuff.
And, I've been taking my cue from Riley because he's on the TC, so as they find things that are important to them and all that kind of stuff, I've been, been reactive on that, so… But yeah, definitely if we can spin things up and, you know, get more on it, that'd be great.
**Nick Moore** 34:02 That seems… Yeah, very reasonable, and yeah, very happy to help with that.
Yeah, so that repo, the list of the issues in there, those are kind of like… general ideas that people have had. Probably not much work towards, is that fair? Or is it…
**Jeremy Corley (Microsoft)** 34:23 Yeah, I think that, Some of them, Yeah, are just general suggestions that people have made, and there's a couple of them where we've had a little bit of back and forth and got left, In a not-really-sure state.
Others are, Yeah, I think there's some of these that are left open that we've actually decided on. Like, I'm looking at… there's, like, a CLO monitor, and somebody's suggesting we use it, and Trask is, oh, CNCF is moving towards, you know, this other tool.
I suggest we focus our efforts there, and we just haven't really closed the issue. I think there's probably a little bit of cleanup and stuff we can do on some of those. Cool.
So, yeah.
**Nick Moore** 35:16 Interesting, open SSS.
Oh, yeah, I see, yeah.
**Jeremy Corley (Microsoft)** 35:24 Yeah, it… yeah.
So, yeah, there's probably, Yep. We could probably go back through and do some of that, you know, maybe… That, that might be a good task.
At our next setup. You know, once we get you, you know, set up into things, then… then maybe on our next thing, we can kind of go through some of this stuff.
I mean, offline, we can probably close some of the low-hanging fruit and things like that.
But, yeah, there might be some other… like I said, there's probably some stale stuff. Honestly, I think a lot of times what happens is, the new interesting issues, the couple bubble to the top, and we kind of take care of those, and then we never get down into the cleaning up the stuff, the older stuff that's been sitting out for a long time.
Yeah, there's… bottom of this first page, it even has stuff, and it's more than a year old, so… yeah.
And yeah, and just, I think for your, sort of background a little bit, I was just looking at… I think I spun up on this about a year ago, and then we put together some of the guidelines and stuff over the first, you know, few months, through the end of last year, and then really, that's… that's all we've done, and before I came back onto this, the security SIG kind of was, Was just kind of empty, basically, for… You know, a year before that, so it kind of goes in these waves, where we… we do a little bit of work, and… and You know, So, yeah, we're just trying to keep it rolling, I guess.
**Nick Moore** 37:13 Yeah, that makes sense.
Definitely.
Sounds very reasonable to me.
**Jeremy Corley (Microsoft)** 37:21 Alright, But, yeah, you know, feel free to take a look through things, and yeah, you know, send, send stuff through the, through the Slack channel. Are you on the Slack on the.
**Nick Moore** 37:36 I am, yes, I have now… I was in the semantic commons, and I'm now in… yes, I am here. Yes.
**Jeremy Corley (Microsoft)** 37:43 Okay, excellent.
Excellent. Okay.
**Nick Moore** 37:50 What?
I was just looking through… I've just got the information about membership on the Contutor Guide, so I need to… there needs to be a PR and things like that, requesting group PR reviews.
Deep understanding, responsibility, yep.
Okay, so… Excellent, so yeah, so I just… so, need nomination, Need an approval. Fantastic. Okay.
Right, I think that's all pretty clear to me, I've gotten the information about it, so that's all useful, thank you.
**Jeremy Corley (Microsoft)** 38:30 Okay, great. Excellent.
All right, all right, well, we'll see you around, Nick, and nice meeting you. All right. All right, bye-bye.
**Nick Moore** 38:40 Cheers, Jeremy. Bye.

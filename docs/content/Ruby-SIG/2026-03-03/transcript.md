SIG: Ruby SIG
Date: 2026-03-03
Duration: 66 minutes
============================================================

## Zoom Recording Transcript

Ariel @arielvalentin (ATX, USA) 00:03:31 Hello!
Hannah Ramadan 00:03:37 There we go. Hey, everyone.
Ariel @arielvalentin (ATX, USA) 00:03:44 Aruna, I think I've seen you on this call before. Can you remind me?
You know, tell me about yourself, and or brings you to the… to the seat?
Globe?
It looks like you're unmuted, but I can't.
Sweet.
Arjun Rajappa 00:04:19 Sorry, sorry for that. The mic was… I selected a different mic.
Ariel @arielvalentin (ATX, USA) 00:04:24 No problem, no problem.
Arjun Rajappa 00:04:27 So, hey, hey. So, I work with IBM Instana, so…
Ariel @arielvalentin (ATX, USA) 00:04:32 Oh, okay.
Arjun Rajappa 00:04:35 I've been participating in meetings on and off, and tried to contribute to the repositories.
But yeah, it's quite late for me, it's 11.30 PM, so that is where.
Ariel @arielvalentin (ATX, USA) 00:04:46 Oh, no.
Thank you so much for, like, coming here so late.
I will try not to, tip you up much later.
Arjun Rajappa 00:04:59 Yeah.
Ariel @arielvalentin (ATX, USA) 00:05:00 I'm sure you've heard my voice on here, but I've been kind of…
in and out, I'm on the observability team at GitHub.
And Honda is on, she's, engineer in New Relic.
And so, I think that it's just gonna be us today.
Because I didn't hear back from anybody else in the channel of them joining.
And… I think we can jump into some of these…
Now, if that's alright with everyone, I'm gonna…
Close out some of my tabs here, because I'm on my laptop in my backyard.
I mean, myself, I'm not very interested in You're in boards.
Let's see… all this other… Yeah. Pretty nice out here in Austin, Texas.
And I'm gonna close out anything that would incriminate me.
Hmm…
Alright, so it should be sharing Google Chrome.
And to confirm, if I went and opened up another tab.
You all are able to see that tab as well.
Hannah Ramadan 00:06:24 Yes.
Ariel @arielvalentin (ATX, USA) 00:06:25 Okay.
Don't… Don't mind, kind of, all the little widgets that you see there.
Look on GitHub and Strong also.
Don't tell anybody on YouTube, either.
I did not attend the spec sig, but we can go ahead and see what the summary looks like.
Well, just to be sure that we don't highlight anything that we're missing.
On March 3rd here, we've had quite a few folks.
A new release of the spec, which includes the declarative configuration.
So I think that we need to,
Probably set up some tasks around that.
Which is effectively the… YAML config that folks can use to configure the SDK.
Hannah Ramadan 00:07:21 Hmm.
Ariel @arielvalentin (ATX, USA) 00:07:22 There's a little bit of work, for us, considering that a lot of our declarative…
Configurations are code-based.
So…
What is the best way to probably do this stuff? Should I go to, like, a project board here?
And just start typing these things up…
Do I have access to do stuff on this?
Project board.
Can I add something? So if I were to say…
And I don't have a link to this compliance thing, right?
Absolutely.
So, I'm gonna do… I'm just gonna leave a little note for myself here, a declarative configuration, just to see what happens.
And I see the track.
Hannah Ramadan 00:08:14 Okay.
Ariel @arielvalentin (ATX, USA) 00:08:16 So, I feel like this is something that some sort of agent can do, going through these,
Going through these configurations… going through the specification, looking at all of the…
The things that we're not complying with.
And generate project tasks for them.
So that we can get up to date.
I keep saying that over and over again. Nope.
Such as, like… More questions about…
scope attributes… right now, we don't support scope attributes, right, Hannah?
Hannah Ramadan 00:08:53 No, that doesn't feel familiar.
Ariel @arielvalentin (ATX, USA) 00:08:58 So we need to get onto that. The…
SpecSid gave up a status, and they are stabilizing RPC calls.
So I think we're gonna have to go through the same process that we did before.
with what you were doing with the HTTP, stabilization? I don't know.
And get our PC stabilized the same way.
Are we still on track to go, to remove the… the Jeep?
And backwards compatibility?
Keep a food?
Hannah Ramadan 00:09:29 esports.
Yeah, I need to look at… I have an issue with the exact date that… is that 6-month mark?
I don't think we've discussed that, but it should be a pretty easy pull,
Yeah, maybe we can… I can look at, like, where we're at with that. I remember, Arielle, you had, like, some…
I think you had something you wanted to make sure we, like.
there was, like, maybe a potential reason, like, GitHub couldn't upgrade to the newest one if… when we, like, removed the old conventions. Is that still something of concern, or can we…
Ariel @arielvalentin (ATX, USA) 00:10:06 Yeah, that's also a big concern for me, but I think the way that we can mitigate that is by…
having the SLUMA URL be available to us. So I think that there is… there was an open… Cope.
the StableScope feature parity.
Which looks like it paused, work?
But essentially, adding this email URL so that we could say.
Let's add a schema URL to initiation.
And then on… in the collectors, we could look at the schema and say, oh, you're… this is now…
A 1.0 schema, I'm gonna have to downgrade this.
To the pre-1.0 schema, and we can do some processing using this schema processor.
So, that'd be in collector considered.
Here's the schema processor.
So we'd probably use this to say, when I see an instrumentation.
and I see that, you know, there's a particular schema, I'm actually gonna target it to an older version of the schema.
If that makes sense.
Hannah Ramadan 00:11:19 Yeah, that's.
Ariel @arielvalentin (ATX, USA) 00:11:20 I don't have a lot of experience with the performance of the schema processor. We haven't…
We haven't done anything.
to test the performance on our Gateway collectors, where we do a lot of our transformations.
But that's pretty much where… that's pretty much the only strategy I would have in place to try to deal… deal with that, because we don't… we don't have, like, an easy way to say.
Oh, we're gonna rename this attribute now?
Now we're gonna have to have a transition process to say, if…
you, you know, you had span metrics that you were using that had http.method. Well, now, the attribute's name is going to be http.request.method.
So… Go ahead and update all of your monitors and dashboards and all this other stuff.
Like, that's just not feasible in a small time frame.
Hannah Ramadan 00:12:22 Yeah, I think the original plan, or the original, I guess, spec was around needing to support all of those environment variables for 6 months after it's introduced. What we could do is…
keep support for them, but switch the precedence, and have stable conventions emitted by default, and keep those environment variables around a bit longer. If that would be… if that would be helpful, I don't really… I mean, the drawback is those duplicate files, but…
If that would be helpful, I think that could be something.
We could do it in 12.
Ariel @arielvalentin (ATX, USA) 00:13:00 That would be helpful to me if, like, we can switch to, like, stable by default, leave the dupes in place so that people with backwards compatibility have a little time. But,
But again, I'm also not gonna hold the community hostage, just because of us.
Hannah Ramadan 00:13:15 Yeah.
Ariel @arielvalentin (ATX, USA) 00:13:16 You know, there's, like, there… at some point, we have to, like.
We're falling so behind that everybody, you know.
Everybody else should be on one X by now.
on stuff, right? And I don't know.
That's all I gotta say about that, I don't have much more.
Hannah Ramadan 00:13:39 Nice.
Ariel @arielvalentin (ATX, USA) 00:13:40 But I think that this would go a long way in making that possible.
So, I could try to reach out to Robert to see where his head's at.
With this, and see if there's any more… work.
That's missing to make this possible.
So, I'd like to see what we can do about that.
But that's, you know, that's going back to the RPC conventions, let's see here…
you still have that stabilization OSAP, about what the expectations are for stable instrumentations.
I haven't looked at it at all.
As far as the Kubernetes operator is concerned.
I know that Sean, who's not here, has been going a little bit back and forth about getting the…
Ulta operator gen in place.
Got auto insurance each in German.
just not sure… I'm not sure where we're at. I think Vita Dog was expressing some concerns.
in that PR, but I can't talk about what I don't know.
So I'm gonna add another little… so that was that task here, right, on this board.
I'm gonna add another one here, another giraffe.
Which is, oops, I should have added another draft. What's the other draft date? Was, the RPC Stable Conventions, right?
Hannah Ramadan 00:15:08 Which was something that we need to try to file.
Ariel @arielvalentin (ATX, USA) 00:15:12 And then I'm gonna add another one here, which is, you know, instrumentation scope.
Attributes.
Oops, not what I wanted to do.
I want to draft, because I need to flesh these out.
It ain't my first time trying this, so… we'll see how it goes.
I think that covers it for the specs, Sig. I don't know if there's any other questions or concerns there.
I mean, Kayla had this… Semantic Inventions thing that's been open for a while.
And I think I approved it.
And what happened?
Oh, I see.
Okay, well, we're still a little bit behind.
I'm not authorized to put him to the trash, okay, because I am not a…
maintainer in this repo, so I can't merge anything.
But, I guess you just have to wait for somebody to come along and merge. That's about it.
Not much more to add to that.
Were there any other new issues that came up, or PRs outstanding? Let's take a look at those.
Hello!
Let's see, create a date.
I need to… I need to get better at using my own product.
Since last week? That's right, 2 weeks ago?
Okay, nothing new came up? That's cool.
Let's look at open reviews already required.
So, it looks like we have a ton of these, like, you know, Dependabot, and…
Just on and so forth, updates, the renovate Bot updates as well.
But there's not a lot that I could do about resolving those and merging those, right?
But we've got quite a few here. Okay, under you, added this dice roller example here, right?
Arjun Rajappa 00:17:33 Yes.
Ariel @arielvalentin (ATX, USA) 00:17:34 Oh, okay, pretty cool. So then this would be something for us to be able to…
To demonstrate how to use Tell me a little bit more about the GitHub action here.
If you can… Is this to demonstrate how it works using Git of Actions?
Arjun Rajappa 00:17:53 This is just a test, right? It basically tests the application.
Ariel @arielvalentin (ATX, USA) 00:18:00 Gotcha, so that actually will run against the example.
Arjun Rajappa 00:18:04 Yeah.
Ariel @arielvalentin (ATX, USA) 00:18:05 And that's to test the output of the example to make sure that everything is working right. Yeah. Okay.
You know, are we not at the point where we are… we're not on… we don't have any tests for…
Ruby 4? I mean… The remainder on the core repo?
Awww.
Okay, so we'll take a look at this PR a little bit… a little closer, but that's pretty cool. This is gonna be a risk repository. Is there any…
Automatic instrumentation that's being added to this as well, or is it only the core libraries, the core tracers?
Arjun Rajappa 00:18:44 The specification said something like, we need a file where if someone uses that file directly in their app, so we should be able to instrument the app, so I've written that file, that's called as hotel.rp.
Okay. And so…
Ariel @arielvalentin (ATX, USA) 00:19:00 So it'd be preferred to put this in the core repository versus the Contrib one, right?
Arjun Rajappa 00:19:05 Yeah.
Ariel @arielvalentin (ATX, USA) 00:19:06 Okay.
And I'm just kind of perusing this, so I'll take a closer look at this, but this would be great because, also, this effectively makes executable documentation for us, right? Folks who are looking at the examples can use to ensure that that's always working. But thank you for that contribution.
Like I said, I'm not a maintainer on 4, so we'll have to wait for a maintainer to do a review. I could do…
A cursory review, and do approvals and whatnot, and provide any feedback.
Let's see here, so we've got this error, this going on here, where there's some changes that are happening to the OCLP exporters.
Mmm… oh, we need some backwards compatibility, so this looks like a compatibility issue.
where some version of NetHCP is changed.
Oh, are they changing the… there's a change in the base class, then, I guess, huh?
So, what I could do… okay… Okay.
Wait, what is the difference between success and okay now on NetHTTP?
Is there something I'm missing here?
Oops.
That's what was the, HTTP success?
Hannah Ramadan 00:21:00 Yeah, just Google it, it looks like success is, like, all the 200 response. Yeah.
Ariel @arielvalentin (ATX, USA) 00:21:06 So it's the range, as opposed to just the 200, it could… it would include the entire rating, so 201, 204.
Hannah Ramadan 00:21:14 Okay.
Ariel @arielvalentin (ATX, USA) 00:21:15 Is there supposed to be some sort of a behavioral difference there?
Like, why would the… Why would the… the exporter…
Sorry about this. I don't mean to derail the conversation.
You're probably… It's CRP.
Am I derailing the conversation, everybody, or is this alright?
Hannah Ramadan 00:21:44 This is helpful for me, this is new.
Ariel @arielvalentin (ATX, USA) 00:21:49 response… The response body may be full partial failure.
Hannah Ramadan 00:21:55 So, full success would be HTTP200.
Ariel @arielvalentin (ATX, USA) 00:21:59 Partial success would still be a 200, so I don't see why we would be doing a 200 range.
I'll have to go back and take a look at this.
I'm gonna leave a comment, though.
And I'm gonna say… let me see what this person had said in the description. Fixes this.
Hannah Ramadan 00:22:24 Wow.
Ariel @arielvalentin (ATX, USA) 00:22:25 If 204, no contents is returned.
Similar issue in OpenTelemetry Go.
Mmm… Okay, controversy… when I have to get in touch with…
or Damien, and see what's up with that. I can follow up on this one.
Academian… Going to reach out…
And discuss that decision.
To accept two or four… Remo contact… Other responses… Shit.
Okay.
I, did that.
And I'm sorry, oh, actually, I did review required, because there's, like, the pending backlog of all the things in history, but I probably don't want to go back to all the things in history. We should probably limit this.
To… since last week.
Is there a cleaning loop filter?
Hello, no creative filter?
creation date, filter…
Arjun Rajappa 00:24:15 Open, get it. Open.
Ariel @arielvalentin (ATX, USA) 00:24:21 Yeah, why is it not auto-completing for me?
I'm not criticizing my own product, people, just, you know, watch yourselves.
Let's see, we're creating a date.
So when you created? That was, what, like,
reading, it was, like, resting at eager to… minus 7 days or something like that? Did that work? Nope.
That didn't work. Oh, well.
Hannah Ramadan 00:24:56 Oh, that did work, that was a good surgery.
Ariel @arielvalentin (ATX, USA) 00:24:59 Maybe it did, I don't know, yeah, because this is 2 days ago…
Four days ago, last week, so 2 weeks, so I went a little bit too far.
But, we'll try to… we'll try to roll through that.
Is somebody doing Ruby 4 fixes for us? Let's see here…
I saw this and I thought it was an opportunity for a good first-time contributor. I don't think that this is what we wanted, though.
Because of Ostruct being added as a development dependency. Okay, this brings me to another, topic of discussion.
Which is going through the main repo.
And getting out of the gem specs all of the developer dependencies, development dependencies out of these gems, and moving them into GEM files.
And… let me see… where are the gem specs for these?
So I did the same thing in…
I did the same thing in the Contrib repository.
By taking the development dependencies out, we have more control when running appraisals of what versions that are compatible with a specific version of Ruby.
Because when we start pinning them to these minor versions like this, or we pin them to…
Bug fix versions?
If there's a major version change because of a language version change that's not compatible, Bundler becomes very unhappy.
About trying to resolve dependencies.
So it's recommended that we use a gem file for development dependencies instead of
For our per- for our actual production dependencies.
Does that make sense?
And I never got around to dropping support for Ruby 3.2 in this repository, which is another thing to do, so… where was my board? So I think, I'm gonna add something which is, Ruby 3.2 min…
For the core repo.
I'm gonna create a draft here, and I'm gonna say also the cleanup, and this probably shouldn't be in the spec compliance board, but…
Cli… Use gem files instead of… Some spec for… development dependencies.
Core.
No, I didn't mean to do that. Let's do this.
And that's about that.
So…
that completes the… I think what I wanted to look at, at least, for Quora, for, like, looking at Excel from the…
past 7 days.
If we look at… This specific PR, which is the one thing that… We wanted to come through.
What is this… what is Kayla saying?
Oh, okay.
Can I add something? Some code changes in here?
Why did she say… Oh, I see, because we needed to do something…
She needed to do some code changes in order to skip some of these rules. Okay, so we need somebody to go through and review that PR.
Dude.
And then as far as our open QR, open issues… Right?
Yeah, I got my autocomplete here, past 7 days.
I'm gonna try to throw that in some of the PRs as well.
And it's not supported. Man, I've been working on this product so long.
I don't even know what the features are that work in it.
It's crazy.
Okay, we had… Thompson pointed… I'm sorry, James pointed out something… problematic.
Which is that our test suite doesn't work because of the changes of authentication in… MySQL 8.4?
And that also brought up a separate problem.
was…
That we're only testing against a specific version of a database when we can have… when these gems can have compatibility across multiple versions of a database?
So, something I wanted to ask the group was.
Are we concerned about adding instrumentation? Like, should we always be targeting
The latest version of a specific data store for our test suite? Or do we care about, sort of, like, historical test support?
For older versions of us, you know.
of a specific data field. Like, do we want to support multiple versions of MySQL in the test suite with Postgres?
Does that matter to us, or should we always be aiming for the newest version?
Hannah Ramadan 00:30:13 Yeah, I've… it's… it seems like we'd want to test anything we say we support. I don't know how… is it…
Difficult to do?
Ariel @arielvalentin (ATX, USA) 00:30:24 The weird thing is, it's not about us supporting the datastore as much as it is…
The library that we're using That we're instrumenting, that it supports that thing.
Hannah Ramadan 00:30:37 Let me explain.
Ariel @arielvalentin (ATX, USA) 00:30:38 sense?
Hannah Ramadan 00:30:39 Yeah, okay, that makes sense.
Ariel @arielvalentin (ATX, USA) 00:30:41 the thing that I worry about is, like, oh, okay, well, now the Postgres gem
introduces something new for Postgres 15. I'm just making that up, right?
And it's some new methods that get added, but then we don't have coverage that say, like, oh.
Well, they're adding this through method, but it's only for this version of the library and up.
I don't know.
I'm weird, like, I'm just… I'm being weird, I guess.
Maybe I'm overthinking this.
Hannah Ramadan 00:31:18 Was there any, like, discussion on this issue, or did James have an opinion?
Ariel @arielvalentin (ATX, USA) 00:31:24 No, I think that James was just trying to, like… he was, like, depend about, or renovate about, or whatever, trying to update things.
These services to the latest version.
Right? Because, you know, Dependabot wasn't doing that before, but RenovateBot is. So it's trying to update, like, the MySQL container, and all the tests failed.
Which meant the test had to be rewritten, but we couldn't support
you know, running the test in version 8 and 8.4 and whatever.
So we need to, like, rewrite the test in order for them to…
Work correctly, if that makes sense.
And, I think we ran into some problems with just actions just setting up the authentication period.
So,
Like, he's saying that, like, he can't mount init scripts, can't use Unix sockets, and he can't use TLS certificates, which are things that are prevent… like, you know, MySQL having much more strict authentication requirements.
In order for us to be able to run the test suite and actions.
So there's, like, multiple problems, multiple layers of problems hidden in this issue.
description, it doesn't, I don't know if that answers your question, Hana.
I kind of felt like I derailed it a little bit.
Hannah Ramadan 00:32:52 No, that helps. This is, like…
To your point, it looks like multi-issues in one issue.
to think about.
Ariel @arielvalentin (ATX, USA) 00:32:59 Yeah, it's like, issue 1 is… Hey, he tried upgrading… Mysql… But…
It didn't… it's failing because we need to figure out a way to set up authentication for it in GitHub Actions.
Like, that's number one.
And number two is, do we want to support multiple versions of MySQL for the test suite?
Or do we just ca- or do we care just to do the latest every time?
Just, you know, cause… Does it matter for us to have this, like, Test coverage for older versions.
And I guess those are the two… those are two separate questions.
Cancer.
Hannah Ramadan 00:33:55 Yeah, not sure, I… Otel does seem to have a, like.
Like, maybe more of, like, a newer approach, so maybe it's okay just to test the newest versions?
Ariel @arielvalentin (ATX, USA) 00:34:32 Thank you, Pattel, there's an open question.
Ain't… I feel like… We're saying this out loud.
I'm gonna contradict what I told James, which is I think that we should figure out a way to support multiple versions of the data stores.
What?
I don't see any value in it anymore, after saying it out loud.
To you, to, on this call.
Until… Yeah, I don't know, I don't have a compelling argument to keep Supporting Older versions of games.
Not supporting, but rather… adding test coverage that executes against older versions, I think.
Thank you for patiently answering, or, like, responding to my questions. I don't… at any time that you feel… am I pronouncing your name correctly, by the way? I'm sorry.
It, it's that.
Arjun Rajappa 00:35:48 It's Arjun. Arjun.
Ariel @arielvalentin (ATX, USA) 00:35:49 Arjun?
Arjun Rajappa 00:35:50 Arjun?
Yeah.
Ariel @arielvalentin (ATX, USA) 00:35:52 And I'm gonna say it one more time, just to make sure that I'm pronouncing it correctly. Ajun?
Arjun Rajappa 00:35:57 Yeah, Arjun.
Ariel @arielvalentin (ATX, USA) 00:35:59 Oh, okay, the R is pronounced in May, so Arjun.
Arjun Rajappa 00:36:02 Yeah.
Ariel @arielvalentin (ATX, USA) 00:36:03 Alright, just correct me whenever I make a mistake, please.
For the, did you have anything that you might have wanted to add, or any concerns you might have about us?
Executing our test suite just against the latest version of a datastore.
Arjun Rajappa 00:36:22 If that was a library you were asking about, for example, let's say MySQL gem, I would have said, okay, let's just…
At least few versions of,
a few… few previous versions, but when it comes to the actual MySQL server, I don't…
Ariel @arielvalentin (ATX, USA) 00:36:42 Okay.
So it sounds like we have at least some consensus here.
I think I'll provide that feedback then on that issue there. And perhaps I'll encode it in a policy as well?
To say, for instrumentation authors, we only require you to support the most recent version of a datastore.
One library.
Okay, and so another thing that came up after having some discussions is that the All Gem
isn't using appraisals, so we just… so we opened up a task here to add appraisals to the all-instrumentation package.
So that we could have… Sort of, like, appropriate test coverage.
over many different versions of Ruby.
Okay.
So, something that was a bit interesting to me last week, so, it was…
Me trying to understand, like, okay, what are… In general, are…
Oh, no, wait, I'm sorry, I'm jumping ahead.
I should have gone to the pull requests.
I apologize, everybody, for bouncing around here.
We've got some pull requests here around…
these updates, right? These, these renovate by updates, and really, like, James has been, churning these out.
And I haven't had a chance to review these, because I don't know all the implications of adding this stuff.
because I'm not as familiar with RenovateBot as I am with Dependabot. So, I could use some help on taking a look at some of these, if anybody has time.
We have a bunch of these that are… that are open or in draft mode right now, at least looking at the ones that are…
Are ready for review.
Were the reviews required…
I can't… let's see here, do we have a draft as false? No, we don't.
Why don't we have a draft fall filter?
Those are these, you know, those are some things I could use some, some help with. And a couple of things that I added here that I'm waiting on some reviews for.
So, for me.
adding the AWS team as component owners of the AWS resources and X-Ray, which they weren't. They were only…
reviewers of the SDK.
So, I'm expanding the ownership there, and Schwan was actually the…
author of the AWS Resource Detector, so I've added him as well as a component owner on that one.
But I could use some help with reviews on these, so I can get these merged, because I'd like to get the AWS team alerted when
You know, there's a change to those… those libraries.
So that's one of those, and then the next one for me is
So we have, like, a mix of the usage of R-Spec MOCs and mini-test MOCs?
Or many tenth doubles?
And I wanted to converge on one, because,
One of the problems we have is that, as part of one of the RoboCop updates.
It's trying to update to Minitest 6.
But it's not able to.
Update to Mint test 6?
Because… many tests, I had extracted test doubles out of the core gem.
So, it would have to… we'd have to change some cult, you know,
some of the code configurations around, and so I said, well.
In some cases, we're using RSpecMOC, in some cases, we're using Minitest. I said, let's just converge on one.
and only use Minitest whenever… I'm sorry, R-Spec mock whenever possible, as opposed to Minitest.
I just didn't know if that was gonna be controversial, but I could use some feedback on that one.
20.
If that makes sense.
Okay, with silence, I'm gonna move on to this one.
Because, Hannah, you opened this so many weeks ago, and we're still waiting on reviews for you. There's a lot of stuff going on in here.
Hannah Ramadan 00:41:29 It's a very large PR, and I'm actually really interested in what you had put on the agenda in terms of AI.
Because this… this was generated mostly with AI, so I… I don't know what the… the policies are around that, so I was kind of interested, but yeah, that was a very, like, large, meaty PR, with the goal of generating query summaries.
Ariel @arielvalentin (ATX, USA) 00:41:55 Hmm.
Hannah Ramadan 00:41:55 a query summary is supposed to be the new span name for the updated database transit conventions. We talked about that briefly a couple weeks ago, about, like.
Kind of concerns around… Maybe, like, performance and processing this? .
Ariel @arielvalentin (ATX, USA) 00:42:14 Mmm.
Hannah Ramadan 00:42:14 I always decided that…
merging this PR, we would default to not having the summary generated, and adding big, that if somebody wanted to, they could… they could turn this on and use that for, new span names and have that as an attribute. But, defaulting to off, and that… I think that…
Would be… probably a good idea.
And with the new semantic conventions, there's, like, you know, fallback options. Doesn't have to be summary, so…
I was actually planning to… to add the…
Environment variable for, old, new, or dupe for databases in the next couple of weeks, but yeah,
that is a different PR, because it's almost all AI, and yeah, I want to take a look at…
The guidelines around it.
Ariel @arielvalentin (ATX, USA) 00:43:13 Yeah, so that's one of the things that I was trying to figure out, because it's like.
We want… like, I think… so here's the short version.
And I'll read it out loud for our benefit here. While we welcome contributions from anyone, maintainers of individual projects may, at their discretion, hide or close issues, pull requests, or contributions that are made totally, or in part through generative AI tooling.
The human driving any contribution is responsible for ensuring the LLM generates
Content aligns with the project guidelines and policies, especially the generative AI document and aforementioned Linux Foundation.
generative AI policy.
So, I think…
like, there's the long version of this, but I think it's, like, it's up to us to say.
Yeah, okay, I'm gonna review this PR. The person who wrote the PR knows what… Was… the results were.
And can explain what the results are of the code that was generated.
And, would you be able to maintain and shepherd those?
us as maintainers, if somebody generates a bunch of AI code, a bunch of code using AI,
We reserve the right to say, no, we're not gonna accept this.
Right?
Just because you generated with AI doesn't mean that you know what it does.
Does it mean that you're gonna be responsible for making sure that it works?
Hannah Ramadan 00:44:43 Because ultimately.
Ariel @arielvalentin (ATX, USA) 00:44:45 That responsibility falls on the maintainers, right?
Of whatever it is that… That we end up choosing to accept.
And I think that that is…
I think that's one part of the main general AI policy. There's another set of… that's how I… that's how I understand it.
Right? There's this open issue about it being very, like, you know, for it to be very specific.
I haven't read through this issue in detail.
But there's a… it looks like that there's some sort of a… A policy around
communication with our LLMs and challenging enforcement strategies. Like, this PR right here is gonna make it a bit more explicit.
Making… how to enforce those guidelines.
and what we expect. So, for example.
One of the things that we expect is for commits to contain information to let us know
That you wrote this code with the assistance of…
an AI, or who were of an L&M toolset.
So, in this case, you use ChatGBT and Claude Opus.
to generate this PR, or to generate this commit.
That way we know, right?
It's… there's some expectation that that would happen.
And what we would, we would do is…
we would add, agents to our, agents markdown to our repository, to the, the OpenTelemetry…
Ruby repositories that say specifically this.
Hey, agents, when you go and generate a commit, this line.
As part of the commit message, assisted by and whatever model was used.
To do that.
But that hasn't been merged yet.
So, I don't know that that's exactly what's gonna happen.
But we can see also an example here that we can include in our own repository.
And that's the model that's being proposed
to be included for all repositories. And so, effectively, what Pablo…
is including in this fact here. It's like, hey, here's what's up. This file's to tell the AI, yo, you cannot do this, because you're gonna cause too much…
Is this excessive for the maintainer?
Right? Things should be humans only, don't you be posting on behalf of humans, and so on and so forth. So, this might be something that
We want to include as part of our repo by default to mitigate
AI slot from being generated or sent our way.
That might overwhelm us as maintainers.
Hannah Ramadan 00:47:50 Whoa.
Yeah, I think it'd be a good idea. I know this is still, I guess, draft, but I think it would definitely be worth
adding an agent's, like, markdown file to describe, like, expectations around AI and…
like, commit messages and stuff, and making it clear that it is AI-generated, and whatever.
Expectations we have for, like, the human generating it.
Ariel @arielvalentin (ATX, USA) 00:48:18 Yeah.
So, no, we, no, no, no…
there is no, we're not prohibiting the use of AI as much as we are trying to be careful about how we use it.
Hannah Ramadan 00:48:34 Yeah.
Ariel @arielvalentin (ATX, USA) 00:48:36 But, do you mind if we talk a little bit about that?
about that PR, that, that's summary PR?
Hannah Ramadan 00:48:54 Yeah.
Ariel @arielvalentin (ATX, USA) 00:48:57 Like, just a…
Hannah Ramadan 00:48:59 You guys wanna, like, review it, or just kind of, like, where it stands?
Ariel @arielvalentin (ATX, USA) 00:49:04 I don't know about reviewing it as much as I wanted to hear, again, kind of like,
I wanted to muse a little bit, I think.
I'm wondering to myself, like, Do… How do we…
And I think that, in general, like, the… The SDK needs more offloading.
What do I mean by that? I feel like…
Hannah Ramadan 00:49:42 Hallelujah.
Ariel @arielvalentin (ATX, USA) 00:49:44 like… I feel like what's… We have, like, a…
I just kind of want to share… let me share my whiteboard over here.
You got a whiteboard here, right?
Hannah Ramadan 00:50:03 Yes.
Ariel @arielvalentin (ATX, USA) 00:50:05 So life… If we took the same, like, right now, the model that we've got is…
Can I type in here? Yeah. So we have a processor, Right.
we kind of have the pipeline. We have the batch processor here.
You can put as many sort of processors in between.
Right? You do have, like,
This processor here, and this processor here.
And you can kind of stack them together, or stack them on top of each other, whatever.
Brilliant.
So, when, you know, we do, like, a start span.
That's gonna call, basically, like, on start on each…
In the loop on each one of these processors here.
Before it includes it… before it enues it onto the batch spam processor.
Does that make sense so far?
So basically, you call on, you know, starts fan, this thing calls on start.
And that calls on-start on each one of these processors.
And that gives you… A read-only span, right?
I'm sorry, a Reid Writes fan.
The backstrand processor does nothing until it receives the on-end command.
Right, where it didn't use that thing.
And it sends it off to the exporter.
Which, let me pick a different color for this one here.
So you have the exporter here. And the background processor goes, and it… and it does this in the exporter. But these things are happening in a… in a thread, right?
So… D… No, no.
Can I get a frame?
That thing is happening in its own thread here, where this interaction between the…
Sort of on… on finish, or on end, or whatever it is.
Whenever you call on end on the span.
It calls on in on these as well.
And I'm sorry that this is not exactly a sequence diagram, but I'm trying to… app with sticky notes.
what I got going on here. Oh, this is the… Export function, right?
That's happening in its own thread, and this is happening in the main thread.
So, all of this is happening inline in the main thread.
So, this is, like, the main threat.
And one of the challenges that we see for performance sake anyway.
Is that anything that happens in the main thread is gonna block the end user's
ability to do something unless it's I.O. bound, right? And there's some context switching that happens. Or some context switching and, like.
the scheduler's like, I'm gonna move on to do something else. So, in other words, anything that we do.
Here, when we're creating a span, so let's say I'm doing this in an instrumentation somewhere.
like, let's say this is, like, MySQL instrumentation, right?
That's gonna… that ends up calling, start span over here.
No.
Anything that we do there is gonna delay
Some portion of what the user's trying to do.
Does that make sense so far?
Hannah Ramadan 00:53:50 Right, yeah, I think I see where you're going with this.
Ariel @arielvalentin (ATX, USA) 00:53:53 So, my thought about this is, well… What can we do To take this portion here.
And say, what if we were to defer
This, and put this into its own…
X, you know, like, own sort of, like, red… Right?
And then… These things can happen outside of the band of what the end user is doing, right?
So instead of us doing the sum regeneration over on this side.
and the, you know, obfuscation and everything, the SQL processor would run here.
And that would actually get triggered
It can't be triggered on end.
Because you get a read-only span at this point.
You would get it in the on ending, which is… you have a writable span here.
Right?
On start, you get a writable span, so you can make changes to it.
And so, effectively, it's like, it doesn't block what…
The end user's doing by putting that into its own sort of, like, deferred execution context of some sort.
But I think that the problem, then, is… The way that…
The way that the interaction is gonna be here.
Now that I'm saying this out loud, Is the fact that the…
The on-ending call… is happening… Is happening in the main thread, and has to defer it to here.
But the code has to continue to execute in the main thread and call on end. So it's kind of like, oh, this can't happen…
This can't happen in its own execution context.
I think I stumped on myself, Hannah.
because of the way the API is, it's like, oh, you know, you call on start and onEnd.
Hannah Ramadan 00:56:24 Huh.
Ariel @arielvalentin (ATX, USA) 00:56:25 And what the user sees on this side is the span is finished, and you can't change it no more.
So, there has to be something that happens where, like, if… let's say we incub…
The span of some sort to this other, you know, execution context.
And it's like, oh, it sees a writable version of the span, but no one else outside of it can mutate it. Does that make sense?
Hannah Ramadan 00:56:53 Yeah.
Ariel @arielvalentin (ATX, USA) 00:56:55 Because by this point, because it's like, by the time that it gets to the backspan processor.
Right? This is, like, the silly model. When it gets down to the batch band processor over here.
We wanted to see… the span that's already being changed.
Right? Unless we change the model where the batch band processor's not wrapping the exporter.
But it were… but if the specification would allow chaining the batch band processor, and say that the SQL processor ran here.
In, in this section.
If that makes sense.
Where, if it was more that…
The batch plan processor was in the middle of these two, or the SDL processor.
And this, on export, we're running.
Where the export would run, It would receive the span data.
And now, we're processing the spam data
And converting it, and changing it, or whatever, to have a new span name, to have new values.
And that would occur not… That would occur outside of the user's context.
But, back to the Spanish over now, the problem with that is… It's sort of against the… the specification.
Because this would not be… Compliant with the… With the spam processors,
the span processor state management.
or the spam processor interface, because the spam processor interface has to have the on start, on-end interface.
So this is, like…
Free exporter, or something like that.
interface, which doesn't exist in the spec.
But I think that this would allow us
To offset, or to, you know…
Does it make sense what I'm saying?
Hannah Ramadan 00:59:11 Yeah, yeah, yeah,
That does make sense. Wasn't… was… I feel like there was something that… where, like, spans could be… Changed…
on the, like, before they reach the collector, but, like, in the SQL… in this… if the SQL processors, maybe…
Yeah, like, could it… is it… oops, I don't know how to use a whiteboard. Could it be right.
Ariel @arielvalentin (ATX, USA) 00:59:38 It's all good.
So, that's a… yeah, that's the thing, is that the banks… in this model.
This would be a decorator of the exporter.
And so it wouldn't have, it wouldn't have… It would be, like, Let's do… let… it would…
Whenever the batch span processor was exporting a set of spans, this…
I don't want to use the word processor, but it's kind of like…
Export… export a decorator, let's… let's, you know…
evacuator…
the bash band processor has gone through the process of saying, I'm gonna take all of these…
the group of spans that are read-only spans, and I'm gonna send them off.
To be exported into… as protobuffs or whatever.
Once this hits this… Exporter, decorator.
It'll have, sort of, like, the raw span data, I believe. Let me just go ahead and take a look at the implementation.
I'm sorry about that.
I'm gonna confirm that that's what it does.
Arjun Rajappa 01:01:02 Somewhere it calls to span data.
Ariel @arielvalentin (ATX, USA) 01:01:14 Is that happening in the… Export batch? Yeah, so… Yup.
So as, as Arun, Arjun,
mentioned, it's this line here. So basically, like, this would be, you know, Happening on line 187,
that says, I'm exporting the span data.
One that… and then we would be taking the span data.
And in a separate thread, or in a separate execution context outside of the main thread.
We would look for spans that had design… the span data that had specific… Attributes in it.
Like, the DB system.
and say, oh, db system is MySQL.
So, I'm gonna go ahead and apply the…
Hannah Ramadan 01:02:11 SQL summary transformations on this band data.
Ariel @arielvalentin (ATX, USA) 01:02:16 And that's basically a different data structure than the span objects themselves.
Right.
It's the only way that I can think of that allows us to take
The execution out of the user's path.
Hannah Ramadan 01:02:36 Yeah.
Ariel @arielvalentin (ATX, USA) 01:02:41 And this is very, like, highly experimental in my brain, as you can tell.
Because we're just talking about it right now.
But I…
But if we, you know, in the other cases, like, you know, right now, like, Ruby threads are kind of, like, they're awful, like, not awful, but…
Ruby threads are constrained, right? So, if we can somehow, like, in the future, make these Raptors, then we get true parallelism there.
And we can get…
get this done that way. The other thing is that we can think about doing is doing, sort of, like, a native
A native version of this?
Which is not ideal for many reasons, but if we had a native implementation of this, then, again, it would, like.
We can… A defer down to…
faster implementation than a pure Ruby implementation, potentially.
You know… to mitigate some of the challenges, you know, that I'm… at least I'm facing.
with, with Ruby Parallel example.
Anyway, so we're over 3 minutes, I'm really sorry, everybody, I didn't mean to,
Hold everybody up here.
Okay.
Hannah Ramadan 01:04:08 No, that was interesting. Could you, like, screenshot or keep a hold of that,
What was it called? The whiteboard?
And share that. That's good to kind of remember and look back on.
Ariel @arielvalentin (ATX, USA) 01:04:24 If you would like to… Get Thunis…
What do I do, real sexy here?
Oh, look.
Hannah Ramadan 01:04:34 I feel like I can't even alert to myself, I think.
Ariel @arielvalentin (ATX, USA) 01:04:37 Garrett, you think you can email it to yourself?
Hannah Ramadan 01:04:39 I think so.
Ariel @arielvalentin (ATX, USA) 01:04:41 Give it a shot.
I'm gonna copy the link, I'm gonna go into… a channel.
I'm gonna dump it right here.
Does that work? The link?
I…
There's no way for me to, like, export this as, like, a…
Like a PNG? Yeah, yeah, Ken. Yeah, what's up, man?
You and my solo?
Look, Ana, if you look in, the CNCF,
Booyakasha, I just… I just pasted in the CNCF slide.
How'd that?
Hannah Ramadan 01:05:35 Got it. Yep, yep, yep.
Oh, nice. But… Andy?
Ariel @arielvalentin (ATX, USA) 01:05:42 But I do appreciate everybody for, staying over. I'm really sorry to keep you all over. Arjun, thank you so much for joining us so late at night.
If there's any good word I can put in for you, for your manager, let me know.
Arjun Rajappa 01:05:57 Dude.
Ariel @arielvalentin (ATX, USA) 01:06:00 Okay. Well, I hope that y'all have a great day. Thank you so much for joining. We'll see each other next week.
Hannah Ramadan 01:06:05 Thanks, Ariana.

SIG: Go SIG
Date: 2026-10-15
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn (Splunk)** 00:58 Hey, David.
**David Ashpole (Google LLC)** 01:01 Ed?
**Tyler Yahn (Splunk)** 01:02 How's it going?
**David Ashpole (Google LLC)** 01:04 Doing all right?
Yeah.
**Tyler Yahn (Splunk)** 01:06 Are you going to be at KubeCon North America?
**David Ashpole (Google LLC)** 01:08 I will be, yep.
**Tyler Yahn (Splunk)** 01:09 Nice.
**David Ashpole (Google LLC)** 01:10 Are you on top?
**Tyler Yahn (Splunk)** 01:12 Observability Day as well, right?
**David Ashpole (Google LLC)** 01:13 Yep. I'll be there Sunday for the maintainer day or whatever. Yeah.
**Tyler Yahn (Splunk)** 01:18 Yeah.
**David Ashpole (Google LLC)** 01:19 Yep, Observability Day.
**Tyler Yahn (Splunk)** 01:21 Nice.
Cool. Yeah. You got any, talk submitted?
**David Ashpole (Google LLC)** 01:26 Yep.
Kubernetes SIG instrumentation introduction and deep dive.
**Tyler Yahn (Splunk)** 01:32 Nice.
**David Ashpole (Google LLC)** 01:34 It's gonna be really different from last year.
Maybe we'll get… maybe we'll get a sixth person this year.
**Tyler Yahn (Splunk)** 01:40 Wow.
**David Ashpole (Google LLC)** 01:42 to attend.
**Tyler Yahn (Splunk)** 01:43 you.
**David Ashpole (Google LLC)** 01:44 Hey.
**Tyler Yahn (Splunk)** 01:45 Hey.
Are you still the, the, the lead on that? Project?
**David Ashpole (Google LLC)** 01:57 one.
**Tyler Yahn (Splunk)** 01:58 attack.
**David Ashpole (Google LLC)** 01:58 else.
**Tyler Yahn (Splunk)** 01:59 Yeah, that's right.
**David Ashpole (Google LLC)** 02:00 We just had one of our chairs stepped out, so there's one chair.
who's now on maternity leave, and then 3 TLs.
**Tyler Yahn (Splunk)** 02:09 Okay.
**David Ashpole (Google LLC)** 02:10 We… right, we have one who's more logging-focused, and then I guess I'm the… the only one who cares about the trace-focused aspects of the SIG, and then… Everybody is kind of interested in the metrics.
**Tyler Yahn (Splunk)** 02:27 Oh, okay, I gotcha.
Hmm.
Cool. All right. I'm sorry. I'm looking at the, agenda. So looks like if you haven't yet, go ahead and add your name to the attendees list. And if you had agenda items you wanted to talk about, go ahead. Add them there as well.
I don't see Robert on the call, but other than that, I think we probably could jump in here in just a second.
Yeah, let me, let me start sharing my screen here.
Okay, cool.
Okay, cool. First off, I guess I wanted to just pull attention to the new dashboards, that were opened.
For the pull request stuff, this has been really helpful in other SIGs, so, I'm pretty excited to have it here as well.
There's, Yeah, I think this is great, like, in case you haven't seen it, there's a good breakdown, that… tells, essentially, like, all the open PRs, like, if it's waiting on a maintainer.
Waiting on reviews, or waiting on the author for feedback. There's a lot of author feedback, and then a bunch of draft PRs as well. So that's the classifications. I think it's something that we could probably jump into here, maybe weekly or bi-weekly into the waiting on maintainer stuff. I did take a look at this right beforehand. There's… there's a lot of stuff that can get merged. Problem with this repo is that it all needs to be up-to-date in Maine.
So, I'm looking at trying to merge a bunch of this stuff. There's a few things that, obviously.
This dashboard doesn't quite understand, the fact that, like… Like, this PR, looks like it's only approved by me, so this needs more review. This… one here… I don't know if Robert actually approved this, but, like, this one would also need more review, given the fact that we have the same company here. So, there's, like, a little bit of a, you know, obviously it's not perfect, but it gives you a little bit of a heads up on this. It also helps you if you wanted to, like, go in and find.
things that need help. So the waiting interviews is, I think, a good place to start. It's not always perfect, either. Like, this waiting on authors thing is not always accurate, but… Yeah. I think that's, yeah, just a good heads up. Helpful from the maintainer's perspective.
**David Ashpole (Google LLC)** 05:06 Pretty cool. If you subscribe to that, do you get… Notifications all the time about the issue.
I saw you were subscribed to it.
**Tyler Yahn (Splunk)** 05:16 Am I?
Oh, I don't know.
**David Ashpole (Google LLC)** 05:21 I guess it updates the description, so you don't.
**Tyler Yahn (Splunk)** 05:23 Yeah, I don't think it actually… yeah, exactly.
**David Ashpole (Google LLC)** 05:26 Okay, that's nice.
**Tyler Yahn (Splunk)** 05:28 Yeah. Also, I don't know if we want to lock the conversations on these.
I guess, I guess we'll see when that happens.
Yeah, actually, I… no, you know, you're right, I don't actually get updates on this, because I'm on the other, SIGs as well. I must be subscribed there, so no, I don't get updates on them. So, yeah, because it's just top level.
But, I do wonder, because, like, this is also something that Trask is working on, like, if you had that as a suggestion, he might be able to take that as, like, feedback as well, but it's also, yeah.
Up to you. One of the other things that, like, is interesting is, like, this is using the shared workflow.
To generate this, it's just a configuration there.
That's where the original PR was from.
I guess maybe I'll ask this now, like, there is another setting in there, which I found to be… It's cool, it had a bug that was extremely… frustrating, but, like, the idea is that you can set it so that Copilot reviews are continually requested until it succeeds, so it's been really helpful for, like, newer First-time contributors, because they'll come and, like, they'll get review instantly, but then they'll also, like, get, you know, a lot of just standard repo stuff from our You know, code review stuff done, before humans have to actually come take a look at it.
The… there's, like, a budgetary thing. I'm not exactly… I'm still not 100% sure how the allocation of, like, the Copilot review gets assigned, but I think that, like… because, like, when I open a PR, I think it actually gets assigned to me for some reason.
Which, I'm always out of review…
**David Ashpole (Google LLC)** 07:11 Oh yeah.
**Tyler Yahn (Splunk)** 07:11 quota.
**David Ashpole (Google LLC)** 07:12 We talked about this at one of the TC meetings, so there's… it's this funny thing where if you do not have Copilot enabled on your account, It comes from… like, the CNCF's budget or something, the project's budget. Yeah. And then once you get Copilot on your account, which I think all of us have.
Then it comes from your own quota. So there's this weird thing where, like.
Yeah, we… the project pays for you if you don't have it, but if you have your own account, and it runs out of quota.
it will just be out of quota. You don't ever get to fall back to the project's quota, which is a bit annoying, because you're kind of penalized for Having signed up for the darn thing.
**Tyler Yahn (Splunk)** 07:56 Yeah, which is where the bug came in, because that auto-review thing didn't take, I'm out of quota as a success, so it just kept requesting the thing.
**David Ashpole (Google LLC)** 08:05 I see, yeah.
**Tyler Yahn (Splunk)** 08:06 And I woke up with over a thousand comments on a PR, which is pretty great. But anyways, like, that's been fixed. But yeah, I mean, I think that, like.
I think from what you just said, also, like, it's more about new users anyways, so, like, they were more likely to not have that, so it should be pretty helpful, and, like.
So yeah, I'm just maybe running that by, see if folks wanted to enable it.
**David Ashpole (Google LLC)** 08:30 I'm down to enable it. It would be nice if there was, like, some cap or something, just so that one runaway, bizarre user didn't… blow through all of our quota, or something like that. Yeah. You know, some, like.
Claude, you know, whatever the really simple version is.
**Tyler Yahn (Splunk)** 08:47 Yeah.
**David Ashpole (Google LLC)** 08:48 Loop.
**Tyler Yahn (Splunk)** 08:50 Yeah, that's actually, I mean… Again, like, this is, like, all… it's in that repo. You could always just go push a fix, or push a limit thing if you wanted to, or you could just ask Trask. Trask, he's early on this, I'm sure he would be happy to.
**David Ashpole (Google LLC)** 09:06 Happy to just turn it on and then we can give our feedback to Trask.
**Tyler Yahn (Splunk)** 09:09 Yeah, okay.
**David Ashpole (Google LLC)** 09:10 If he's on top of it.
**Tyler Yahn (Splunk)** 09:12 Then, let me… let me add an action item here.
Okay, cool. Yeah, I will… I will look into adding that as well.
Okay, next up, Damien, you wanted to, talk about Automerge?
I thought I saw Damien on here. I don't know if he's…
**Damien MATHIEU** 09:46 Yeah, it's… it's me. I don't know why my Zoom just crashed.
**Tyler Yahn (Splunk)** 09:51 Oh, okay.
Did you want to say anything about this, or…
**Damien MATHIEU** 09:59 I just want to raise awareness about it. Sorry, it's on Tyler's screen, but it's only available to maintainers.
Basically I want to enable auto merge.
Which would make it way easier to merge all the dependable PRs.
I've been chatting about it with Robert. His concern is that it would also allow folks to Push something into a branch after Automerge has been enabled, and therefore, like, allow them to, like.
to push things that we don't want in the main branch.
I think this can be solved with auto, like, with the merge queue.
Because then when we click merge on merge queue, then it's like whatever was pushed afterwards is not being merged anyway.
I'm happy looking into setting up MergeQueue.
Instead.
But I really think, for Deep and Abouts, I'm also happy to have, like, a… rule for maintainers that says that we cannot do auto-merge unless it's for Dependabot?
I think Dependabot is really taking a lot of our time at the moment, and just setting up a merge queue would just allow us to… approve, enable it to merge, and let's depend about rebase everything afterwards, and not have to worry about it anymore.
Right, but… And,
**Tyler Yahn (Splunk)** 11:41 Yeah, I mean, I'm with Robert. I think that that was the original reason why we didn't enable AutoMerge. It was something that was raised years ago, as well.
I think the merge queue, like you're saying, could be helpful, though. So, yeah, I mean, that sounds like the right way to go.
**Robert Pająk (Splunk Inc.)** 11:56 I agree.
**Damien MATHIEU** 11:57 Okay, sorry. Okay, I'll, look into setting up a merge queue instead.
I'm not sure if that requires an admin change.
I'll… I'll look in it. I'll look into it.
And sorry for the background noise.
**Tyler Yahn (Splunk)** 12:14 Yeah, no worries. Alright, sounds good.
**Puneet Singh** 12:16 I have a question here, a doubt basically, that in some cases, like the Go version update, we do it ourselves.
So… Sorry, going back, is this different from the Renovate?
Based dependency bumps, or it's the same thing?
**Tyler Yahn (Splunk)** 12:35 So the auto-merge is a GitHub feature where you can take any PR and say, like, at this point, once all the status checks have passed, and once all, like, the reviews have, like, come in, it'll just… you don't hit the merge button anymore, it just merges it for you.
Is the idea. So, for… in the situation that Damien's talking about, yeah, like, the Renovate PRs, is, I think, what he's actually mentioning, is like, yeah, like, what'll happen is it won't merge it, because it's not up to date, but Renovate will automatically rebase. So, essentially, once you get the review in.
you can just say, like, auto-merge once this is, like, ready, and Renovate will rebase, Seattle will run, and then it'll just merge itself, and you, like, you can be asleep while that happens, is kind of the idea, is more… around, like, essentially, you get that set up. A merge queue is similar, it's just, like, you essentially add it to the queue once it's ready, and then I think it allows a rebase, but any, like, new changes that are pushed get pushed out of the queue.
**Damien MATHIEU** 13:31 The merge queue does the rebase, but once you push merge, it's a snapshot in time, and that's where it does the rebase, and it does not add any new commits afterwards, which is where it's better.
**Tyler Yahn (Splunk)** 13:47 Yeah, perfect.
**Robert Pająk (Splunk Inc.)** 13:47 Yeah, I think .NET automatic instrumentation is using merge queues, and they're very happy with it, and it's working fine for Renovate as well, if I remember correctly.
At least it's better than manually, because you have the chance that it will work.
**Damien MATHIEU** 14:01 I mean, right now, it is extremely time-consuming. And, I mean, the collector is using the merge queue. I'm pretty sure Contrib… Collector Contrib is also using the merge queue, which it sometimes fails because of flaky tests.
But if it fails because of that, so it's like, don't fix it, I would say.
And that just reduces toil a lot.
**Puneet Singh** 14:29 Yeah, I think, I think that makes sense. My confusion was with respect to another thing that, that if the test app passed will not, I, I basically confused it with auto approve actually, which is, which is not the case. And, and yeah, I think maintenance only can do the merge, which is a lot of… work right now, I mean, based on what I see on the daily basis, so yeah.
**Damien MATHIEU** 14:55 I mean, it's a lot of work, because we have to… Sorry. Push merge, making sure that the commit is the latest one as well.
And so for dependable, when there are five dependable PRs, it means we have to push one.
Wait for the next one to auto update.
Ci to pass, and then push it, which is, like, 10 to 15 minutes… 15 minutes between each PR.
it can easily take a morning to do everything. Obviously, you do something else at the same time, but, it's still, like, Yeah.
a digression in whatever else you would be doing, but better.
Thank you.
**Puneet Singh** 15:47 Yeah, I think it makes sense, yeah.
**Tyler Yahn (Splunk)** 15:53 Cool, alright, yeah, look forward to the…
**Damien MATHIEU** 15:56 I'll be, setting up merge queues.
**Tyler Yahn (Splunk)** 16:00 Sounds good.
Okay, puneet, you wanted to, Talk about experimental option, rejection.
**Puneet Singh** 16:12 Yeah, so I think, I started with.
So, so the basic idea was that, With multiple experimental features around.
Meter provider, at the moment, We only have one meter working because we are not addressing that if two experimental features are supposed to work together.
What I started with was declaring that explicitly that, you know, that finish aware instruments and the meter contributor cannot work. But I think another option was to decide that if we have multiple experimental options, we can reject route right away.
And I was just thinking that what happens if they have experimental options, but not on the meter side, but let's say viewer exporter, and they can work with, you know, the experimental meter, but in order for work, you know, for them to work together, the maintainers still have to commit to say that they work together, so essentially committing towards their composability as well. And until, I think, such a requirement comes from user, we can simply reject that.
multiple experimental options, be it meter, viewer, exporter, or anything in the meter provider, cannot work, like, multiple options at a time. Does that make sense?
**Tyler Yahn (Splunk)** 17:50 Yeah, I mean, it makes sense to me.
I thought that's what we kind of talked about last time, was that we'll just allow one option And then… if a user comes along and says, like, hey, I need these two options together, and, like, they, in theory, shouldn't clash, or in theory, developers could make this work, like, we'll address it then. That's what you're saying, right?
**Puneet Singh** 18:11 Yes, yes. I mean, my only confusion was that we are considering multiple meters, but then if there is experimental option, the viewer exporter, what to do, but then, the convergence came towards that you still have to say that these two can work together, so that's.
commitment, so if you're not seeing, might as well reject, actually, and let the user ask for it first. So… In that case, I'll switch to… conf.experimental, which means checking that if we have more than one experimental option, just simply reject it rather than going for explicit rules. So just stating for clarity.
**Tyler Yahn (Splunk)** 18:48 Yeah, I think that's a great way to start, at least.
I imagine, the users may be us coming back and just saying, like, yeah, I really want this, but, like, that's fine as well. Like, I mean, I think just to get this over the line, like, let's just go that direction right now, yeah.
**Puneet Singh** 19:04 Yeah, and in case, users come with a requirement, that might be a point where you start to think that how you want to say what things are supported and whatnot. In that case, maybe more elaborate solution can be planned, depending on what we need. So, yeah.
**Tyler Yahn (Splunk)** 19:22 Yeah, a huge, matrix of… Incredible.
**Puneet Singh** 19:26 Indeed, I understand, you know, like, that where this was going, so… unless and until we absolutely need it, there is, there is, yeah, we can avoid as well. Yeah, I think, yeah, that's, that's more or less.
**Tyler Yahn (Splunk)** 19:38 David, what do you think about this?
**David Ashpole (Google LLC)** 19:41 This is… Just to be clear, this is saying that no two experimental features can ever coexist, right?
**Tyler Yahn (Splunk)** 19:48 Yeah, you can only have one on at a time.
Steven S. Well, so, okay, hold on. Currently. That's how we're gonna start. And then, if somebody comes along and says, I need these two experimental features, like, we're not saying, like, that'll never happen. We're saying, like, okay, then we'll evaluate it case by case.
**David Ashpole (Google LLC)** 20:10 That seems fine to me, like… To me, the point of the experimental features is to I guess the key gotcha is gonna be, like, Is Obi gonna want… Two of these, because you're definitely planning on using this, like, like, I see this in our future, it's not, you know…
**Tyler Yahn (Splunk)** 20:28 I do too. I do too. That's why I'm saying I think it's going to be one of us that comes and says, Hey, can we have these two?
**David Ashpole (Google LLC)** 20:34 I'm okay with it. I just want to see these features move forward in the spec. But you're also, you know.
have a vested interest in some of these getting like released and in real things in the near future.
**Tyler Yahn (Splunk)** 20:48 Yeah, I… the thing is, is, like, I mean, I actually, like, I could definitely see the found instruments and the finish being useful for OB, but, like.
I, like, I'm so underwater, I'm trying to get a 1.0 out for OB right now, like, I will cross that bridge when it happens, so, yeah.
**David Ashpole (Google LLC)** 21:03 Okay. I mean, I have no objections to it, and I'm happy to revisit it later. It'll probably surprise a few users, but, Yeah.
I want to make sure that we can… like, I think getting these experimental features out and in people's hands is more important than… making, like, them work.
you know, perfectly for all use cases, kind of. Like, they should work, I should say, but, like, I'm okay with this restriction if it means that we unblock some of our experimental features.
**Tyler Yahn (Splunk)** 21:35 Yeah, and, like, the other option that Puneet had already suggested was, like, this, like.
essentially, an allow list within blocks, and I think that could work, but then it just gets super complicated, and, like, we have to start maintaining, like, this compatibility matrix right from the start, and I think that this is just an easier way to get us out, is just… yeah. Default to nothing works, and then add it in as needed.
**Puneet Singh** 21:58 So the other forward option, I thought I can hold on and, you know.
Think about it when it comes, is the… Composability of the experimental features, and that… that's basically start looking into that, okay, user are looking for these two options, how we can make them work together, so… So essentially making changes to make things fit together and yeah.
So, that can come later, once the requirement comes.
**David Ashpole (Google LLC)** 22:26 I had one thought around that.
which is like in other code bases I've worked in.
People use, like, feature flags.
Quite a bit, and the pattern is usually, like.
Right now we're building these, like, very separate implementations of things to make sure that we don't.
impact existing users.
But you can, like, mix code a little bit more effectively if, like.
There's a feature flag thing, and you, like, put all of your special code inside an if statement that checks the feature flag enablement thing first.
It's like… I don't know if that model…
**Tyler Yahn (Splunk)** 23:08 I don't think that that really works.
**David Ashpole (Google LLC)** 23:10 You don't think.
**Tyler Yahn (Splunk)** 23:10 given.
**David Ashpole (Google LLC)** 23:10 here.
**Tyler Yahn (Splunk)** 23:11 No, because, like, the isolation mechanisms that we're using are literally, like, returning different types, underlying types, to, like, interfaces.
**David Ashpole (Google LLC)** 23:19 That's the key, is, like, we would have to not do that, right? We would have to return the same types, but then have the actual implementation have a… You know, a check for the enablement of the thing in it.
**Tyler Yahn (Splunk)** 23:31 stuff.
**David Ashpole (Google LLC)** 23:32 So that would be the… that would be the alternative.
**Tyler Yahn (Splunk)** 23:36 And I think that, like, that… performance issue was something that we wanted to try to avoid, as well as, like, the mixing of the code also, like, introduces the possibility for bugs into, like, stable releases.
**David Ashpole (Google LLC)** 23:46 Mixing of the code does, yeah.
**Tyler Yahn (Splunk)** 23:48 Yeah, and I think that, like.
I'd prefer the isolation that we currently enable, yeah.
Even if it makes it harder because, like, honestly, to be The people that care about these are, like, the people on this call.
And, like, y'all are smart enough to think… figure this out. Like, I definitely think the feature flags are way easier to use, like you're saying, and, like, it's also nicer because you can dynamically do it, but, like.
I think that, like, at least until we get, like, big user bases that are going, like.
All of these, you know, features I really want to start using, like… From the start.
I also think that, like, you know, like, say the bound instruments stuff, like, you have to already have plumbed it into your API.
Right? So, like, if you're already plumbing it into your API, like, adding another option to, like, a setup for the SDK doesn't seem too, you know, hard to do. Similar for the Finnish stuff.
**David Ashpole (Google LLC)** 24:40 Yeah, yeah, for sure. It's… it was more… Anyways, I think that's fine. I'm not, like, super opinionated.
**Puneet Singh** 24:49 But, just… sorry.
Correct.
**Tyler Yahn (Splunk)** 24:52 Go ahead. No, go ahead.
**Puneet Singh** 24:54 Would it be advisable to invest a bit into composability of features given this might likely happen for Example, OBI, like I mentioned.
**Tyler Yahn (Splunk)** 25:06 No, I… Get your… get your meter configurator out. Don't… don't focus on this.
**Puneet Singh** 25:15 All right.
**Tyler Yahn (Splunk)** 25:17 I think that… it… so… Obi is not going to be looking at this until after KubeCon at the earliest. I'm going to try to take some time off at the end of the year anyways, and it's pretty much, like, the end of the year comes really quick after KubeCon.
So, I imagine the earliest that we're gonna see is, like, next year, before I come back and say, like, I really want these two features together, so, like… I'd rather you get your meter configurator out before then, yeah.
**Puneet Singh** 25:45 Cool.
**Tyler Yahn (Splunk)** 25:50 Okay, cool.
gary scott: Alright, moving on, Robert, you wanted to talk about a PR.
**Robert Pająk (Splunk Inc.)** 25:56 Yeah, I think you interrupted sharing on this. Oh, you're still.
Yes, so… I think it would be easier to ask here on the call. So, we had this, also ago, X cardinality limits, and just a question, are we fine removing it? Because it was removing from the documentation once we deprecated it, as we added this with cardinality in limit option.
And I think we can just remove it right now. It's already, it all has already been removed from the docs in the previous PR.
So just asking for a battle or any objection here.
**Tyler Yahn (Splunk)** 26:44 Did we say… Hmm.
I think…
**Robert Pająk (Splunk Inc.)** 26:49 You see the change log we already said that is being deprecated.
Before.
**Tyler Yahn (Splunk)** 26:56 Yeah.
**Damien MATHIEU** 26:56 I know I… I approved this one already, just thinking that since it's in X, it's unstable anyway, and we have released it with a deprecation warning and saying it's going to be going away, which is fine.
**Robert Pająk (Splunk Inc.)** 27:14 Yeah, I just want to double check.
**Tyler Yahn (Splunk)** 27:18 Yeah, I think it's more that communication. I just wanted to make sure that we… have communicated the deprecation, so if we've already done that, then I don't see why we couldn't…
**Robert Pająk (Splunk Inc.)** 27:26 You've done this.
**Tyler Yahn (Splunk)** 27:27 Yeah, when did we do that?
**Robert Pająk (Splunk Inc.)** 27:29 Like, two releases before, I will need to double-check the changelog.
**Tyler Yahn (Splunk)** 27:33 Okay, yeah, seems good.
**Robert Pająk (Splunk Inc.)** 27:36 But I can triple check it just to be sure that we for sure.
**Tyler Yahn (Splunk)** 27:41 Yeah, I mean, I can too. It can be part of the review, I do.
**Robert Pająk (Splunk Inc.)** 27:45 Yeah.
**Tyler Yahn (Splunk)** 27:46 Those things good.
**Robert Pająk (Splunk Inc.)** 27:49 Yes, ma'am.
**Tyler Yahn (Splunk)** 27:49 Is there… Any opposition on the call.
**Puneet Singh** 27:58 Nope.
**Damien MATHIEU** 28:00 And you already have my approval.
**Tyler Yahn (Splunk)** 28:05 Okay.
If that's the case, yeah, Robert, let's move forward with it.
Next up, Robert, you want to talk about, another pull request?
**Robert Pająk (Splunk Inc.)** 28:14 Yeah, this one is regarding the exporter stabilization.
So, there is one thing… there is one part of the specification which says that the exporter cannot… must have, you know, the export must have a timeout. But, for instance, when you have, like, all the languages that support standard output exporters or file exporters.
do not really interrupt when there is a timeout. You know, when there's an I.O. call to write something to a file, it just waits, or hangs, or whatever. And I just wanted to add, you know, an explicit exception.
For this rule, so that, you know.
just to make it clear that we are compliant, and that when we do, you know, audits doing AI, or even manually, we are… we can be certain that it's okay to have this implementation for this EDF exposure.
Any thoughts on that?
**Tyler Yahn (Splunk)** 29:15 So wait.
If… Like, the file mount disappears, our exporter's just gonna hang forever?
**Robert Pająk (Splunk Inc.)** 29:23 No, it should not, because it will just return an error, usually, when you write to a file. If for some, any reason, it will write because, I don't know, something's wrong in the kernel or whatever, you know, and it hangs on the right in your file, then it can hang on the right on the export, but it has been forever there like that.
The only other option is to make some other Go routine which makes a write.
But still, this bureaucracy will hang anyway.
And we'll go with this.
**Tyler Yahn (Splunk)** 29:58 I don't… I don't understand.
Like, isn't… isn't this PR saying that you should be allowed to have… Like, hang forever on the standard allowed exporter?
**Robert Pająk (Splunk Inc.)** 30:12 Yes. Yeah.
**Tyler Yahn (Splunk)** 30:14 Why do we want that, though?
**Robert Pająk (Splunk Inc.)** 30:17 How would you prevent it?
**Tyler Yahn (Splunk)** 30:19 A context timeout?
**Robert Pająk (Splunk Inc.)** 30:21 But there's no context timeout for when you're writing to a file.
When we have an, you know, the right, Right device?
Then you cannot interrupt it.
**Tyler Yahn (Splunk)** 30:35 You can't interrupt it?
**Robert Pająk (Splunk Inc.)** 30:36 You cannot.
**Tyler Yahn (Splunk)** 30:44 is… Okay, so, like, Is there just no error that could ever happen there, is what you're saying?
**Robert Pająk (Splunk Inc.)** 30:53 No, it can… there will be an error. The thing is that you do not control the timing. You cannot interrupt, you know, in the middle, when you're writing to a file, you cannot say, like, in one second, I want to interrupt this call.
**Tyler Yahn (Splunk)** 31:06 I mean, I'm coming from Obi where I work at a pretty low level. So I don't know if I…
**Robert Pająk (Splunk Inc.)** 31:10 ego.
**Tyler Yahn (Splunk)** 31:11 I don't know if I believe that.
**Robert Pająk (Splunk Inc.)** 31:13 Go.
**Tyler Yahn (Splunk)** 31:14 I still think you could do it and go,
**Damien MATHIEU** 31:18 I mean, a… Timeouts?
Even if we're just writing, like, just… we could be writing and timing out on the rights?
**Tyler Yahn (Splunk)** 31:29 Yeah.
Yeah, I mean, I think I'd have to understand the problem a little more.
**Robert Pająk (Splunk Inc.)** 31:38 Sure.
**Damien MATHIEU** 31:38 And, I'm sorry, I kind of missed, I'm not sure it's the same specification PR you're mentioning, but the one I mentioned, we talked about earlier.
My concern, and I've commented on it, is also that I think your DR comments, like, your PR, like, specification change is too broad.
And even if we do it, because technically we can't do it any other way. We need to make sure that, it's the only reason we can do it that way.
And.
**Robert Pająk (Splunk Inc.)** 32:18 Yeah.
**Damien MATHIEU** 32:19 share.
**Robert Pająk (Splunk Inc.)** 32:20 So I changed the PR during the call that it's still a must not.
And I added, except because when it's a synchron, it's a I/O call that cannot be interrupted by by an Api.
**Damien MATHIEU** 32:36 That sounds better.
**Robert Pająk (Splunk Inc.)** 32:44 And.
**Tyler Yahn (Splunk)** 32:45 Well, I mean… I, I don't… yeah, like, if… the spec community wants to go that direction, I don't see what the problem is.
Okay. I'd have to look.
Closer to understand.
Like, is this a problem? Like, do we have users complaining about this?
**Robert Pająk (Splunk Inc.)** 33:03 No, we don't. It's just about, you know, we don't have users complaining about the current thing. It's just, you know, during the audit.
I… It's just, you know, AI just noticed that it's not really making the time out, it's not really working for STV out exporters.
So it's about compliance and just making sure that we know everything is perfectly clear.
**Tyler Yahn (Splunk)** 33:24 I see, okay.
Yeah, sounds good. I'll have to take a look.
Okay, that looks like the end of the written agenda. Any other topics folks had on this one?
**Robert Pająk (Splunk Inc.)** 33:41 Observability Day.
Yeah.
call for papers. I don't know. It's until this. I don't know, but I think it's coming.
**Tyler Yahn (Splunk)** 33:50 Yeah.
**Robert Pająk (Splunk Inc.)** 33:51 Send it, yeah.
**Tyler Yahn (Splunk)** 33:52 Yeah, yeah.
**David Ashpole (Google LLC)** 33:54 Maybe I'll have to do something.
Hmm.
**Puneet Singh** 33:58 Yay.
**Tyler Yahn (Splunk)** 34:00 Go ahead.
**Puneet Singh** 34:01 Sorry, I'll be somewhat inactive for the rest of the October. I'll be here, but… Overall activity might be very less, actually.
**Tyler Yahn (Splunk)** 34:14 Yeah, sounds good. Are you taking vacation time?
**Puneet Singh** 34:17 No, just some… personal paperwork, I would… that needs more attention, so, yeah.
**Tyler Yahn (Splunk)** 34:22 Yeah, okay, fair enough.
Yeah, just a bummer. You should be taking some vacation time, right?
Cool. Alright, yeah, no worries, yeah, we'll happily see you back, next month, then I'll…
**Damien MATHIEU** 34:35 I mean, this is open source. Even if we are all doing that on our work time.
You don't have to justify yourself.
Taking time off. Taking time off is something that we all must do.
**Puneet Singh** 34:53 Yeah, I mean, this is much better. I remember when I first started contributing, like many years, I used to apologize for the issues I didn't work on and, you know, showed up anyway in the next meeting. So, yeah, slowly I learned that, yeah, it's fine, actually.
**Damien MATHIEU** 35:10 I mean, as I think, as as Tyler would say, it's Europe talking.
**Tyler Yahn (Splunk)** 35:17 Nice.
Yeah, so I'm pretty sure you're required to take at least 3 months off if you're on that side of the dateline, so, yeah.
No, jokes aside, it is important to take time off and make sure you prioritize life outside of this, so yeah, absolutely. No need to justify. We still appreciate all the help you're giving us, yep.
**Damien MATHIEU** 35:38 I mean, if you want a justification or something like a consolation or not, I was away for 4 months on paternity leave, and I still accrued a vacation, because it's, like, paternity leave is not vacation.
And so I will be off for mid-December to mid-January for a month.
So, yeah.
Just feel free to take time off, it's important.
**Tyler Yahn (Splunk)** 36:11 Yeah, I guess actually that's a good point, just a heads up. I did kind of mention it, but like after KubeCon, at least in North America, there's, like, a big lull for, Thanksgiving comes up, like, two weeks afterwards, and then… A lot of people take a lot of time off there, and then the Christmas holidays, like, it just… there's very little activity in the project. So, yeah, do plan to see…
**Damien MATHIEU** 36:34 It's more than that. Usually OpenTelemetry goes on a kind of free.
**Tyler Yahn (Splunk)** 36:38 Yeah.
**Damien MATHIEU** 36:39 With an official, we are not working during that time.
**Tyler Yahn (Splunk)** 36:43 Yeah, it's definitely… it slows down dramatically.
Which is always fun, because then you have KubeCon Europe in March, and you have a sprint in the first two months of the year.
Cool.
brian: Alright, I think if there's no other topics folks had… We could probably end the meeting here.
Thanks everyone for joining.
Good to see you all. I will see you all in a week's time, or asynchronously until then.
**Damien MATHIEU** 37:14 Thank you.
**David Ashpole (Google LLC)** 37:15 everyone.

SIG: JavaScript SIG
Date: 2025-09-03
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 00:29 Nope.
Alright, let's wait for a bit longer and see if anybody returns, and then we can get started.
Hey, Luke.
I guess we can kick it off, sort agenda today. Brent.
The first one is about the new Composer samplers.
**Trent Mick** 02:28 Yeah, I saw someone already commented that they might be another reviewer, and that should be great.
I'm not the author, but I've done a review of this. This is to add support for most of the new consistent slash composable sampling spec that was developed over time in a couple of OTEPs, and not too long ago merged into the spec.
**Marc Pichler (Dynatrace)** 02:58 Awesome. Yeah, I would, also put this one in, the review queue, but I'm, Yeah, if anyone else can have a look before that, I would very much appreciate it. And… Yeah.
If, anyone else also reviews this, I'm fine with just getting this.
merged in without me having a look as well. So, yeah, if anybody has time to look into this one, please do.
It is a spec feature as well, so, need some cross-referencing, usually.
**Carlos Alberto Cortez** 03:38 Yeah, hello, by the way, this is Carlos, Yeah, I am in the sampling group, so I did review this for Java, which is… it's in the spec, but it's development.
So you can easily change, but I think it would be great to get, like, a second pair of eyes. So actually, I'm doing… I've been doing some review of some PRs around configuration in a similar style, and I would like to have this. I don't know if it's too much that you hold on for the rest of the week. Maybe you can merge that on Monday.
I would like to have some days to review these.
**Marc Pichler (Dynatrace)** 04:14 Yeah, I think, there's no particular rush to get this, sorted, so, yeah, getting review from somebody who was involved in this pack is also really good, because then, you already have all the context,
**Carlos Alberto Cortez** 04:30 Correct, yeah.
**Marc Pichler (Dynatrace)** 04:31 No.
Perfect. So…
**Carlos Alberto Cortez** 04:33 Thank you, yeah.
**Marc Pichler (Dynatrace)** 04:33 Very much appreciated. Thank you for taking a look.
Right.
Does anybody else have any topics they would like to discuss?
Or does anybody else have any questions about, this particular PR or the composer samplers?
**Carlos Alberto Cortez** 04:58 Maybe just, like, say the same. I saw that, there are TPRs around configuration, file configuration, specifically.
And I would like to… I started reviewing them, last week, but I didn't grab that up. Likewise, I'm doing the Java review for that.
So it would be good, because you were asking for a second pair of eyes, so I can take a look at that. And actually, the plan would be to finish doing the review for those ones, and right after, do the sampler, the consistent samplers here.
So, yeah, I would like to, yeah, hold in a little bit longer so I can provide any initial feedback.
For the configuration part, it's probably more important, because as you may have seen, we want to make that part stable in the specification, so it's a good time to start, you know, getting feedback now.
**Marc Pichler (Dynatrace)** 05:50 Yes, yeah, the configuration part is also, in my review queue before this PR here. So, yeah, it's obviously good to get, Get some ice on this one.
Alright.
I saw a few more people joined. If anybody has any topics you would like to discuss, please feel free to just put them on the agenda here. If there's no other topics.
Then, we'll go to, triage some bugs.
If, yeah, topic comes up while we're doing that, please feel free to, just interrupt me, and then we can Go back to discussing topics.
Alright.
So, the first one here is… Something that we've seen… A few times already… This one still needs a reproducer.
Yeah, there's probably some, some setup to get this to work. Also, in Webpack, I've tried this with, Rollup, but, Yeah.
there's… It's a bit more involved, I don't think this is actually a bug in the… gRPC export a server.
remove the bug label, I will remove, triage labor as well, and… I'll put the question on.
This issue right here, and… We'll see if the author here comes back to it this way.
Alright, in the meantime, I see there were a few, topics added, so, Aaron, you, pass.
**Aaron Abbott** 08:06 I'm like, for this one.
Yeah. So yeah, this one, I think we discussed maybe, like, 2 or 3 weeks back, But basically, the… the thing was, there's, like, a resource detector in Contrib, and then we had one in our Google-specific repo.
And the decision was to contribute, you know, Google's, like, official one into Contribure, so that they, so that there's only one.
To make things a little easier for people, and also, you know, include it in the default auto instrumentation, get free, you know, you know, free, like.
Large changes, like… like, the SDK2, for example.
So yeah, this PR basically adds that, I wanted to maybe point out a couple things for discussion, but otherwise, I think it's pretty much, like, the dependencies are not changed at all. Just… just the test dependencies, I think, were slightly different. I'm not using NOC.
yeah, added Sanon, Sanon, however you say it. And, yeah, the… the commits are split up, so hopefully it can be kind of easy to review. I split up sort of the parts where I copied in code, did auto-formatting and stuff.
But, the only other really interesting thing is, you know, per, like, typical Apache 2 licensing, I left the Google copyright and added the hotel one.
In addition, I think that should be okay, but, I think that's pretty standard, right?
**Marc Pichler (Dynatrace)** 09:44 Yeah, I think we've done that in a few files already. I think the Oracle… database instrumentation already has a similar setup, so I'm not sure if all the… Yeah, if all your platforms are passing, then the way it is now is fine. Oh, sorry.
**Trent Mick** 10:03 The way it's been done there is… is easier. It works with the… with the linter that we already have for the header, so that's… this way we went. The Oracle way, I can't… I don't recall being in the full discussion, but that one required local hacks to change the… To change the ASLint rule. But anyway, yeah, that's good, the way I have it, yeah.
**Aaron Abbott** 10:22 Yeah, I had to change it from, like, you know, block line comments to block comments.
Which is… which is fine, but it passes the linter now, so it should just, it doesn't get overwritten or anything.
**Trent Mick** 10:33 Yep, yep, correct.
**Marc Pichler (Dynatrace)** 10:35 Awesome.
**Aaron Abbott** 10:35 Thanks.
**Marc Pichler (Dynatrace)** 10:37 Cool.
**Aaron Abbott** 10:38 So, one more thing was, I also sent a separate PR, which is to update the component owners to add some more, like, to basically freshen the list and add more Googlers there, so that hopefully we can,
**Marc Pichler (Dynatrace)** 10:48 Cool.
**Aaron Abbott** 10:51 Yep, make this easy for everybody, but… Yeah.
**Marc Pichler (Dynatrace)** 10:56 Okay.
Awesome, yeah, already merged, so… Good. Thank you for, updating the list there as well. And, for this PR, if, the new owners also want to have a look already, that would also be very much appreciated, and, I guess… yeah, they're going to be responsible for PR reviews and issue triage on these things anyway, so if we can get them, Getting started on this one would be great.
And we take a more hands-off approach on the components in Contrip, where we trust the component owners to do the thing.
The reviewing and stuff like that, so, yeah, awesome.
**Aaron Abbott** 11:42 Okay. Actually, I had one more question on this, which I could maybe ask. So, for the resource detector SDK 2.0 thing, You basically are supposed to return, like, the attributes with the attribute… attribute key and promise, and… Obviously, you don't know what that's gonna be beforehand, so we kind of include… the way we implemented it is There's, like, a list of all the possible attributes, and then all of them get a promise where most of them will be undefined. I hope that's okay. I don't know if that's, In the spirit of… How this was supposed to be implemented.
**Trent Mick** 12:24 Let's take a look. I think it's… I think it's probably fine, yeah.
Okay.
Yep.
**Marc Pichler (Dynatrace)** 12:32 Yes, that's the way I think we did it in all the other resource detectors as well. I think that's very much in line with what the others do as well, so I think that's good.
**Aaron Abbott** 12:45 Okay.
Awesome, well, that's all I had. Thank you so much.
**Marc Pichler (Dynatrace)** 12:49 Thank you.
**MG Marylia Gutierrez** 12:53 It's just, like, somebody asked me a question, but I did not know the answer, and since I haven't touched the logs, maybe someone here knows. They were just, like, looking for patterns, like, on logs, and they gave me the example of the one that exists on Java and .NET.
But I didn't know if we have any pattern for our logs.
**Marc Pichler (Dynatrace)** 13:17 Is that, diagnostics logs, or… Logs exported through the console exporter.
**MG Marylia Gutierrez** 13:24 Yeah, the exporter ones.
**Marc Pichler (Dynatrace)** 13:26 So for the exporter, we don't have, any pattern. I seem to recall that there was an… proposed spec change at some point to add, like, a unified format for logs, exported through the console exporters, or the debug exporters, but I'm not sure if that has gone anywhere.
the way that ours does it, I think it just, That's a console deer, thing on the, on the lock.
record that… the exporter receives, and then just dumps that to the console. It doesn't… Follow any fancy format like this.
Since it's, just intended for debugging, we didn't really, go any further with this, it's very rudimentary. It's not something that, is… is useful in the way that it is right now for running in production as well. So, yeah.
**MG Marylia Gutierrez** 14:33 Hmm, okay. Yeah, those ones, the example are the, like.
console output, simple, or the others, like .NET and stuff like that.
**Marc Pichler (Dynatrace)** 14:42 Inc.
**MG Marylia Gutierrez** 14:43 Cool.
**Marc Pichler (Dynatrace)** 14:45 If there's gonna be any specification on… on that, then… we'll probably be able to just align with, whatever the decision is. We can just serialize it to… Whatever is needed.
Is that, something that's gonna be, that people are thinking of adding to the spec, or is it just something that,
**MG Marylia Gutierrez** 15:10 No, this was, like, an end user that asked me.
So, I don't think it's on specific radar from anybody, but yeah.
**Marc Pichler (Dynatrace)** 15:19 Yeah, it has come up, quite a few times that people wanted to have a standardized format to output to STD out, so that they can use that to, then parse it somewheres, and other adventurous things like that. I'm… yeah.
always, always quite interested in what people are up to with these things.
**MG Marylia Gutierrez** 15:45 Yeah.
Yeah. Thank you.
**Marc Pichler (Dynatrace)** 15:52 Thank you.
Yep.
Guess we can move on to, country pack triage, which… there are no new ones, so nothing to triage, which is good. If… yeah.
If you have any additional topics, please feel free to interrupt me while we go through the pull requests as well.
Actually, we said last.
A few weeks ago, I think, that we are gonna take the one with the most open PRs, and go through this one, and on contrary, we are actually down to 28, which is, quite the achievement on its own. So let's… go and have a look at the open PRs in… The core repo.
Alright, this one here is actually approved.
So this one would be good to merge.
I remember this one, I had a look at this one earlier today, and what is actually happening here is I cannot resolve the conflicts in the changelog file for some reason in the UI, so I will check out this one and update the changelog.
And merge this one in, or put it on my list, and then we should be able to… Get this one merged.
Next one.
This one has some changes requested.
By me, I went through… the older PRs, offline, and made sure to mark them as changes requested, if there's anything, and here, this adds the delegating NOAP meetup provider, but we also need to, have a delegating NOAP for the instruments.
Otherwise, this PR won't have the intended effect of, actually making an improvement there for end users who usually create the meter and then the instrument, directly after they create that.
So… Nothing to do here.
And then we can move on to… This one here, that is blocked on… Things in the milestone here.
One thing that somebody reached out to me recently is this issue right here, which is Audit Logs API for Browser Friendliness.
That is, basically intended to, for people to have a look And see if there's anything we need to do in terms of minification optimizations and stuff like that.
And, yeah.
We would be able to do that still while it's, In, in an experimental range.
So, David, I think you are attending Deep BrowserSeek, right? Is that something that you could bring up with the folks there for them to have a look?
**David Luna Bistuer** 19:44 Yeah.
Sure.
**Marc Pichler (Dynatrace)** 19:47 Thank you for, doing that. I won't be in the browser sig tomorrow, otherwise I would bring it up myself, but I have a conflict with some other meeting there, so won't be able to make it.
But once we get that sorted out, then, There's one more thing in the milestone here, and… then I don't think there's a whole lot left for us to do until we can mark the blog's API and SDK as stable.
So, yeah.
That would unblock this PR here.
Alright.
The next one is, web DR as well. Adding the session handling implementation seems… There was some review.
I think I've also seen them around in the processing, questions. I commented that this is… looks good to merge, so we'll give that another look, but all my comments here seem to be addressed, so I don't expect there to be A lot more, to have a look at once we have that.
Resolved here, then we can also get this merged.
It's my own PR.
It did resolve the conflicts.
Since last time.
If anybody has time to have a look at this one.
Would be appreciated.
And then the next one is… One that has a stale label on it.
Oh.
God, this is not… Updating some of the documentation around the… XNET propagator, I am… Not too much up to speed on the specification on… That one, so… this would require quite some… Some deeper, people are digging to figure out if everything that's written here is actually correct.
Nothing that we can do on the car here today.
But, nonetheless, something that… We should look into.
yep.
And there's a few PRs that, Like, some lint warnings.
Adds a few more types, and does a bunch of other things, Probably also not something that we can cross off the list today.
More easily in the morning changes.
I seem to recall that this was already… URL.parse was already phased out at some point. I'm not sure if I opened the PR to do that, but it might be that this is… A little outdated.
Yeah, seems like… There are some conflicts.
David already commented here.
That was… Wait, some time ago.
There hasn't been any activity. I know the person was just, Working for a company that, got a project from some customer to… for them to contribute to Altair, so I… I think the time just ran out for them.
So I will close this PR here, as it has conflicts, and if anybody else wants to pick up the work that they did here, please feel free to reopen my new PR.
8.
Closing this one… And then we can move on to… The next one. Which is… this one here… It says changes requested on it.
Oaks… Weird.
Was there a force push at some point?
My comment is still, still blocking this one from getting merged.
So, I guess we'll leave that one as is as well.
if I find some time, I will also go in and I usually resolve some of the conflicts myself to make sure we get this on the road. If anybody else ever stumbles upon any old PR, it's also appreciated. If you are an approver, you have Permission to also push to the branches, of… like, these PRs here, and, resolving some of the issues, usually is quite helpful in, getting old PRs merged quicker.
Especially if the person is, not responsive anymore. If maintainer edits are on, you can, also take a shot at… Reserving some of the comments here.
One also still has… Some comments that need to be addressed.
Looks like D.
Just look up these.
So we can… Continue on to the next ones.
This one, I actually promised that I would, talk to Jamie about, possibly addressing some of the comments here in the follow-up, because it's, Bit difficult to make these… work, and I don't want to, like, make a too large change to this example.
But I didn't reach out to Jamie yet, so, it's not something that we can… cross off the list here, this is, the work-in-progress entity prototype.
Yes, we can always just keep that. Renovate PRs.
And then there is one that has changes requested for, allowing any value attributes in the API and SDK logs. This should actually be… Part of the, logs SDKs to build the milestone, so I'll put this on here.
are some changes requested by me, because it is adding this validation to the API, which on itself doesn't really do a lot, usually. So that needs to be moved over as well.
Here is adding advisory attributes, which is actually a spec feature, so I will… Put the spec feature label on here.
tests.
I guess… What's going on here is… Quite some tricky thing.
I think I put the comment here.
Somewhere, at some point.
Something up here. I guess they're looking for some help in troubleshooting what's wrong here.
But it's… Often very difficult to know immediately.
Looks like that was some forced push mishap.
Rights.
Next one, views.
The docs change… Looks like here they accidentally pulled in some of the, changes from another PR, which actually already got merged, so maybe we can just reserve this.
Easily.
Or maybe not, the way that it looks like.
There's no easy way to just accept the other thing, so, I'll actually put my comment here again.
see the notification the second time around, and then… We can also get this one merged.
This here, is a PR that touches some of the, I'm in code, which… I guess nobody really likes to touch.
Because there were some quite long-running, problems with, clock drift, and, like, correcting that clock drift.
And, any change is really, it's really unusually.
Causing some trouble.
But it also seems that tests are failing here.
Oh.
payment tests here are an issue. Not sure if we need to point that out, directly. It is a required check anyway, and I think they… It's usually easy to see if something… out of phase here… Oh, that's OpenTelemetry Pot.
We already merged this in the country repo, but looks like we forgot to merge this one here.
So we're gonna put a skip changelog label on it.
This… France, okay… We can merge this.
And… This here changes something to… Add an explicit, detected and overwrite keyword.
Which is kind of weird, because I thought that we had a ruler in the… In our lint step to prevent… Where's appropriate to go.
It's kind of late in the day for me already, so my brain is not working that good anymore.
This lint base should be the place where this is.
Actually, I will not comment on this CR right now. I have to dig deeper to make sure that what I'm saying is actually correct, but I'm… fairly certain that there's some lint step that should actually catch this.
nope.
And this one we had talked about earlier, we said that we are gonna keep that open for a bit longer, And, next one is… Add Tracer factory option to Tracer config.
I provided an example of how they want to use it.
Like, what they want to do here is actually re-implement their own SDK… This is, really weird.
VR.
But this feels like something that we don't want to do.
I'm seeking to have a tracer factory that gets passed to the tracer provider.
also handles not just the creation, but also the caching manage… caching management logic that I had no desire to re-implement.
So I guess what I will, comment here is… That… that is kind of not… thing that we intend to support right now. Providing a non… Compliant tracer… in the tracer provider, seems like… adding API surface, or… working a very niche use case. Ideally, any optimizations we would do in the actual tracer provider in Tracer, so that… We get the allocations.
Don't… In these spots, rather than, Providing a way to do something like this, and have people create their… Or implement their own, traces.
if anybody has a differing opinion, please, feel free to also comment on the PR here, but I'm… I'm fairly certain that that's not something that we want to do.
Renovate bot again.
Then… There's another PR, Peace insensitive carrier handling. I did review this one.
But it looks like they didn't.
convict.
to actually make the changes that I proposed.
And this gets injected back as, lowercase.
Doesn't really matter for HTTP, but it does matter for any sort of, carrier that, is case sensitive, which… I'm not sure we have that anywhere right now, but, people might have their custom, Set up somewhere where they inject some context into some carrier, and, then… If it becomes… A different string, it might be.
Might be causing trouble for them.
Also.
Put that onto my list to get back to them, and ping them again on.
Please making the changes here.
I'll need… And then, this is the PR pay… earlier that we talked about earlier, about, adding more conf… more… more attributes to the config model. Sorry about not, getting back to you on this one. It's… Yeah, there's quite a few things going on at our times, and I just never seem to find the time to sit down and actually have a look at this one.
The same with this one. I'm sorry for.
**MG Marylia Gutierrez** 45:22 Yeah, hopefully the parts of the config file should be easier to review, in case you want to start with that one first, because it's just, like, adding that package, like, the ML, and then just actually parsing the ones that were already accepted as the config model.
**Marc Pichler (Dynatrace)** 45:41 Yeah, we're, or tried to get the, the door.
Get this, reviews.
In the next week.
Right.
Next one seems to be… Some sort of performance improvement thing.
And very nice that there's actually a benchmark thing that we can run, so, should be fairly easy to figure out.
Whether this is actually… Giving us the improvements that we're looking for, but… That seems like exactly the type of thing that, I was saying would be better to do, rather than adding the, tracer factory thing. So… Yep.
That would definitely… be quite helpful.
Go.
It's nothing that we can just, review and get merged quickly, but if anybody has time, please have a look at this one.
performance improvements are always a bit more difficult to verify, because we don't have any automated runs or anything on PRs.
But if that is something that anybody wants to… Have a look at and, Or to get automated, then please feel free to, start chipping away on that. I think, running the benchmarks on the… on the PRs would also be quite helpful. Not sure if we have enough.
space, though, on the, on the bare metal runners.
To actually… Get comparable results there.
**Trent Mick** 48:03 And not a… there's just one runner. No, and I think they want us to…
**Marc Pichler (Dynatrace)** 48:07 Okay.
**Trent Mick** 48:08 To limit… limit the usage.
**Marc Pichler (Dynatrace)** 48:10 Then, yeah, then in that case, please, everybody forget what I said, and don't automate it on the PRs. We don't want to take the resources away from everyone that wants to actually run this on main, so, yeah.
Would be still cool, though, if anybody can find another solution, I would also… Appreciate that, alright, The next one is… Pr for instrumentation fetch.
Release HTTP connection when response body is canceled.
Just pause.
But… It doesn't look like any… Tissed for the… Behavior that they are trying to… So… Address were added.
So I'm gonna ask them.
**Trent Mick** 49:55 I don't know the current state of the fetch instrumentation. Are we in this pickle because we're only ending the span after a body is read?
Do you happen to know?
**Marc Pichler (Dynatrace)** 50:04 I don't know exactly, unfortunately. I think, what they are running into is that, like, the HTTP connection itself is not released, so what they're seeing is, not a buildup of unfinished spans, but, actually just, us holding on to the HTTP connection somehow, which I'm not sure exactly why that happens.
A test would, in any case, help here, I think. Yep, absolutely.
Also demonstrate what it is that they're fixing.
Please add a test here.
I think it… Yeah.
Or the tests pass here, and then they just added a changelog.
So, yeah.
I guess at some point, the fetch instrumentation will be replaced by something else, or some other fetch instrumentation that is event-based.
But until then… We might still have to, Yeah, it leaks any bugs that come up, until there's a replacement.
Oh… Yes, this is a PR, that I opened. I'd been chipping away on this, in, like.
spare, some spare minutes that I had in between meetings and whatnot. This is a workflow to move inactive, folks to emeritus, it's something that I had been, doing manually for some time.
I just periodically, been going through, the approvers list and, just checking if There have been any, reviews posted in the past, few months, and this basically, does the same thing in, in a workflow. The reason why I'm automating this, it's actually not a lot of work, but it is, Kind of, hard to… to go through and actually open the PR to, yeah, move somebody to Emeritus and take their… their role away, basically. So, this… Basically opens up brain space for me to, look for replacements rather than, Yeah, stress about the remover part.
Yeah, but opened yesterday, so… Or the PRs here are failing you.
Right.
Where will that be?
this, adds this create OTRP patch export delegate, which we just, added recently.
through the exports, and here I'm mostly interested how they're actually using this right now, because most of these things are just used internally.
So it just… wanna know what they're actually up to. There's also an issue to change the exporter interface, and if I know what they are up to, then I know how this is used in Other places, before actually making that new interface, and it can give some good ideas of how to design that new API, so I'd be quite interested in what they have to say here.
In any case, we do already export.
send peaking and, fetch, send peaking and XHR, so adding fetch doesn't be too much of a big deal.
Just wanna make sure that, that's actually what's… And we just want to make sure that it actually helps them.
Achieving whatever they want to achieve before actually adding something to the public exports.
Yeah.
This is, core release, I will postpone this to tomorrow, because it's quite late, in my day already, and If I do it tomorrow morning, then I will have the whole day to deal with any problems if they arise.
And then we have here, PR to add, experimental trace decorator support. This is something that, Sheng Tsung has been working on, and basically it adds this decorator support that works like so.
So you can, like, if you have Some class somewhere, you can add this decorator start active span, and then you don't need to pass in the corpbacks and stuff like that.
Yeah, this is a draft right now, Shang Tsong actually asked to, Have a look at this one, so if anybody has some input on, The approach here are to, save of the API, please feel free to have a look at this one, and put your comments on the PR.
I'm sure he would appreciate some input on that one. And this is also a feature that has been requested quite a few times. I think… There's a limitation right now that it just works for classes, but, yeah.
Doesn't… doesn't work for… for functions right now, but, This is as close to getting working decorators as one can get at the moment. So, yeah.
Anybody has some time, please have a look.
And that is it for the PRs in the core repo. I guess we don't have a lot of time left in this meeting, so, next time we can focus on drip again.
All right.
I guess that's it for today. If we don't have any extra topics to discuss…
**Trent Mick** 58:05 Thanks for running.
**Marc Pichler (Dynatrace)** 58:05 to everybody?
Yeah, thank you, Aura, for joining, and, see you next week.
**Raphaël Thériault** 58:14 Do you agree?
**Jackson-iPhone15** 58:15 Bye.
**Marc Pichler (Dynatrace)** 58:17 Good one, bye.

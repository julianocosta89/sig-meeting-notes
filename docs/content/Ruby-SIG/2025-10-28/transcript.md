SIG: Ruby SIG
Date: 2025-10-28
Duration: 55 minutes
Zoom Recording URL: https://zoom.us/rec/share/u31AOQAv_Rm6Wft5oB8iQ9mTRryXn75q1ZWTeCd0X7Vf1Xrd6Z_j8mhcyNmbbEny.GnbzR_GBohCpqj3X
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 04:17 Hello, everyone.
Welcome, Mark.
**Mark S (Smart Pension)** 04:25 Thank you.
**Kayla Reopelle** 04:39 In the Zoom chat, I posted a link to our agenda. If there's anything that you want to add, feel free to just go ahead and put it on there.
Green.
We'll give folks maybe, like, another minute or two to see if anyone else is joining us.
We're just gonna give it, like, one more minute, see if anybody else is joining us today.
Right, I feel like we are probably good to start then. Let's see…
Shall we just dive into the agenda, or is there anything burning that we want to talk about first? I don't want to put you on the spot for a round of introductions if you're not interested, Mark, but we can do that as well.
Maybe, maybe we'll get to that as time goes on. Alright, so, with the Spec SIG today, I was unable to attend.
It looks like there is…
you know, some work related to, KubeCon, which is coming up in a week or so. And,
This stability blog… It's not something I've looked at yet.
Looks like, okay, this is part of what we discussed last week,
about the, kind of, four OTEPs that might be coming, OTEPs being, like, open telemetry proposals.
To kind of work towards the stability of, the OpenTelemetry project as a whole.
Next up, feedback on the EBPF profile, that's not really for us.
Voting in the OpenTelemetry election, which I have some links for that we'll look at in a minute.
Not sure what we've got going on here.
Oh, it looks like there's some problems with…
The enabled, disabled parameters for meters, which we have not implemented yet.
This was a long time ago.
Okay, I guess it's maybe coming back to life, recently.
So yeah, something to keep an eye on, but until we implement that, maybe, maybe good to wait a little longer until they've decided.
If you're going to KubeCon NA, here is a special schedule for the Hotel Observatory of, like, special events and different SIG meetings that are occurring.
None of the Ruby maintainers that I'm aware of are going to KubeCon this year, so, we don't have any Ruby meetings, but if you do end up going, the people there, what I've been in the past, have all been super nice, and would love to chat and answer any questions you have.
Let's see, so there's two… Sampling-related PRs, too…
Time unbiased Reservoir Sampling algorithm for histograms.
I think we might have looked at this one a little bit a while back.
But we do not have the exemplars merged yet, so…
That's maybe made some… some progress, and the last one…
Add spec for an always record sampler, interesting.
**Wendy Smoak** 10:27 A sample that doesn't sample?
**Kayla Reopelle** 10:29 It would seem to be, yeah.
Have the spans always processed by the span processors.
Interesting.
I wonder… yeah, I'll have to think about that more. I wonder how that's different than just the always-on option.
Okay, is there anything on this list that people want to dive into more before I start talking about the voting?
Alright.
So yeah, so, once a year, I believe, OpenTelemetry has new elections for the Governance Committee. The Governance Committee is kind of more of the community-focused part of the group that, you know, they help support the SIGs, help support the conferences, focus more on, you know, processes and procedures.
You… if you are eligible, you should have been tagged in this post.
Somewhere with your name. If you think that you should be eligible and you weren't,
we can try to figure that out, and or I guess right here, there is…
A form that you can fill out, to request an exemption there.
And, the votes themselves go through this, like, Helios…
app. It's pretty… pretty straightforward.
you just click in here, I think you have to authenticate with GitHub, and then they'll have some different options.
You can vote for up to 5 people, I think there's 5 seats available.
So yeah, the voting ends… did it say when it ends?
Let's see there…
Did not say there. I think it's pretty soon, so I would recommend voting sooner rather than later, like, maybe only a day or two more.
So, just something to keep in mind if you're interested in that.
Okay, yeah, let's… Dive into the agenda, then.
Schwan, yeah, go ahead and… Kick us off.
**Xuan Cao** 12:59 Oh, yeah, I just want to, get, more attention on this, some of the remaining, because I kind of wanted to move on to the exemplar.
Before moving on that, I think there's a couple issues, need to be addressed, first.
And then, yeah, that's pretty much it that I want to bring about today. And then, I think the one that I think, you already…
you already reviewed, but, haven't had another chance to look at, is the merge logic. Yeah.
Yeah, and then rest of them are just followed up for that, for the fixed allegations, I think.
**Kayla Reopelle** 13:42 Okay, sounds good. So, as far as goals go, it would be kind of taking care of these…
Yeah, I know. So that you can move into that.
**Xuan Cao** 13:52 Yeah, and for the refractor, I don't think that's really important right now. I don't even know if that's the case, right, at this moment, because it changes a lot of things.
**Kayla Reopelle** 14:03 Oh.
Cool, sounds good.
**Wendy Smoak** 14:06 I'm watching that one that's still in draft. Cardinality Limit is interesting to me. Does it need more work, or…
**Xuan Cao** 14:14 So…
**Wendy Smoak** 14:15 Back to it?
**Xuan Cao** 14:17 Excellent.
Yeah, I think, I think I'll… I can mark his ready for you.
**Kayla Reopelle** 14:23 Okay.
**Xuan Cao** 14:25 Yeah, but, yeah, comment making.
Pretty clear, yes.
**Wendy Smoak** 14:31 Not an emergency. That's the one thing that's, like… I have no control if someone does something crazy.
And I've got these in production.
**Kayla Reopelle** 14:40 Okay.
Cool. Alright, so… Top 4 is goal.
Yeah, I think I've moved… I've finished up the project that I needed to work on at, my normal job, so I should have more time to review this week.
I guess before we move on… Oh, I also wanted to say, Wendy, I thank you for the updates to this PR. I'm feeling ready to merge it in, just wanted to… Shawan, I wasn't sure if you wanted to take a look as a metrics-related PR, if that was anything.
Before I merged it in, but if not, then… I'll,
I'll ship it out, and I think we can include this in a release, even though, I didn't get a chance to get it in yesterday before the releases were automatically generated.
**Wendy Smoak** 15:42 Thanks.
Yeah, is there anything else? There's been a little more activity on this error reporting, debugging, UX.
**Kayla Reopelle** 15:52 PR, Francis had some feedback.
Robert had some feedback, so,
Yeah, I think if you have other opinions, or are curious about why they blocked it, especially if you've used this and you've run into these problems, like, more feedback from the community would be really helpful.
I'll add this as a list.
And as far as any new issues go…
Okay, I don't think we have anything… New right now.
Yeah, okay, so anything else on the core repo before we move into contribib?
All right, let's, let's move on in. Schwan, do you want to start here?
**Xuan Cao** 17:00 Yeah, per year, because I think, I realized here. Oh, I think, I want to get a,
If it's anything I can do to keep this moving.
**Kayla Reopelle** 17:13 Yeah.
**Xuan Cao** 17:15 Oh, oh, I'll be grateful.
**Kayla Reopelle** 17:18 So, let's see, is there anything…
in particular you're aware of, because I haven't looked at this for a while, that…
You… you know that we need to resolve in terms of questions?
**Xuan Cao** 17:34 on… now from me at this moment, because I also haven't looked at what I respond,
It's, it's like…
5 months ago, so… But is there anything that's still concerned, I will try to address them.
The PR lives on the old interim, she operated, like, long, long time.
It seems they've… they forgot about us, so, hold on.
**Kayla Reopelle** 18:03 Okay.
**Xuan Cao** 18:03 given we? Yeah.
**Kayla Reopelle** 18:06 Sounds good.
**Ariel @arielvalentin (ATX, USA)** 18:07 I will look at it after this meeting.
**Kayla Reopelle** 18:10 Awesome. Thank you.
**Ariel @arielvalentin (ATX, USA)** 18:15 And thank you, Hannah, also, for looking at it.
**Kayla Reopelle** 18:22 Alright, shall we jump in here?
Arielle, what would you like to…
**Ariel @arielvalentin (ATX, USA)** 18:29 Just bringing up some things to the attention. So, my intention here is to fulfill…
give us a faster feedback loop. Right now, what happens is that if unrelated files are changed.
You end up waiting for the entire test suite, which can be very long.
So, what I was hoping that we can do is only run a subset of the suite.
We could be very granular if we wanted, to go, like, you know, only run the test related to a specific change in a specific gem.
As you noted last week, or I think in one of the comments.
One of the problems that we have is that we have these intergem dependencies.
So if you, like, say you edit helpers, or you edit base.
Then… that impacts all of them, and then you don't see the errors, you know, unless you run all those tests together.
So what I did was I sort of grouped
I did a little bit of a regrouping of some of the… The test suite, so…
You know, for example, like, all of the ones that were, like, checking spelling and markdown and all this stuff, I rolled them all up into one.
And then I'm… we're only gonna run those checks when markdown files change.
Similarly for, instrumentation, that's gonna be… that's changed now to only run the All Gem, because the All Gem's the only required build that we have right now.
And I've moved all of the other instrumentation gems into, full.
Effectively?
So, all will run all the time.
But, the…
instrumentation Full, I guess I… maybe not a good name, but it's the one that has all of the gems that don't have it… that don't require any services running in the…
Action? The action container?
So these are gonna be all your in-memory tests.
They're all gonna be bundled up together.
And then similarly, the one with the services, this is the one where… only helpers?
If instrumentation bass changes, or if any of the services that require something like Kafka or
you know, Memcache or Redis, all of those are required services. They're all gonna run
If any changes happen to those gems.
I couldn't figure out a nicer way to say.
Hey, run these dependencies with each other.
You know, so, as you can see, the paths include…
Oh, and I even messed that up, you see? This is the problem with the duplication. Maybe I… I gotta figure… maybe I should be using, anchors.
But effectively, when a pull request is opened up, so this is still… needs work. So could you put this back in draft? Let's put this back in draft, it's not ready.
See, that's what happens when you look at code together, right?
**Kayla Reopelle** 21:36 Reveal.
**Ariel @arielvalentin (ATX, USA)** 21:37 You find out that you didn't do a good job.
So what I'm gonna do in this case is that I'm gonna… I'm gonna introduce anchors into those and see…
That way we could get rid of some of that structural duplication in there, and…
Prevent ourselves from getting a headache.
Okay, so we can put that… but I guess, you know, Sean, you had mentioned in the PR, I don't know if you had a chance to see my response, I think that the biggest challenge with doing, sort of, like.
Only running a subset or just one file is that we… and right now, we have the problem of, sort of, like, the dependency hierarchy.
And, we want them to all… we're gonna have to… I don't wanna…
I'm worried about making it too complex by saying, okay, only look at what was changed, only run those that were changed, but then also find the dependency tree.
To run them all together, right? If we were trying to, like, really be very granular about only run tests for this specific gym.
As opposed to a group of gems together.
You know, I hope that that's, suitable, satisfying, or…
If you have any other concerns.
**Xuan Cao** 22:49 No, no, I also saw where some of the, the issue you were… you're talking about, yeah, that NSC3 is not a good idea in this case.
**Ariel @arielvalentin (ATX, USA)** 23:02 Okay, so if we're in agreement and that's okay, I'm gonna go ahead and put this back in draft, and then…
I'll make the necessary changes.
And, you know, get back to y'all about it.
**Kayla Reopelle** 23:23 Sounds good. Thanks for working on this. I think the amount of time that it takes for the CI to run, especially when you have to merge main into the branch to, like, make the whole merge…
possible. It's, takes a long time, and I think that really slows us down for getting new stuff out, so I'm really excited for this.
**Ariel @arielvalentin (ATX, USA)** 23:43 Fantastic.
And… and Kayla, as you predicted, slash pointed out,
that refactoring that I did, where I pulled all the Ruby versions into an external file and kind of just read them.
Led to… anytime I bought the Ruby Gem version, none of the toys didn't discover that the gems needed to be updated.
So, I said, okay… Let's, go back to having a script that bumps through the Ruby version.
**Kayla Reopelle** 24:14 And so now, instead of…
**Ariel @arielvalentin (ATX, USA)** 24:16 you, updating the one file.
And then having to force a release for all the gems.
You know, run a script, give it the gem version, it'll go through and update the gem version in every gem spec in the repo.
And that'll force, and then, you know, that'll…
That'll end up, like, triggering changes with, whatchamacallit, toys.
And toys will see, oh, you, you…
You need to release a gem, though.
**Kayla Reopelle** 24:56 One thing, just looking at it quick right now, I wonder if we should call it out in the contributing file, that this is the approach.
So people know how to update it.
**Ariel @arielvalentin (ATX, USA)** 25:10 Yes, please leave a comment, and I will address that.
**Kayla Reopelle** 25:13 Okay, will do.
Alright, awesome. Thank you for working on this.
Yeah, I'll take a look at that.
What about this one?
**Ariel @arielvalentin (ATX, USA)** 25:26 Okay, so, I've run into a pro- we're running into a problem right now where…
Fastly has, like, this, patch API.
And what people do in code is they manually patch oh, Faraday.
to include an additional non-standard HTTP method.
So, there's constraints in the instrumentations right now that…
won't allow you to use a non-standard HTTP method when you're…
instrumenting the application. Like, if you look, it's like Faraday's like, oh, it's got a map.
And, according to the spec, the default behavior is, if you're not… if we don't find…
a specific HTTP method, it should end up being other.
Instead of the instrumentation not working.
And then the other thing is looking at, sort of, HTTP client span names.
Because, the instrumentation right now, all it says is HTTP posts, which doesn't match what the current SUMCOM is.
Or, you know, HEV's method.
The recommendation is for it to be on the URL template.
or the RPC method and framework, whatever, for client spans.
Or, you know, for database bands, as you know, it's probably… it's like the select statement with possibly the table.
So I said, okay, so,
If we try to implement that.
behavior, then what I would want to see is something like, you know, adding a, say, a helper method here that's, like, for all of the HTTP clients to use, that given this set of
attributes… the request method, a URL template.
Rename the span, or provide a name for the span.
That wouldn't match that templated route.
So if we look at the specification, and looking at this example of how it's written,
the span name would eventually be whatever the URL template value was.
And it also has the fallback behavior, so you can see, one example is, like.
hey, you passed in, your client made a request, and it has a URL template attribute.
which is that path, you know, user's ID or whatever.
The span name will be… the spam name that we desire will be getUser's ID.
Because it's gonna be the HTTP method and the low cardinality templated route.
Whereas if you have an instrumentation that did not have
the URL template in it, it would simply be the HTTP method.
And in the case where there is an unknown
HTTP method, you would support it, and…
it would show up just as HTTP, so in the case of, say.
Fastly, if somebody was using the Purge method.
which is a non-standard method. What should be displayed as a span name is HTTP, not the… not the purge.
That's how… at least that's how I understand the specification.
And so we have, like, this hybrid, also, of pre-Semconf and… And some common 1X.
And so the idea here is to support both, so given the attribute map, it'll look up SIMCOM1X first.
fall back to SEMCOM Pre… And then, use URL template, which is part of some conv1X.
And try to assemble that together if possible.
And that'll produce a span name, and then what we could do with this helper is put them in all of the different…
Drivers, so Night HTTP, Faraday, and so on and so forth.
And then all of the client spans will now get this name.
As opposed to only having the word… the literal HTTP and the method.
There.
Also resolving the problem that I have, which is…
That we can't find… you know, if it doesn't find the method, the instrumentation doesn't work.
Or, you know… .
**Kayla Reopelle** 30:10 Bing.
**Ariel @arielvalentin (ATX, USA)** 30:12 So, that's,
that's what I'm trying to address here. I don't know, you know, we also have the other circumstance, so, like, I started with HTTP, I don't know if this is the right interface, so this feels very experimental to me right now.
Because we also have, like, this… this all came about, really, because…
Of that fastly situation, and then the second thing was…
you know, we use the TWARP RPC framework.
Which is built on top of HTTP, which uses Faraday, and we were trying to figure out, oh, how do we instrument the client side?
And the simplest thing for us was to say, well.
we can provide the URL template.
And then, in the collector, we'll take the URL template and rename the span.
But then we said, wait a minute, but in these circumstances, if the client library already has ways for us to inject these things, can it…
Can we have the client libraries rename the span themselves?
To the best of their ability to meet what the specs description is…
And that's… this is my feeble attempt at trying to, like, create a helper that does it. I know it adds more complexity by adding yet another helper.
But what I'm hoping to do is get… is reduce some of the structural duplication that we see.
In the… in the client libraries.
**Kayla Reopelle** 31:39 Okay, nice. Thanks, thanks for explaining that. I think I'll have to take a closer look to… and, like, look at the SEMCOM and everything to kind of understand it more.
One question I have is, have you explored at all using the new SEMCOM stability opt-in environment variables that were recently released for the HTTP libraries?
**Ariel @arielvalentin (ATX, USA)** 31:58 No, that's gonna be a big…
migration for us. It's a lot of work, and…
we might be stuck at a particular frozen version after February.
**Kayla Reopelle** 32:11 Okay.
**Ariel @arielvalentin (ATX, USA)** 32:13 Because…
**Kayla Reopelle** 32:14 There is that dupe option, but I know that that has its own problems because of cost, but it's there to help with the migration.
**Ariel @arielvalentin (ATX, USA)** 32:23 Yeah… Yeah.
**Kayla Reopelle** 32:27 Okay, yeah.
**Ariel @arielvalentin (ATX, USA)** 32:27 Yeah, just wanted to point it out there. The problem for us is that it's also the logging signals.
So, the log signals have pre-calmed as well, and we're trying to do our best to keep those in sync, and logs is already, like, super expensive for us.
**Kayla Reopelle** 32:45 Oh, are you using OTEL logs or different logs with the…
**Ariel @arielvalentin (ATX, USA)** 32:48 No, we just… we only use the semantic conventions as part of, like.
as part of the logging formats, right?
**Kayla Reopelle** 32:56 Thank you.
**Ariel @arielvalentin (ATX, USA)** 32:56 We tell people, hey, for… if you're gonna use,
If you're gonna use a, record HTTP method, record it as a HTTP method.
And we don't have a migration story for saying, okay, now for log attributes, whatever you've done.
go and move them over. And so we don't want that asymmetry.
**Kayla Reopelle** 33:14 Okay.
**Ariel @arielvalentin (ATX, USA)** 33:15 Because that makes it a little bit difficult for us. So I think we're gonna be stuck for a while, and even if we switch to the mode where, like, the instrumentations are emitting…
You know, some conv 1?
I think we're gonna have to, in the collectors, revert them.
**Kayla Reopelle** 33:33 Hmm.
**Ariel @arielvalentin (ATX, USA)** 33:34 For pre-1.0?
Just to keep everything in sync with each other, but that's not your problem.
**Kayla Reopelle** 33:39 Yeah, yeah.
**Ariel @arielvalentin (ATX, USA)** 33:40 So, anyway, so the reason why I did it like this was to avoid the structural duplication.
**Kayla Reopelle** 33:46 of habit.
**Ariel @arielvalentin (ATX, USA)** 33:47 An old and a new.
**Kayla Reopelle** 33:49 So, we'll.
**Ariel @arielvalentin (ATX, USA)** 33:50 Kind of, like, the idea here is, if we look at the implementation of it.
it'll prefer new over old, I hope so.
Now that I'm saying it out loud, wait a minute, I could be wrong. Sorry, we just… you skipped all of it. This is mostly, like, gem nonsense. Oh, yeah, yeah, so there's an example, like, test case and stuff.
Of, like, you know, if you gave it…
a request method with, you know, some common new, and the URL template, this is what the result's gonna be.
If you use the old post with the URL template, this is what it'll be.
And so on and so forth. And so, like, if you used, HTTP request put.
that, you know, SEMConv, you know, the line 17, that test case, if you use SEMConv1 with, pre-SemConv.
Semcomp 1's gonna win.
In that case, because there is no dupe.
**Kayla Reopelle** 34:46 Family.
**Ariel @arielvalentin (ATX, USA)** 34:46 It's like, one of them has to win.
**Kayla Reopelle** 34:49 Right. Yeah.
**Ariel @arielvalentin (ATX, USA)** 34:50 And in this case, I'm gonna assert that it's gonna be some comp 2 that's gonna win.
Or some kind of 1.0, or whatever.
Because I don't think that dilemma's resolved in the…
The already been mentioned in the specification. Yeah, these are attributes and not for span naming, so I chose the…
the la- you know, I chose to, do that.
Now, Again, if it's a thing where it's like, that's the one collision case where it's a dupe.
Versus new or old, right?
So in my case, Dupe would end up always winning with one.
But those are all the test cases, basically. Like, what it's gonna look like if you were to submit it.
And And that's it, and I mean…
Yeah. Again, this is a helper library, so it would be… added to… as a dependency.
I mean, it could be, you know, it might be more complex than we need it to be, you know, it could be part of base, I don't know, but I was just like…
You know, why not just add more gems?
**Kayla Reopelle** 36:05 We're so welcoming to gems, add all the gems, yeah.
For sure.
Okay, cool. I… yeah, I don't have any other questions right now. Anybody else?
**Hannah Ramadan** 36:23 I'll take a look at this as well, would this make sense to…
add into, like, that other semantic convention gem we…
**Kayla Reopelle** 36:32 Mmm.
**Hannah Ramadan** 36:32 Released, just for…
**Ariel @arielvalentin (ATX, USA)** 36:35 The Webweaver one?
**Kayla Reopelle** 36:38 Yeah.
**Hannah Ramadan** 36:38 Yeah.
**Ariel @arielvalentin (ATX, USA)** 36:40 They feel like there's a close affinity. Is that one in the… Main repo?
**Kayla Reopelle** 36:46 Yeah.
**Ariel @arielvalentin (ATX, USA)** 36:48 So yeah, there probably is a close affinity there.
And I don't know if it makes, like…
If these are utilities that belong on the packages themselves.
But maybe you're, you know, Ana, maybe you're right, it's like, maybe this functionality belongs there and not in here.
But the only reason why I brought it up is because I was like, oh, this is like…
Instrumentation things, which is not…
**Hannah Ramadan** 37:15 Yeah.
**Ariel @arielvalentin (ATX, USA)** 37:16 Which is dead.
There's, like, this weird relationship between, like, a SEMCOMF package, and… the instrumentation.
**Hannah Ramadan** 37:27 Yeah, I think Q might be… yeah, I was just thinking, like, all semantic…
things together, but you're… there's a difference in how.
**Ariel @arielvalentin (ATX, USA)** 37:38 I mean, there's… you know, we're trying to keep the rules together, I just… it's like this thing where it's like, okay, now the SEMCOM package, like, if more utilities get added here, for example.
I don't know what…
yeah, I don't know what to do. Like, some of these libraries use request objects, some of them use hashes, some of them use, like…
I… I'm not… I'm not entirely sure. So maybe… but again, maybe this refactoring is not the right thing, and…
Or maybe introducing it this way is not the right thing, and we…
put it in that… in the Webweaver one? I don't know.
I don't know why I call it a web weaver.
**Kayla Reopelle** 38:12 package of, I think it's, like, a HTTP utilities package, or maybe something in common. There's one other thing in the core repo that's kind of, like, HTTP instrumentation specific.
But I don't remember what exactly it is, so… Potentially another.
**Ariel @arielvalentin (ATX, USA)** 38:31 Yeah, that's the client context one, which…
So… I kinda feel like there's gotta be something done about that.
Yeah. We're all together.
**Kayla Reopelle** 38:41 Yeah. I don't know why it's in the core repo one…
Yeah, it might have just been, like, a leftover from when they were all together or something, I don't know.
**Ariel @arielvalentin (ATX, USA)** 38:53 But…
I don't want to drag it on too much. Ana, your point is taken. I'll take a look at the SEMCOM repo, and sorry, Arjem, and see if we can fit it in there.
**Kayla Reopelle** 39:07 Thanks, sounds good.
Alright, I think that's… that's our full agenda at the moment.
Is there anything else that people want to talk about? We still have some time.
**Wendy Smoak** 39:28 Did we look at just the open list?
**Kayla Reopelle** 39:30 Oh, no, we didn't.
**Wendy Smoak** 39:31 S&PRs in contract.
**Kayla Reopelle** 39:37 Okay… Yeah, there is this, new instrument PG Connect PR that I have not…
looked at yet. Thanks for taking a look, Ariel. Looks like there's some test failures.
Let's see… oh yes, this one, I think this one's ready to go. I just kept missing the window of other PRs getting merged in to be able to merge it in. So I'm gonna merge it into base right now, and when that gets cleared…
we can… we can get this in as well. Thank you for… for sending this in. Yeah.
**Wendy Smoak** 40:14 Yeah, like a release of that, I've got… I need to use it in a project that will be…
Frowny about using an internal tag thing.
**Kayla Reopelle** 40:21 Okay, cool. Yeah, we can… we can do that.
Let me just add that to the notes so I don't forget.
Alright, what else we got on here?
Yeah, Hannah will take a look at this one together.
I saw there were some comments that you made on the factory-bought stuff, Arielle, was there anything you wanted to discuss?
**Ariel @arielvalentin (ATX, USA)** 40:55 So, I think what we're trying to resolve here, again, with the… Effect… with… with, like, these… instrumentations around…
libraries, like, test libraries? So, Thompson, Tomo, I think, is the handle?
Was wondering, hey, could we be looking at…
The potential for having more generic…
Test standards, sort of like test packages, test name.
Or including these in the test name, but for me, it feels very… these…
**Kayla Reopelle** 41:40 Oh, are you there?
**Ariel @arielvalentin (ATX, USA)** 41:54 Hello?
**Kayla Reopelle** 41:55 Hi, welcome back.
**Ariel @arielvalentin (ATX, USA)** 41:57 Yeah, so AWS East 1 is probably having problems right now, sorry.
Or AT&T, whoever.
So we started, we, you know, it's the bike shutting situation where, we're saying…
Factory Bot is a very specific implementation of…
of a design pattern, a testing pattern, as opposed to it being… it's really hard to say, like, is this a domain concept?
Our object mothers, and… Object builders and factories.
You know, are all of these things really generic enough?
For us to have a… Standard specification attributes?
Right, because the concept of trait is something that is a DSL-specific thing for factory bot?
As opposed to, I have some other object mother or builder pattern that I use in, say, Java.
where I will compose an object, like…
And then, you know, part of me is kind of like, oh, a lot of this feels a little bit like profiling would be a better fit.
**Kayla Reopelle** 43:17 Hmm.
**Ariel @arielvalentin (ATX, USA)** 43:19 Around trying to figure out why is my test setup generating so much garbage?
But, you know, I don't… I also don't want to discourage the use case of tracing for, you know, test environments.
And people seeing, like, where they can improve their test speeds, it just feels very…
you know, whenever we're kind of like, oh, I…
I'm trying to trace what Factory Bot is doing. It feels very much like, I want to profile Factory Bot.
**Kayla Reopelle** 43:48 Mmm.
**Ariel @arielvalentin (ATX, USA)** 43:49 In some way. So I don't know.
So, I'm not a… I'm not against the idea of adding an instrumentation for it.
I… it just seems very much like, very experimental.
I feel the same way about the R-Spec instrumentations in general.
**Kayla Reopelle** 44:08 Yeah.
**Ariel @arielvalentin (ATX, USA)** 44:08 It's, like, very experimental, and I don't know…
But I did, you know, all I did was pose the question, like, is anybody… are there any other libraries out there? Like, is there the factory bot, C-sharp or something? And is somebody instrumenting that?
And if so, you know, maybe we can have some synergy there, but I'm not necessarily blocking the PR.
And there isn't anything specific about this that I'm… Concerned about, personally.
**Kayla Reopelle** 44:34 Yeah.
Okay.
Sounds good.
**Ariel @arielvalentin (ATX, USA)** 44:40 I did leave some blocking comments, I think, which were around…
you know, they created the gem file with a, you know, 1.0, or, like, 0.1, or whatever. I was like, no, no, no, just… those are the things you gotta clean up, but…
Nothing else, really.
**Kayla Reopelle** 44:54 Okay.
Sounds good.
Yeah, I'm very interested in Simi's comment, so we'll see,
Maybe we can get some response on that, too.
That might help us understand.
Yeah, the profiling versus tracing situation.
**Ariel @arielvalentin (ATX, USA)** 45:17 And then the RSpec ones, I messaged Chris Holmes to see if he can get some input in those, because…
Yeah, I don't, you know, we need the people who…
Contributed the gems to be maintainers, and if we… we need a process in which there's a handoff or sunsetting.
Like, you know, we have the RSpec instrumentation, but we can't keep up with it. We can't keep up with.
**Kayla Reopelle** 45:43 Every time.
**Ariel @arielvalentin (ATX, USA)** 45:44 So, you know, if Chris is not able to maintain it, then maybe,
This contributor is willing to…
take it on, but we would still need somebody with, you know, RSpec expertise and usage to do the reviews.
**Kayla Reopelle** 45:59 And I think, yeah, maybe…
maybe once the pending PR reviews are taken care of, taking a look at how to…
get the actual people who we have listed as the owners of the gems automatically tagged as the PR… on the PRs, you know, taking that code owners and…
integrating it better with the CI. That was something I started a while back, but didn't get a chance to finish, so…
**Ariel @arielvalentin (ATX, USA)** 46:24 Oh, do you have a draft?
**Kayla Reopelle** 46:27 Somewhere. I'll dig around for it and can share it. I think the first step was actually making sure that everyone was a member of OpenTelemetry. So,
that's a number of comments that I just need to send out and make happen.
And then after that, I think there's hotel admin stuff that's already set up, so…
I'll work on digging those things up once I've taken a look at metrics and the new PRs and stuff like that.
I'll set a note.
Joo…
**Ariel @arielvalentin (ATX, USA)** 47:13 Yeah, that was gonna be, next on my list.
**Kayla Reopelle** 47:16 Oh, yeah?
**Ariel @arielvalentin (ATX, USA)** 47:17 Yeah, because I wanted to try to do something to help With pinging maintainers.
**Kayla Reopelle** 47:23 Yeah.
**Ariel @arielvalentin (ATX, USA)** 47:24 And then for us to have the sunset process in place of saying, like.
**Kayla Reopelle** 47:27 Yeah.
**Ariel @arielvalentin (ATX, USA)** 47:28 We're gonna mark this as deprecated if no one's able to support it.
**Kayla Reopelle** 47:32 No, no.
**Ariel @arielvalentin (ATX, USA)** 47:32 off, right?
One of the most, recent ones is, like, I opened an issue for Ruby Kafka.
Because Zendesk is no longer supporting it.
**Kayla Reopelle** 47:41 Right.
**Ariel @arielvalentin (ATX, USA)** 47:42 So, I don't feel like we need…
We have the urgency to continue to support that instrumentation.
**Kayla Reopelle** 47:48 Yeah.
**Ariel @arielvalentin (ATX, USA)** 47:49 And so we need a sunsetting process around that as well.
**Kayla Reopelle** 48:01 Yeah, sounds good.
Okay, contrib issues, we haven't looked at those yet.
Speak, speak of the issue.
**Ariel @arielvalentin (ATX, USA)** 48:18 Double, right?
**Kayla Reopelle** 48:19 Yeah.
Cool.
**Ariel @arielvalentin (ATX, USA)** 48:32 There's nothing new.
**Kayla Reopelle** 48:34 Yeah, nothing, nothing else.
So, yeah, I suppose as some follow-ups, you know, outside of the reviews,
I will work on getting a release out for,
the metrics SDK to include the new export logging and the logger instrumentation, so that we're getting the formatted message out there.
And then review a whole bunch of PRs.
Yeah, I guess last call. Anything else folks want to discuss today?
**Ariel @arielvalentin (ATX, USA)** 49:20 Mark, did you have anything to add? Thank you very much for joining the meeting.
**Mark S (Smart Pension)** 49:23 Yes, hello.
I thought I'd finally, make an appearance,
I've just mostly been lurking around in the channel, but Arielle in particular has helped me out a lot with our journey to open telemetry. I'll just give you a very quick introduction to the company and what we're doing, kind of. So, I'm the lead SRE for
pension SaaS, and they basically… it's quite, you know, we… primarily the UK market is where we're in, and we provide,
you know, the software for, as our own brand, which is, you know, the Smart Pension.
company, but we also do white labels for some other clients as well, so, you know, they sell it on as their own product. We're a rail shop, we've been that since the beginning of time, and we've been quite…
M…
meshed in with Datadog, so we've used all the native clients. We are primarily… we use Datadog at the moment, but, you know, having seen
OpenTelemetry, I think it was last year, it looked like it got to a kind of a maturity level that I was willing to kind of dip our feet in.
This year, we've just basically been looking to start removing all the hard dependencies on Datadog.
start using, OpenTelemetry, hopefully reduce our, our, observability pipeline as well, because we also have Fluent in the mix, just to make things fun, so hopefully we're going back down to one… one agent, one collector. But yeah, it's,
there's a lot to do, and also it doesn't help that I'm kind of… I can about read Ruby, but I'm definitely leaning on one of our development teams to kind of help out. I'm primarily an infra person, but I'm trying to catch up to speed. I figure this is probably a good SIG to kind of…
catch up and keep up with things. But, yeah, nice to meet everyone.
**Kayla Reopelle** 51:25 Oh, it's great to meet you, too. Thanks for joining us.
**Wendy Smoak** 51:28 Same rails, switching over from online various cloud vendors to…
All self-hosting and everything, so you will, you will have company.
**Kayla Reopelle** 51:45 Fantastic.
**Ariel @arielvalentin (ATX, USA)** 51:49 Did you get to meet everybody else, Mark?
Did you get to meet everyone else? Like, Kayla, did you ever meet Kayla, or Hana, or Schwan?
**Mark S (Smart Pension)** 51:57 No, I don't think so yet. I've seen, I recognize, like, I know I've seen Wendy in the channel a few times, and I think, Kayla, you may have merged one of the
PRs that I kind of a really quick one, just to kind of pin the SDK down.
**Kayla Reopelle** 52:13 Oh, thank you for submitting that, nice. All right.
**Mark S (Smart Pension)** 52:16 Oh, well, after all pointed me out in the right direction, I was happy to be the fingers.
Nice. Well, yeah, let's… we have a little bit of time. I'm…
**Kayla Reopelle** 52:26 I'd love to do a round of introductions. So yeah, I'm Kayla, I'm based in Portland, Oregon. I work on the New Relic Ruby agent, and New Relic wants to support OpenTelemetry, since more and more of our customers want to use it, so I'm here to kind of help…
yeah, help maintain, help bring metrics and logs up to stability. That's kind of the main thing that I'm being encouraged to work on, but,
Yeah.
Happy to be here.
**Hannah Ramadan** 52:54 And I work with, Kayla on the New Relic Ruby agent, but I'm in San Francisco, so it's the kind of same thing, here, to help New Relic kind of, like.
like, stay in tune and keep up to speed. Mostly been doing semantic conventions work.
on OTEL.
**Ariel @arielvalentin (ATX, USA)** 53:18 Now, I guess that's me, because we're not popcorning. So, I am Mariette, and I've been helping out on the channel. I work for, GitHub, so…
Please use all the co-pilot features so that my stock keeps going up, and, Juan, you're not…
**Xuan Cao** 53:36 Hi. Basically in, province of Canada. I mostly work on the matrix.
**Ariel @arielvalentin (ATX, USA)** 53:49 Well, then I guess…
**Wendy Smoak** 53:49 I'm Wendy.
**Ariel @arielvalentin (ATX, USA)** 53:50 Oh, hello again.
**Wendy Smoak** 53:52 And, in a,
I'm at Maxia, we're not a vendor like many of the other maintainers are, and I'm not one of the maintainers, I'm just trying to get my stuff to work, so hanging out in the channel, asking a bunch of questions.
So, happy to see more peop- more users show up that can,
Have different scenarios, try to figure things out.
There's so many channels, that's the one thing. I have this question, I don't know where the people are.
Pick one of them.
**Kayla Reopelle** 54:23 Yeah.
It's a massive operation. Yeah, there's… there's so much to explore and figure out. What… what meeting, what channel, what repo, but .
**Wendy Smoak** 54:35 Every time something comes up here, there's, like, every time I come and you pull up various issues, like, there's always another concept that I'm like, okay, I've never heard of that, I should go Google it and see what that is. Yeah. Like, the operator, I just don't know.
this… All kinds of new things trying to fit in my brain.
All right, and yes, we need the sunsetting process, too, so that we don't feel so.
**Mark S (Smart Pension)** 55:00 So that we're happy to accept new things without worrying about it in advance, and then we have a plan, too.
**Wendy Smoak** 55:07 You're not gonna stay around and maintain that one.
Then we will.
Gracefully make it go away until someone shows up to fix it again.
**Ariel @arielvalentin (ATX, USA)** 55:19 With that, friends, I'm gonna say goodbye. Y'all have a great day, and hopefully we see each other next week.
**Wendy Smoak** 55:24 everyone.
**Kayla Reopelle** 55:25 Bye. Bye.

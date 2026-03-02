SIG: Ruby SIG
Date: 2025-10-14
Duration: 34 minutes
Zoom Recording URL: https://zoom.us/rec/share/Tu-xZMF9nRvUzeQzbGu0JzzzJ431qTebrTw_AMoWA8EoaMORCxNvW-5BFrD16QiY.hLfPqliCcVx1qiFl
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 00:25 Hi, Wendy.
**Wendy Smoak** 00:48 Hello.
**Kayla Reopelle** 00:50 How's your day going?
**Wendy Smoak** 00:53 Pretty good. I've got the logger bridge on staging for one of our apps that we haven't gotten around to, switching over yet, so… looks good so far.
**Kayla Reopelle** 01:02 Nice! Happy to hear it.
Yeah, it's kind of surreal that the package is actually out. I hope that I can spend some time this week, like, cleaning up all the places where,
I'm encouraging people to use my branch and, like, install it from Git.
**Wendy Smoak** 01:19 Yeah, I kind of had to figure out… I thought we decided it wasn't going in all, is it… but the release notes make it look like it's in there, so I wasn't sure what exactly happened.
**Kayla Reopelle** 01:29 Oh, interesting.
**Wendy Smoak** 01:31 It's on the… check… look at the release notes for all, I think. That's… I saw it.
**Kayla Reopelle** 01:37 Oh.
**Wendy Smoak** 01:39 But maybe it's not really in there?
**Kayla Reopelle** 01:41 Interesting. Yeah, it shouldn't have…
**Wendy Smoak** 01:45 M.
**Kayla Reopelle** 01:46 I think it was included, but, yeah, I'll take a look at that.
**Wendy Smoak** 01:53 And I just asked Cursor to, like, tell me how to use this, with, like, the minimum… I just pulled up the code, because I wasn't…
Sure, if there were instructions anywhere.
**Kayla Reopelle** 02:05 Let's see…
**Wendy Smoak** 02:05 I did have to do use, like, say, c.use the plugger instrumentation, so, like, it didn't do anything until I did that, so that's good.
**Kayla Reopelle** 02:15 Okay, that's.
**Wendy Smoak** 02:16 Which was the main thing, we didn't want it to just magically start.
**Kayla Reopelle** 02:20 Yeah, I don't know how I missed that, or if somebody else merged it.
Oh, somebody else merged it. Okay, interesting. I'll look into that. It might have just been a leftover…
commit thing? Like, there might have been something else that was updated and all that wasn't logger.
**Wendy Smoak** 02:40 I'm not at my computer right now, I would pull it up, but I was pretty sure I saw it in those release notes, which…
**Kayla Reopelle** 02:44 Oh yeah, yeah, it was in the release notes, but that could have happened automatically.
**Wendy Smoak** 02:48 Okay, yeah.
**Kayla Reopelle** 02:49 Okay, yeah, it's not listed as a runtime dependency at all, so I'll clean up that release note. That should be like that.
Hey folks!
Cool. I can share my screen. I don't know if we have anyone else joining. Oops, let me actually share a different screen.
I don't know if we have anyone else joining us today.
Lyudmila, hello! Nice to see you here.
**Liudmila Molkova** 03:31 Hey, nice to see you. Am I in the right call? Is it a.
**Kayla Reopelle** 03:34 This one's the Ruby SIG.
**Liudmila Molkova** 03:37 Oh, I'm sorry.
**Kayla Reopelle** 03:38 It's okay.
**Liudmila Molkova** 03:38 uncle.
**Kayla Reopelle** 03:39 See you around. See you around.
I'm surprised that doesn't happen more often.
Alright. So, yeah, we have no Arielle, and no Eric, and no Hannah. Hannah's at an appointment today.
The spec SIG today… we got a new version of the spec being released.
And…
let's see, so the trace ID ratio-based sampler kind of switcheroo is, actually getting deployed now, so…
In this,
we don't need to take any action right away. I don't think we have to take any action until 2027. But, the plan here is that our existing trace ID ratio-based samplers can stick around.
But eventually, we'll also need to add the probability sampler, which is the one that aligns with the now-specified algorithm.
And then, at some point in 2027, we just kind of…
do a switcheroo and replace the trace ID ratio-based sampler with the new probability sampler.
So that's something to plan for. Actually would be a good thing to make an issue about.
Probably.
Let's see, what else do we talk about?
There was very brief discussion on extending the set of attribute value types.
And, this is that any value.
PR that's been talked about a few times. Mostly, it was just a request for additional reviews and more feedback. I think they're getting close to merging this one in.
the,
The one… the discussion for the bulk of the meeting was this proposal to add span events for network phases breakdowns. So, basically, adding an event related to DNS resolution, TLS handshakes, TCB connections, and include timestamps inside of those events.
There was a lot of…
pushback about this idea, and concerns, you know, about using span events since they're deprecated, and also
you know, trying to understand the merits more broadly. I think this is also coming from a mobile context, but the next step plan is for someone to make a prototype, and I think the,
I'm not sure if this is an OTEP or a SPEC exactly, but it'll continue to get resolved at that point. If you have opinions about this, though, or need it, I think it'd be a great time to kind of speak up to try to shape this.
And… oh, this is something I wanted to make sure you knew about, Schwan. They are adjusting or recommending a slightly different sampling algorithm for exemplar reservoirs.
I don't know if this is included in the exemplar PR that you opened, but it seems like a pretty…
Small adjustment, just based on the coding example.
They didn't discuss it too much, but it also…
hasn't been merged yet, it was kind of…
one of those. Please take a look. Situations.
I guess they want to merge it by the end of the week, unless there's anything new.
And if you are going to the KubeCon North America conference, there's a sign-up form if you want to create an event at the Hotel Observatory.
And, GC collections are… or elections are happening soon, so keep an eye out on your email. If you want to vote. The nomination deadline is this week, if you want to nominate anyone for the GC.
So that's that. Let's see… we…
our… just to kind of skip over core, since we don't have any bullet points there right now, Ariel is planning to merge and release the PR that would raise the minimum Ruby version to 3.2 and the minimum Rails version to 7.1 sometime today. So,
Keep an eye out for that. It'll be…
A bajillion new gems with,
a minor bump, I believe, so…
There's that. Hannah, who couldn't be here today, wanted to call out this PR.
We've been In an attempt to move towards the…
database, convention migration process. Like, we want to add that SEMCOM stability opt-in variable to databases.
we've realized that refactoring our current gem setup is going to be helpful. There's a new attribute that we're adding, because it's in the spec. The span name is now supposed to be the query summary, which involves some parsing.
And so the idea here is that instead of just having one gem to obfuscate SQL, let's make a new gem that's responsible for all of the SQL query parsing things.
So for now, because that query summary work is still in progress, and I think to just kind of make the transition simpler, this pull request is kind of updating the SQL processor gem to include the SQL obfuscation code.
And, and it also changes the API slightly.
So we did advertise that people could use the SQL obfuscator outside of our gems, because we do have support here for dialects that we don't have instrumentation for, like Oracle and Cassandra. But, so yeah, so…
there's some post-install messages that will show up, and I think other deprecation warnings. Since last week, we released the final version of the SQL obfuscation gem, and the first version of the SQL processor gem. So if you have thoughts about how APIs should be set up, or, you know, how you think
We should organize this code now that it has been moved.
Would love to get your feedback and input on it.
the, yeah, the new… the new plan to call it would be…
through this method, OpenTelemetry Helpers, SQL processor obfuscate SQL.
Whereas before, I think processor was just Obfuscator. It was the main difference in the API, so…
Yeah, any, any questions? Any… Concerns?
**Robb Kidd (he/him)** 10:58 I'll… I'll look at it.
**Kayla Reopelle** 11:00 Okay.
**Robb Kidd (he/him)** 11:01 Any concerns with the idea of…
Okay. Basically a SQL helper, Jim. It's sort of like that, right? The idea that we had a long time ago and might have acted on, the HTTP helper.
**Kayla Reopelle** 11:13 Oh, yeah, I think…
**Robb Kidd (he/him)** 11:14 No.
So regardless of how that turned out, this makes sense.
**Kayla Reopelle** 11:19 Okay.
**Robb Kidd (he/him)** 11:20 plan. Sure.
**Kayla Reopelle** 11:21 Awesome.
**Robb Kidd (he/him)** 11:22 And see if there are devils in the details, but yeah.
**Kayla Reopelle** 11:25 Thank you, appreciate that.
Let's see… yeah, and then… yeah, I'll clean up the instrumentation, I'll release notes about including the RubyLogger there.
One thing on, yeah, the instrumentation All, I think you can still use the useAll method if you want to bring in RubyLogger instrumentation because of the way the configurator works. It doesn't have to be in the all gem, it's just the name of the method. It'll detect
that that's available on your system. If that's not how it works, it surprises me, because I have tested it, and it has been fine, but,
Yeah, as far as I know, that's… that's a good route to take.
Okay, yeah, let's jump in…
to core, I guess, and see…
Thanks for opening this PR, Wendy. I think it looks good. Had a chance to review it this morning.
So, yeah, if anyone else is interested in looking at this.
I'll leave it open, probably through the end of today, and then we'll merge it tomorrow if there's no new comments.
Was there anything you wanted to add, Wendy?
**Wendy Smoak** 12:40 No, just… I did not put it where you suggested in the issue, but…
**Kayla Reopelle** 12:45 Yeah, I swear.
**Wendy Smoak** 12:46 There it is in the log. I just copied and pasted that from what you did in logs, so…
**Kayla Reopelle** 12:50 Yeah, that makes sense.
**Wendy Smoak** 12:51 It seems to do the thing. I just needed it to say something.
**Kayla Reopelle** 12:55 Yeah, a little more guidance.
**Wendy Smoak** 12:58 When I was first starting, I couldn't tell if it was doing anything, so…
**Kayla Reopelle** 13:02 Hmm, okay.
Well, good. I'm glad we can fix this for… for other folks who are… Joining.
Alright, I haven't looked at these yet.
Improve error reporting debugging UX with the OTLP default HTTP exporters.
1931.
Okay, that was the… issue that Hazel opened.
This is, hopeful.
Okay, well, yeah, we did talk about this…
last week, a little bit, just the issue that Hazel had opened, so,
Seems a little beefy. Might be…
Something we'd want to consider for the other signals, too, if we like this pattern.
**Robb Kidd (he/him)** 14:23 Is this sort of in spirit to the changes that Wendy made?
Logging more at the debug level when you're having trouble exporting.
**Wendy Smoak** 14:32 Yeah, it doesn't… so, for instance, when it can't talk to the ex… when it can't talk to its collector, it only gives you, like, the V1 logs, like, it doesn't…
the SDK in general, like, it just doesn't…
Give you enough to figure out what's going on if you don't already know what can go wrong.
**Robb Kidd (he/him)** 14:52 Cool. I wasn't saying that this was…
**Wendy Smoak** 14:54 Yeah.
**Robb Kidd (he/him)** 14:55 that I was just like, this seems Lynn's spirit.
**Wendy Smoak** 14:58 Yeah, it's the same. So, this is a lot.
**Robb Kidd (he/him)** 15:00 But this, yeah, this is a lot.
**Wendy Smoak** 15:02 Not go that far.
So, it is kind of a, you know, I don't know, philosophical, like, this… it kind of clutters up the code, right, when you have all this.
**Kayla Reopelle** 15:12 Yeah.
**Wendy Smoak** 15:12 stuff in there, and I don't know if there's any way to make it…
To do it any other way.
**Robb Kidd (he/him)** 15:19 There's also performance concerns. I don't mean to be premature to optimize prematurely, but the more method calls we make.
It's usually more of an issue during instrumentation, because the instrumentation's usually instrumenting hot pads, and export's not that hot of a path, but it's warm.
I'm sorry, go ahead, Whitney.
**Wendy Smoak** 15:45 I was gonna say, somewhere else, there's a… so right now, there's no log level for the…
Well, no, there is…
There's a log level for the SDK itself, and that's what this is. Okay, so it would respect…
Like, if you… it… so I don't know what… how… how much of a performance impact there is for calling logger.debug when the SDK's level is set to, like, warn or something.
**Robb Kidd (he/him)** 16:16 Yeah, it wouldn't do, like, it wouldn't do the actual logging, so the active logging wouldn't incur, but…
The active calling methods is…
**Wendy Smoak** 16:25 It does still.
**Robb Kidd (he/him)** 16:26 is a non-zero, computer expense, and I'll channel Ariel here and say, like, we have seen performance issues that just, like, method dispatch in Ruby, because of its dynamism, can get…
can slow things down. But maybe in the export loop, it's not that big a deal.
And logging to tell you what's going wrong is useful. We should consider it.
**Kayla Reopelle** 16:53 Yeah, yeah, I think we should.
**Robb Kidd (he/him)** 16:55 One thing to be wary of.
**Kayla Reopelle** 16:57 Yeah, one other thing, too, with the design is, I think.
we could also consider… because, like, this exporter is supposed to get passed to whatever the next level is, maybe the batch span processor, and that is supposed to give, I think, the helpful information right now.
So we could consider refactoring it to just pass better data over to that exporter, and then have the log messages kind of all come out.
If we can find something… That we don't specifically have to write based on the context.
**Robb Kidd (he/him)** 17:32 But I hear you and others. More information about when sending data goes badly.
**Kayla Reopelle** 17:40 Oh, yeah.
**Wendy Smoak** 17:40 Yeah.
**Robb Kidd (he/him)** 17:41 It just really makes you wish for a compiler that could strip all this out for production.
**Kayla Reopelle** 17:49 Yeah.
**Robb Kidd (he/him)** 17:52 So, to review, and.
**Kayla Reopelle** 17:54 Yeah, yeah.
Not that.
What the fuck we got all that?
Alright, and then there was another one that they opened…
This was… Another open issue…
Oops, so my PV6 fixes this.
Yeah, I'd have to… it's been a while since I've thought about this problem, so I'll have to take another look, but
It'd be great to have more than one.
More than one look at it.
And I imagine Arielle will look at this PR once,
the contrib stuff is merged in, so…
The SDK changes are probably coming.
Yeah, was there anything else on here?
That we want to talk about today?
Sean, I left a little more feedback on this guy.
Sorry, you just unmuted, I'll let you talk.
**Xuan Cao** 19:33 Oh, yeah, oh, actually not this one. The one, that was, adding the,
The community, priority for the…
Expense… extension histogram. The test was failed because of one test case that is… Very unpredictable.
No, the, the added merge logic for the expansion histogram.
Appear…
**Kayla Reopelle** 20:04 Is that the one that got merged yesterday?
**Xuan Cao** 20:06 No, no, no.
**Kayla Reopelle** 20:08 Go see it now.
**Xuan Cao** 20:08 Yeah, that's fine, yeah.
**Kayla Reopelle** 20:09 Okay.
**Xuan Cao** 20:11 boat.
Yeah, there's one test case that is not… Very predictable.
I saw this one, I saw this issue from another PR, which is
So they are related to this, issue, so…
And then it is caused because of the timeout.
And the timeout is… the timeout is, like, 10 seconds to wait for the process ID, which is, I think it's pretty enough for the… but still, I think some… somehow…
I don't know, the trace… sorry, not the trace, the, the spread is not, Working…
Predictably, at this case.
So, I mean, I mean, I can find a way to improve the test case.
But, yeah, but I think if you can… if you can be wrong with stuff, probably should.
Hopefully, you know, get past.
**Kayla Reopelle** 21:10 I missed that last part, can you say.
**Xuan Cao** 21:11 Oh, sorry, I mean, if you can rerun the test case, hopefully you can, but I will try to find a way to fix that test case.
**Kayla Reopelle** 21:20 Okay.
You got it.
I'm sorry, I didn't realize you don't have the ability to rerun test cases.
We should, yeah, we should talk about that, and try to figure that out.
Alright, yeah, any other PRs?
If there was one big PR I could look at this week, Schwan, which one would you want it to be?
**Xuan Cao** 21:50 Oh, I think it stays the same for the merge logic. I think.
**Kayla Reopelle** 21:55 This one? Okay.
**Xuan Cao** 21:56 Yeah, yeah, yeah.
**Kayla Reopelle** 21:58 Sounds good.
Or you'll respond also.
**Xuan Cao** 22:03 comments, so… but let me know if this is more, Sync.
Not a contrast, yeah.
**Kayla Reopelle** 22:11 Sounds good.
Thank you.
Alright, let's see, were there any new issues?
Got a couple of new issues.
Span kind immutable to span processors.
Hmm.
Interesting. Okay, so… The request seems…
Uncertain about its spec.
Compliance.
Yeah, it's interesting, kind is not listed.
Here…
**Robb Kidd (he/him)** 23:33 It's… it seems to be excluded from the list of span operations. That's what… Oh, fantastic.
**Kayla Reopelle** 23:39 on the…
**Robb Kidd (he/him)** 23:39 It's, I think, asserting.
**Kayla Reopelle** 23:42 Yeah.
**Robb Kidd (he/him)** 23:42 But while it's not listed as things that should be set in that creation.
It's not listed in…
**Kayla Reopelle** 23:52 Yeah.
So…
**Robb Kidd (he/him)** 23:56 State that you can change, operations that you can perform on its menu.
**Kayla Reopelle** 24:01 Yeah.
**Robb Kidd (he/him)** 24:07 I'm sort of curious…
Not to know more about the problem that gets solved, but in what situations do you not know what kind of span you're producing at start?
**Kayla Reopelle** 24:22 Yeah.
**Robb Kidd (he/him)** 24:23 Not saying that there aren't cases, I'm just…
I can't think of any at the moment.
**Kayla Reopelle** 24:30 Yeah, same.
**Robb Kidd (he/him)** 24:31 We knew what problem we were solving by making it renewable.
Actually, do you want to add that comment? Sure.
**Kayla Reopelle** 24:40 Okay, that'd be great. Thank you.
And this too.
And then… the other issue was…
Adding custom span processors considered impossible without private method calls?
Rob, are people… are you aware of customers using spam processors at Honeycomb with Ruby?
**Robb Kidd (he/him)** 25:53 I'm not aware of it, but I think a lot of,
My experience is that, the Ruby SDK and instrumentation has generally been good enough that I don't hear from our…
It just seems to work for folks.
**Kayla Reopelle** 26:05 Yeah, yeah.
**Robb Kidd (he/him)** 26:09 Or they don't use them. So, like, I have negative, or I have the absence of signal. I don't… I don't know if people are using custom spanning processes or not.
**Kayla Reopelle** 26:21 Yeah, heard it.
**Robb Kidd (he/him)** 26:22 and I'm sure you might have experienced this, it is a challenge to… determined from… telemetry.
The hijinks people get up to in their instrumentation.
**Kayla Reopelle** 26:34 Yeah.
**Robb Kidd (he/him)** 26:34 So, like… despite receiving a volume of it, I can't tell unless they ask questions.
So, yeah, no, I don't, I don't know.
**Kayla Reopelle** 26:47 Interesting. Yeah, I would like to hear from… Maybe Arielle, or…
folks at Shopify to see if they've been able to use them, because I feel like that ad span processor API
Should be sufficient.
**Robb Kidd (he/him)** 27:08 I have used them myself.
**Kayla Reopelle** 27:11 And…
**Robb Kidd (he/him)** 27:12 I… Have done it in that configure invocation, in that second code block.
That spam processor has worked for me.
But I could read this issue and…
**Kayla Reopelle** 27:25 Yeah.
**Robb Kidd (he/him)** 27:26 See ya.
**Kayla Reopelle** 27:29 Understood.
**Robb Kidd (he/him)** 27:29 Manage and see if there's a bug, or just, oh, cool.
Mom.
**Kayla Reopelle** 27:40 Yeah, that would be great. I'll,
I'll try to take a look, too. I'm pretty sure I've used this before, but,
Yeah, it's kind of… it's a surprising one to see, and I wonder if all these folks are on the same team, or just…
All have had the same problem.
**Robb Kidd (he/him)** 28:00 I'm curious about the… I just need to read this.
**Kayla Reopelle** 28:04 Yeah, yeah.
**Robb Kidd (he/him)** 28:05 I've never used wrap exporters from Envy.
Oh, I think I see it.
Or at least I'm starting this… again, I haven't read the… this is the first time.
But… but in…
Wrapped exporters from… it's like, they don't want to have to repeat all of the exporters that might have been passed through configuration. I have.
**Kayla Reopelle** 28:30 Notice.
**Robb Kidd (he/him)** 28:31 that when I use ad span processor, I'm now in a world where I need to spoon-feed the configuration, every span processor.
**Kayla Reopelle** 28:37 Oh, okay, including the exporters. Got it.
**Robb Kidd (he/him)** 28:41 and I think that that is just a point of pain I left… I lived with.
when I was doing my own span processor.
So, the.
**Kayla Reopelle** 28:54 I gotta read this, but my quick…
**Robb Kidd (he/him)** 28:56 sniff test of this is that it's, yes, the configuration interface is that it is…
hard to… it's hard, because you have to use this private method. Too impossible, if you choose to stick with public service, to add a spam processor
in code.
without… Having to then repeat anything that you've given through configuration, say, through the environment variables.
Okay. Or in the future, when we have a config demo with you.
**Kayla Reopelle** 29:26 Yeah.
**Robb Kidd (he/him)** 29:27 The merging of those declarations of which band processors to activate.
probably don't coexist well. So I'll read this, confirm that that's sniff test, accurately.
identifies the problem at comments.
We might need… some merging.
There you go.
I agree that the… that the verb, the imperative ad spam processor shouldn't.
**Kayla Reopelle** 29:56 Oh, Lord.
**Robb Kidd (he/him)** 29:57 All the other spam processors.
**Kayla Reopelle** 29:58 Yeah, yeah.
**Robb Kidd (he/him)** 29:59 remains.
**Kayla Reopelle** 30:01 And, yeah, and should probably apply all the…
yeah, get applied to all the exporters. It sounds like a bug.
**Robb Kidd (he/him)** 30:12 But I'd have to be… I'll put this on my list of stuff to… Responsor.
**Kayla Reopelle** 30:17 Cool, thank you.
What else we got?
Oh… Schwan, you said, tracer provider ad span processor.
**Xuan Cao** 30:34 Oh, I think that's not relevant to the actual issue that they want.
you know.
**Kayla Reopelle** 30:39 Okay.
And… oh yeah, if anyone is interested in this, I forget if I've mentioned it before, but they're trying to do a new, like, reference application for the Getting Started Guides. This one will have…
like…
it's more… it's… I think the first one was focused on rolling dice, this one has a little more details, it's just trying to exercise more of the features than the previous one.
It's still in early stages, so it's kind of buried in the docs right now, but if someone feels strongly about wanting to do this, like, let me know and we can assign you to the issue.
It doesn't seem like there's any rush to do it, though, either.
**Robb Kidd (he/him)** 31:26 Is it, here's an example.
Here's example business logic to implement in all the languages and instrument it.
**Kayla Reopelle** 31:33 Yep.
Yep.
And, yeah, ruby was…
offered… I offered, but I offered 6 months ago, when there was a different level of, availability.
**Robb Kidd (he/him)** 31:50 I mean, I think that would be fun.
Yeah. I'll see if I can… I'll see if I can fit it in.
**Kayla Reopelle** 31:55 Cool?
Yeah, alright, anything else on here we want to take a look at?
Once? Twice?
Alright, let's go to contribute.
And… were there any issues here?
Hmm.
Where did this come from?
Okay, yeah, we did have an Ethon release.
Last week…
So I guess it's not bubbling things all the way back up.
Okay.
And that's the only new one.
Alright, well, I can… I can take a look at that.
After this meeting.
**Robb Kidd (he/him)** 33:29 That looks like we're not re-raising.
**Kayla Reopelle** 33:32 Yeah.
Should've caught that.
**Robb Kidd (he/him)** 33:40 Which, I could totally see, How, when writing this.
If I was in the mode of, OTEL doesn't raise errors so that it doesn't break your app. But, wait, no.
This is an error from the thing being instrumented, I gotta re-raise it.
**Kayla Reopelle** 33:54 Yup, yup, exactly.
**Robb Kidd (he/him)** 33:56 Yep.
**Kayla Reopelle** 33:56 I think that's… that's what happened.
Well, that should be easy enough to fix.
Cool.
And, yeah, I don't think we saw any other pull requests on here.
So… Yeah, alright. Well, I think that's it, unless there's anything else y'all want to talk about.
**Robb Kidd (he/him)** 34:23 Nope, that's enough work.
**Kayla Reopelle** 34:25 Sounds good. Alright. Well, I hope everyone has a great week, and yeah, we'll…
Check in then, if not before. See you guys later.
**Wendy Smoak** 34:34 Thank you.
**Kayla Reopelle** 34:35 for coming.

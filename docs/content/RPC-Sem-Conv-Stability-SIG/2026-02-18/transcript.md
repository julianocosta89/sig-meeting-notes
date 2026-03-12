SIG: RPC Sem Conv Stability SIG
Date: 2026-02-18
Duration: 48 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 02:08 Hey, Matt!
**Matthew Hensley / Grafana Labs** 02:10 Hello!
**Liudmila Molkova** 02:26 Hello.
**Trask Stalnaker** 02:27 Hey, Ludnula.
**Matthew Hensley / Grafana Labs** 02:32 I was able to politely ask one of the AI note-takers to leave, and it did.
**Trask Stalnaker** 02:38 Oh, I love it.
**Liudmila Molkova** 02:38 Oh my god.
**Trask Stalnaker** 02:39 I love that one. Yes.
I hope they did.
**Liudmila Molkova** 02:46 I'm getting… I haven't seen the other one in a while, I think.
**Trask Stalnaker** 02:56 Oh, usually I see… usually I see… Two of them.
And I politely tell one of them to leave, and the other one ignores me.
**Liudmila Molkova** 03:06 Yes.
**Trask Stalnaker** 03:14 Alright, what?
Do we need to do before we can… Mark RC.
**Liudmila Molkova** 03:30 I think we need to hit merge.
on this PR?
And technically, we can, because of the GitHub glitch.
But I would appreciate, Matt, if you could… The ROP re-approval here.
**Trask Stalnaker** 03:49 What's the GitHub glitch?
**Liudmila Molkova** 03:52 So there was a… the original PR was quite different, and you two folks, you two approved it.
Then we changed the direction, and I… Dismissed your approvals.
**Trask Stalnaker** 04:06 Oh, but it still shows… It's still counting, okay.
Interesting.
**Matthew Hensley / Grafana Labs** 04:15 I will re-review it, of course. I've been, trying to keep an eye out when they change significantly, and just… mark mine as request changes, since I can't… Put it back into… An unreviewed state.
4 minutes.
**Trask Stalnaker** 04:32 What is… can you… do, I think I can do… can you do this? Dismiss review like this?
**Liudmila Molkova** 04:46 You're asking me, Hermit?
**Trask Stalnaker** 04:48 I'm Matt.
Let's see, can I do it on myself? Dismiss review.
**Matthew Hensley / Grafana Labs** 04:55 Testing.
**Trask Stalnaker** 05:03 So I think that works.
If you do it that way.
**Liudmila Molkova** 05:08 Yeah.
**Matthew Hensley / Grafana Labs** 05:09 Yes, it does. That's…
**Trask Stalnaker** 05:11 Instead of the… don't… the re-request, yeah, this button doesn't… I think… I'm just gonna make a mockery of your PR here.
Yeah, that one doesn't do anything.
Now, okay, yes, that's so confusing, because now it looks like… because I always look up here, now it looks like nobody's approved it.
Okay, we're gonna fix that.
**Liudmila Molkova** 05:50 So once that's in, I'll… Maybe we can, take a quick look. I can probably undraft the mapping PR.
It kind of depends on… There are a new one, but still one drop.
Fast exception event.
**Trask Stalnaker** 06:26 I'm adding, in Java, ran across…
**Liudmila Molkova** 06:33 Sounds good.
**Trask Stalnaker** 06:33 implementation, so… Events… So this one, mapping…
**Liudmila Molkova** 06:55 Yep.
**Trask Stalnaker** 08:20 Is this… Now… Not correct.
**Liudmila Molkova** 08:28 Oh, we, yeah, need to remove gRPC target from OpenTelemmetry attribute, yeah.
**Trask Stalnaker** 08:36 Oh, we didn't end up… sorry, I already forgot what we did.
**Liudmila Molkova** 08:41 We don't have the attribute.
Cannotel anymore.
**Trask Stalnaker** 08:49 Right, because we said that we were comfortable expanding the domain of server.address.
**Liudmila Molkova** 08:57 Yeah.
I updated.
**Trask Stalnaker** 10:26 I see, we have a more fine-grained…
**Liudmila Molkova** 10:31 Yep.
**Trask Stalnaker** 10:32 Error definition…
**Liudmila Molkova** 10:50 RPC… A response… Status code is where we say which one of them are errors.
**Trask Stalnaker** 11:24 That's on ser… oh, that's on… server… Okay, on the client side… They're awe.
Okay, right, right.
Don't they have a gRPC. method?
**Liudmila Molkova** 12:31 Not on spends, they don't have anything on spends. Oh, sorry, wait, they have it in the spending.
**Trask Stalnaker** 12:39 I see, but they don't stamp the attributes on spam. Yep.
Gotcha.
**Liudmila Molkova** 12:56 Yeah, so, maybe… what do you feel about this? I think the fact that they don't have any attributes is not… Cool?
And what I'm suggesting, that if you… I don't know if anybody would convert, but if you're converting, they keep it up and telemetry attributes.
From this list.
**Trask Stalnaker** 13:21 Other than the ones that have some kind of data representation on that Yeah, I don't see why not.
It's… lowercase should. Anyways, people can do what they want.
**Liudmila Molkova** 13:45 Yeah, the… This is non-normative because it's a non-normative folder.
Cool.
And you… you haven't been there, but trust you've seen there's someone who wants to contribute the mapper between different GenAI semantic conventions in the collector. So, in theory.
this… If that's ever.
GET.
implemented, then in theory, that could be… there could be a component that does this mapping in Collector, and we could probably even write OGTL that does this.
**Trask Stalnaker** 14:35 Yeah, yeah.
**Matthew Hensley / Grafana Labs** 14:37 That would be, pretty interesting.
**Liudmila Molkova** 14:40 I saw there's…
**Matthew Hensley / Grafana Labs** 14:41 One sub, new collector component that… does that for some of the LLM and generative AI conventions.
**Liudmila Molkova** 14:49 Yeah, exactly, yeah.
**Trask Stalnaker** 14:53 Yeah, I think the interesting direction… would be from the gRPC to the OpenTelemetry.
Most likely.
**Liudmila Molkova** 15:08 Yeah.
Because this is the direction we are interested in as a project.
**Trask Stalnaker** 15:15 And, well, I think because the… I'm thinking because the backends… Are probably more likely to be embracing open telemetry, like, the standardization across the RPC signals.
Whereas the native instrumentation, we don't have control.
over it, it would be nice to be able to recommend the native gRPC instrumentation to people.
**Liudmila Molkova** 15:53 I don't think it should be a component, but we… we… I mean, I could… Bride Dojuto for this.
If I think it'll be helpful.
**Trask Stalnaker** 16:11 I wouldn't, unless somebody… is actively… Wanting that.
I feel like this is more… this is… Maybe less or practical.
Mapping purposes, and more to… It's like a way of displaying the diff and communicating kind of an unfortunate, difficult message, which is that they're not the same.
And here are the differences, and… Maybe we'll have a path forward in the future.
**Liudmila Molkova** 16:50 Yeah, and it helped us a lot to make sure we provide something compatible.
**Matthew Hensley / Grafana Labs** 16:58 I wouldn't necessarily write the mapping rules unless we decided Or one of these, it was gonna… Be one of the prototypes?
Spike over the line, which… Could be interesting for other attempts, because we go after messaging.
Something.
**Liudmila Molkova** 17:17 I would be interested in writing those if… if I had the infinite, like, infinite time for… to… to be a playground for… okay, I want to map one arbitrary convention to another arbitrary convention, and I want to have a language that supports it, and it's helpful beyond Just your PC.
**Matthew Hensley / Grafana Labs** 17:40 No, certainly. Being able to… If you can't write the mapping rules.
Then, we don't necessarily understand what we're doing.
Speaking of that, this document looks great, I just see… For the non-normative stuff, just some minor formatting for quality of life.
Make some quick suggestions on the PR.
**Liudmila Molkova** 18:06 Thank you.
**Trask Stalnaker** 18:07 Great.
**Liudmila Molkova** 18:13 Cool.
And… Then… What else do you have?
**Trask Stalnaker** 18:27 I posted the… the RC… release candidate PR.
**Liudmila Molkova** 18:35 Oh, nice!
**Trask Stalnaker** 18:50 So, basically, once we get those… Two merged.
And… Merge this, and… Oh, maybe we get, we owe a SEMCOM release.
Yeah, I think Josh wanted to cut one tomorrow.
Do we want RPC… RC in there?
**Liudmila Molkova** 19:23 Yes?
**Trask Stalnaker** 19:27 Let's do it.
**Liudmila Molkova** 19:34 Yay.
Then I promised to work on Python.
prototype, I did not do it.
**Trask Stalnaker** 19:47 No worries.
Oh, I did look.
I forget if… I see seed.
This was the issue you opened.
About the unknown requests, so… Just a little.
ugly. I haven't really reviewed my own code yet.
But… It's… Now, what does, the gRPC does… okay, I need to look at how GRPC instrumentation.
**Liudmila Molkova** 20:32 It's in the issue.
**Trask Stalnaker** 20:34 Okay.
**Liudmila Molkova** 20:37 I don't remember.
**Trask Stalnaker** 20:43 Yes, okay, so that's what… Okay.
**Liudmila Molkova** 20:52 So, you were… able to deal with the coordinator? I don't remember. How are we dealing? How are we… how do we know if it's a known method?
Because it's the method descriptor, right?
There is some way to know that it's a known method or unknown method.
**Trask Stalnaker** 21:16 Yeah, let me see that… Unknown service… gRPC status code unimplemented.
Oh.
**Liudmila Molkova** 21:37 You're violating the convention! Oh no.
Oh, Span has named other.
**Trask Stalnaker** 21:46 Let's see, so we've got a client, so we've got the client's.
**Liudmila Molkova** 21:49 Oh…
**Trask Stalnaker** 21:50 Which is getting back to unimplemented in the server span.
But it's not populating rpc.
rpc.method, we want to be… Other.
**Liudmila Molkova** 22:07 And we want original to be whatever it was.
**Trask Stalnaker** 22:33 Cool.
I'm a client, so that's… Yes, that's only on the server side. On the client side, we don't… Care, we don't have the cardinality problem.
Look at random PRs.
I think I saw that, yes, Pablo, okay, we have… This is good, this is good.
So, for RPC… Okay, so Matt… okay, you left some comments and an approval grade.
And… on the map, will you have a chance to look at the other… to RPC PRs… Either today or tomorrow morning.
for… We can ask Josh to hold off on making the release.
**Matthew Hensley / Grafana Labs** 24:01 I can take a look this evening.
**Trask Stalnaker** 24:05 Well, thank you.
**Liudmila Molkova** 24:05 So you already approved this one, did you… did you mean it? Do you want to take another look, or should we just hit merge?
**Trask Stalnaker** 24:13 I think I… oh, oh, I see, this one is to get approved, re-approved, okay.
This one's good to go, Matt.
**Matthew Hensley / Grafana Labs** 24:22 Yep.
And the, the gRPC guidance, I just added some section headers that we don't have to have, it just makes linking to the different parts of the dock a lot easier.
**Liudmila Molkova** 24:34 When you've done working clothes?
**Trask Stalnaker** 24:36 So then…
**Liudmila Molkova** 24:37 my screen.
**Trask Stalnaker** 24:38 All we need from you is a… Approval on this, review approval on this one.
**Matthew Hensley / Grafana Labs** 25:12 Okie dokie, got a green checkmark.
**Liudmila Molkova** 25:16 By the way, Matt, you would appreciate it. Well, you would also find it interesting. Somebody sent a PR to define .NET remoting conventions.
And I didn't realize… okay, so that not remoting our legacy deprecated in favor of WCF, which are also deprecated since then.
**Matthew Hensley / Grafana Labs** 25:38 I have, in the last 3 months, worked on, demo instrumentation for ASMX web services.
**Trask Stalnaker** 25:50 Does that predate even that?
**Matthew Hensley / Grafana Labs** 25:53 Yeah, it's like back when, NET was like web forms, so basically React server-side rendering.
The first go at it.
Basically, yeah.
**Trask Stalnaker** 26:06 Wow.
**Matthew Hensley / Grafana Labs** 26:07 I think it was… I think ASMX services were… Jettison in, like, 2008 or 9?
**Liudmila Molkova** 26:19 That's crazy.
I, I, I, I'm going to reject this, Pure.
Just because, like, it's long gone.
**Trask Stalnaker** 26:30 Yeah, yeah, define your own SIMCOM for it is fine, yep.
**Liudmila Molkova** 26:34 Yeah.
**Matthew Hensley / Grafana Labs** 26:36 Yeah, I was looking through it earlier, trying to decide, like, did I miss something as far as this still being relevant?
**Trask Stalnaker** 26:43 Wyatt's… yeah, yeah.
**Liudmila Molkova** 26:51 Cool. So then, it seems like we will finish… Today.
**Trask Stalnaker** 26:56 Yeah.
**Liudmila Molkova** 26:59 Wonderful.
**Trask Stalnaker** 27:06 Why did… Why did the merge queue failed?
semantic convention, so that's probably… Make… probably need a… probably merge conflict, need a make on…
**Liudmila Molkova** 27:22 And which one?
**Trask Stalnaker** 27:24 the GRPC table…
**Liudmila Molkova** 27:27 The mapping?
**Trask Stalnaker** 27:29 Yeah…
**Liudmila Molkova** 27:30 The, the table of contents, though.
**Matthew Hensley / Grafana Labs** 27:35 Oh, yep, that'll do it, won't it?
**Liudmila Molkova** 27:38 I'm… I'm working on…
**Trask Stalnaker** 27:48 Oh, it was actually the other one. Also, I think needs some kind of make or something. I'll clone that one and make it.
Make is very slow.
**Liudmila Molkova** 29:13 Docker.
Beaver.
**Trask Stalnaker** 29:18 No, you know, the Weaver, let's see, Weaver Target, that's going fast. It's the other… Yeah, probably. Something. Anyway, I don't run it that much.
**Liudmila Molkova** 29:35 In theory, we could ask a pilot to do it.
**Trask Stalnaker** 29:41 It was smart enough to know, like, to run a diff, or… I don't know.
Yeah. Oh, I see, on the PRs.
**Liudmila Molkova** 29:51 Yeah, like, there is this new workflow, right, and imagine that this check fails. In theory, Copilot can run the update.
**Trask Stalnaker** 30:01 that.
I think that requires us to send, to use branches on the… Upstream.
Hmm, I ran on PR… 3317… Got rejected from the merge queue, but I ran make on it locally, and it didn't produce any changes for me.
Not sure yet what I'm doing wrong.
**Liudmila Molkova** 31:27 Dang.
Washington drills.
There is some… Different, maybe it's… At first, yeah, I see the difference in… In the logs.
Let me see, let me try, there's the PRs…
**Trask Stalnaker** 32:27 Yeah, something else is the problem for me, because Dubbo, I'm not even seeing…
**Liudmila Molkova** 32:48 Maybe… Large Mane.
**Trask Stalnaker** 33:05 That's a good idea.
**Liudmila Molkova** 33:09 Yep.
Table of content check is the longest one.
Welcome.
**Trask Stalnaker** 34:26 Command… Let's see, does the other one…
**Liudmila Molkova** 34:32 Yeah, the other one should be good to go as well.
Okay, this one's… I mean, if we're done with our PC… list. That's the major part.
**Trask Stalnaker** 35:07 We've got… yeah.
We've got 10 minutes.
**Liudmila Molkova** 35:12 No, I mean, it went pretty smoothly, in terms of conventions, I feel.
**Trask Stalnaker** 35:16 Oh, yeah.
**Matthew Hensley / Grafana Labs** 35:21 Certainly, it was relatively quick compared to some of the other efforts that have been Going on for a while.
**Liudmila Molkova** 35:32 Yeah.
I think we…
**Trask Stalnaker** 35:35 learned a lot.
**Matthew Hensley / Grafana Labs** 35:35 Cool.
**Trask Stalnaker** 35:36 In the past ones. There have been a… I feel like the ones that… things that… Well, HTTP was… So hard, because… We were still figuring out a lot of, like, fundamental semantic convention Things.
And then database, that was a new set of Kind of bigger picture questions.
**Matthew Hensley / Grafana Labs** 36:04 I think we also saved ourselves. I mean, there's obviously more work to be done. There's things that passed on for now.
But… have all the fundamentals done, and I think in a case like databases, it had some extras that were not necessarily needed.
To start with. Not that they were bad, but… By any means.
I definitely like getting out the, The minimal, useful one, whenever we can, so people can get to work and start relying on them, the conventions.
**Liudmila Molkova** 36:38 Yeah.
**Trask Stalnaker** 36:40 Just producing the, yeah, the basic duration, whatever, the red metrics, Rate, error, duration.
It's a big deal.
**Liudmila Molkova** 36:57 Consistently, across instrumentations. I've been playing this hotel demo, and it's surprising how inconsistent our instrumentations are.
Some limit spends, others emit spans and metrics.
Yeah.
**Trask Stalnaker** 37:13 Oh, that's it. Interesting.
I wonder, because I have this community issue right now where I was asking… Fox… to… for the HTTP SEMCOM status.
It didn't… Confirm that it's producing metrics also.
That's a good question.
**Liudmila Molkova** 37:46 I think most .NET instrumentations produce chest spans, right, Matt?
**Matthew Hensley / Grafana Labs** 37:55 No, not anymore. I added it for, ace Peanut.
We have SQL Client, I think, EF Core? That database one? So, HEP-wise, it's… there's… Complete coverage.
**Liudmila Molkova** 38:09 Oh, nice.
**Matthew Hensley / Grafana Labs** 38:10 So, for all the Net Framework stuff, and obviously all the new stuff, does it on its own.
But… Yeah, that was… as soon as HEP conventions went stable, Aye.
Started working on, adding it everywhere we could.
**Liudmila Molkova** 38:29 That's awesome.
**Trask Stalnaker** 38:38 I, resolving conflicts on the RC…
**Liudmila Molkova** 38:44 Oh.
**Trask Stalnaker** 38:44 PR.
**Liudmila Molkova** 38:46 Oh, I need to approve it.
**Trask Stalnaker** 38:52 You should have a few minutes to actually read it, if you'd like.
**Liudmila Molkova** 39:56 It's always surprising to see WES when we do it.
RPC things.
**Trask Stalnaker** 40:04 Which one?
**Liudmila Molkova** 40:06 the AWS.
**Trask Stalnaker** 40:08 Oh, Yeah, I was updating… I noticed that on… the Java instrumentation, when I was adding those RPC exceptions.
**Liudmila Molkova** 40:29 And I would… tried to fix it, but I don't know how to fix it without AWS people.
And I feel like they're… they're… unless they're… We'll get involved, we should… remove AWS conventions, or… But we have instrumentations for them in Otto.
**Matthew Hensley / Grafana Labs** 40:56 And in multiple languages.
I was just gonna say the .NET SIG, Last year, year before, because some of the AWS instrumentation had not been taken care of in a while.
There was effort, just in general, to find con-oders or start unpublishing packages.
Because they were not being maintained at all, so…
**Liudmila Molkova** 41:24 They are still there.
**Matthew Hensley / Grafana Labs** 41:27 Yep, found, the… Threat of having the instrumentation yanked because it was unmaintained. Got it.
Maintained.
**Trask Stalnaker** 41:42 be an interesting… I think there's gonna be some interesting discussions once we have a… The decentralization or the federation path.
Open… Of, what we want to… prune what we should prune from semantic conventions.
**Liudmila Molkova** 42:02 Yes.
**Matthew Hensley / Grafana Labs** 42:05 And along those lines, in that .NET remoting PR, so, obviously, you… like, the list of RPC frameworks, whatever, there's some listed.
what's the, like, hurdle we want people to cross to add more? So, like, in this case, this .NET remoting thing, it's… deprecated. It's only one potential runtime, likely.
So that doesn't seem like a great one, but it's… I don't know if we have guidance elsewhere. Like, what would it take to get your new database added to the list of databases?
**Trask Stalnaker** 42:46 An act of God.
**Liudmila Molkova** 42:48 Yeah.
I… This part is tricky.
And there are other tricky parts, like, I think that all the .NET conventions we have in semantic conventions should be eventually owned by the .NET, the PCL team themselves.
they've been… Working in semantic conventions, because… We have the tooling.
And also, we have the… Taste?
And they relied on it.
But maybe now they can.
Fly on their own.
**Matthew Hensley / Grafana Labs** 43:35 I was just going to propose, since… likely to recommend closing that .NET remoting.
edition. It's like, it's much like, we need prototypes, right, in multiple languages.
So, if something's not… It would be used.
Across… different runtimes, or different versions, like, if it's really narrow in scope.
You can just use your custom stuff, because you don't need Interop, necessarily, and you can stick to these for, you know, the rest of the stuff for easy querying, and add what you need, and… Should it get popular, it's easy enough to… Accept those changes, once they've experimented with it.
**Liudmila Molkova** 44:16 I think you just cited what… Go ahead, Trask.
**Trask Stalnaker** 44:20 I think that a little, like, I almost want to go further and say that I mean, ideally, we wouldn't host… any… RPC framework-specific or database framework-specific conventions in semantic conventions.
We would only have the… core… Conventions.
don't think that is a reasonable place to start, because we kind of have to explore some of the other… some database-specific ones and RPC framework.
Specific things to make sure that Dot.
Is gonna work out.
But long-term, I mean, it would be nice to not be… I could see that almost being, like, hey, we don't do any… Sort of vendor-specific or projects.
Libri… framework-specific stuff.
**Liudmila Molkova** 45:27 I think there is one reason why we could. I agree with you, like, if everybody owns their conventions, then yes. But if they don't.
like, AWS, right? They don't on their conventions, but we could still be interested in having instrumentation libraries in our repos, and there is more than one in different languages.
**Trask Stalnaker** 45:50 semantic convention contrib.
**Liudmila Molkova** 45:52 It's a magic commission country for… The conventions that need love.
**Trask Stalnaker** 46:00 are things that, you know, we want to use? I mean, that could be where we send all of the, you know.
database-specific, RPC-specific, AWS, things that… True, we use across multiple repos in OpenTelemetry, so it makes sense to have a central location for them.
But to be clear, differentiation between Like, and then people who are left out of that don't feel like they're left out of this central SEMCOM repo.
**Liudmila Molkova** 46:36 I see. So these are conventions we'd rather somebody else to own, but we just didn't find the owner for them.
**Trask Stalnaker** 46:43 Yeah.
**Liudmila Molkova** 46:44 Yeah, I like it.
**Matthew Hensley / Grafana Labs** 46:45 That definitely works, so… in the future, your conventions can either be owned by you locally.
We can add the… Contrib, or the really important ones with a high bar.
To make changes or additions to.
I think that's pretty understandable for people, and… Makes it easy.
Because there isn't a policy for this, so it's like, hey, we're actually not going to accept these, and… don't want it to seem completely arbitrary.
**Trask Stalnaker** 47:14 Right. Yeah, and people feel left out if we have some frameworks in there, and then we're saying no to their framework. That's not… doesn't feel great.
**Liudmila Molkova** 47:27 Yeah.
Okay, we just outlined the end of the semantic conventions.
There is a horizon, we can see that now.
**Trask Stalnaker** 47:37 And the, the RC, PR is in the merge queue.
**Liudmila Molkova** 47:42 Yay! I would give you a high five if we were in the same location.
**Trask Stalnaker** 47:49 Pardon.
**Matthew Hensley / Grafana Labs** 47:51 Alright, y'all. Well, I'm going to, drop off and get a kid to bed.
**Trask Stalnaker** 47:56 All right. Thank you both. Thank you. Congrats!
**Matthew Hensley / Grafana Labs** 47:59 Yay! See y'all!
**Trask Stalnaker** 48:01 Bye.
**Liudmila Molkova** 48:01 Ew.

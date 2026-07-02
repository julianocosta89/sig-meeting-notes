SIG: JavaScript SIG
Date: 2026-07-01
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Matt Wear 00:00:53 Hello.
Marc Pichler (Dynatrace) 00:00:54 Hello?
I'll wait one more minute to see if anybody else wants to join today.
Might be a quiet, meeting this time around.
Matt Wear 00:01:23 Yeah, what's… what's going on? Is there… is there holidays? Is there…
Marc Pichler (Dynatrace) 00:01:28 I think it's, Canada Day today.
Matt Wear 00:01:31 Yeah, alright.
Marc Pichler (Dynatrace) 00:01:32 So Canadians are out of office, and then, I think 4th of July is also coming up.
Maybe people are out already.
Matt Wear 00:01:43 Yeah, that makes sense.
Yeah, I've been away for a while, and coming back, I noticed that these SIG meetings are… I don't know, a little less full than they used to be, like… A year or two ago.
Marc Pichler (Dynatrace) 00:02:00 Yeah, it used to be… used to be a lot more, traffic in the SIG meeting, and it's kind of died down a bit, but it's picking up again. Usually we have… A few people here, that's, like, the usual suspects here.
But, yeah, there used to be a lot more people joining the meetings.
Matt Wear 00:02:26 Cool. Well, I'll… I'll be around a lot more going forward. I've kind of started working on declarative config for instrumentation.
I had a PR up, but Trent kind of commented. He pointed me… it was a little in the wrong direction. He kind of pointed me to how it should actually work, so… I'm reworking that. The good news is that most of it actually applies. It wasn't too far off.
Marc Pichler (Dynatrace) 00:02:55 Yeah, I think the whole declarative config stuff is really valuable. There's some things in the spec that aren't that easy to follow sometimes, or, like, at least for me, it is a bit… Difficult to, to map to, how it works right now in order.js, but, it's good to… look into the different things, and I think especially the instrumentation configuration stuff is gonna be very, very valuable going forward.
So thanks for working on that.
Matt Wear 00:03:30 Yeah, no problem.
Marc Pichler (Dynatrace) 00:03:37 Alright, looks like it's just us three today. Hello, David.
I guess I'm gonna go through my topic anyway, probably all of you are aware of that already. There's, the SAMConf migration happening. Marillia has been working on this, to… remove all of this, double emit stuff, and then only emitting the stable HTTP semantic conventions.
So… this is now a PR that's open in the core repo, and then there's also a second one that's in the contract repo. So, if there's, anything, To speak up about, then now would be the time, because this is, Quite a large change, and yeah.
Has been a long time in the making, so… Yeah. If anybody has any, objections to that, please note them on the PR.
That's… Pretty much it.
Moving on to the next… One.
David Luna Bistuer 00:04:56 Yeah.
Maybe, maybe, it's oversimplified here in these, in the comments, so I just wrote it in… In 5 seconds, so… so… It's on vacation, sorry.
So, basically, I've been more working on the browser part right now, so I'm dealing with Fetch and moving the instrumentation for Fetch and XHR.
But we also, are preparing kind of a package to have an browser SDK, which will be… mostly… We're exporting something from the SDK trace-based, and maybe something specific per browser?
By now?
So lately I lost a bit of focus on the… on the… on the plan for the… for the SDK packages on Core Repo.
the plan is… I guess ACK 3.0 was pushed to September, right?
Marc Pichler (Dynatrace) 00:05:54 Yep.
David Luna Bistuer 00:05:56 What about this new package, SDK3s?
which is kind of a certification of everything. Is that meant to be published as a 3.0, or part of the 2.0?
It's crazy.
Marc Pichler (Dynatrace) 00:06:08 supposed to come around in the 2.0 line still, and… Then, we're just gonna start pointing people towards that package, since it's.
David Luna Bistuer 00:06:20 some of you.
Marc Pichler (Dynatrace) 00:06:20 We can just publish it there.
So that people can already start moving over. When they move to 3.0, it's less of a break to them than… That's, like… current idea. Are you planning to use the SDK Trace package directly, then, in the browser?
David Luna Bistuer 00:06:37 So…
Marc Pichler (Dynatrace) 00:06:38 them.
David Luna Bistuer 00:06:38 when… when we were… so the browser SDK Which, as I said before, is not the… it's not a right, it's not a full-blown new SDK. It's just, you know, we're taking the pieces that we are focusing right now.
But it's kind of a problem for browser, and actually more… more bundler-friendly.
The first… it's still in draft.
So, yeah, we have to work on that.
But I made sure that it was already only importing from… so it only has a dependency from SDK3 Space.
Not, no, not browser, not, yeah, not SDK trace web, or something like that. It was already, depending on the base package, but… for me, it would be ideal to just, you know, depend on the new one, and go for it. So, before it gets, you know, before it gets more work on that, and we get kind of a… first, or 0.1 version of the browser SDK, I would prefer to… to actually update the dependency to… to this one.
Marc Pichler (Dynatrace) 00:07:48 Okay.
David Luna Bistuer 00:07:49 But there is no rush, but, you know, just to know about the timings, and if somebody on the browser seq wants to publish already.
I will let Nadim know about the timings and say, okay, let's maybe wait for… A couple of weeks or a month.
To have these, packets already, published, and then… So, we will be happy to be the, kind of, the early adopters of the SDK package.
The church packets, yeah.
Marc Pichler (Dynatrace) 00:08:15 Nice. Yeah, so… I think we would probably be ready… Anyway, with this package, because we… did all the renamings. We didn't do the renaming of this one type that I was talking about last week. I think it's called the SDK Span, or something like that.
But it's more of, like, an optional thing.
If we want to do that, we could do that now.
Or we could also defer to later and just have, deprecated Type. Exported.
Daniel Dyla (Dynatrace) 00:08:52 I think it's a lot more important that that type has the correct behavior than that it has any specific name, and as far as I know, we are… behaving properly there.
Marc Pichler (Dynatrace) 00:09:05 Yeah, exactly. It's really just, like, if we want to also change the name in the logs SDK, it would be nice to have it aligned, but it's not a hard requirement to have it.
Already this way, so… I think that would be fine. The last release was 3 weeks ago already, so if we want to actually do a release now, we could do it.
I think we'll be fine.
David Luna Bistuer 00:09:29 There is no rush on that, so don't worry. And, maybe, Oh, sorry, maybe I'm asking something that was already said, but… I remembered you mentioned about the… So, having a 2.X branch, no, so we need to update the release process to be able to release from the 2.X branch, and then from the main.
Is there something that I can do, or, you know, to actually help? Because Yeah, well, it's September, it's not so far and away in the future, so…
Marc Pichler (Dynatrace) 00:10:00 Yeah, I think the first thing to do, which doesn't require a second branch, Would be to have, pre-releases? .
be possible in the core repo?
We… Or… I… I think we did a few pre-releases with 2.0, from the main branch, and we would just set that up first, and then we would also start looking into, The release process from another branch.
David Luna Bistuer 00:10:39 Beautiful.
Marc Pichler (Dynatrace) 00:10:39 There might… that is also very helpful to have in place already.
I think the main… Thing that we need to look into there is to, Configure the deployment environment.
To also be allowed to run on that new branch.
And set up branch protection rules that are equivalent to main.
Or, like, rule sets, I think they're called now, that apply to that.
To make sure that… Like, if there's a commit that lands on… on the 2.x branch, it actually went through all the necessary reviews and everything, and it's just not something that,
David Luna Bistuer 00:11:24 Okay.
Marc Pichler (Dynatrace) 00:11:24 Somebody pushed there.
But yeah, I think that would be very helpful, to have that in place already, because then we can just get right started, with the… After publishing and, like, if we have to do a security fix or something like that.
We can… we can actually follow through on that without… Too much hassle.
David Luna Bistuer 00:11:51 Okay, I'll have a look and see. Maybe I'll ping you on Slack.
as you can board. So I'm still working on the browser, but then I'll allocate some time to actually Either Ken.
Help with that, and and have the… the tools in place to… to have these little releases, so…
Marc Pichler (Dynatrace) 00:12:09 Hmm?
Yeah, thanks.
Alright, yeah, if you're trying to reach me, I will be in… the office until Friday, I will be out of office the next week, but I.
David Luna Bistuer 00:12:24 Thank God.
Marc Pichler (Dynatrace) 00:12:25 for death.
David Luna Bistuer 00:12:27 Okay, good.
Marc Pichler (Dynatrace) 00:12:30 Alright.
Matt Wear 00:12:40 I just added that because this meeting is light, but, this is from a PR that I closed, but the issue, I think, is going to remain. I'm going to reopen this PR at some point.
But, I found, like, CodeCov was under-reporting for the HTTP and the instrumentation package, when I first submitted. That's what I got, like, 6% and 4%, when I think both of those were covered at over 90%? So, so… if you… yeah, if you look at that actual commit that I linked, it kind of has, Maybe the proposed fix.
But basically, the.
Marc Pichler (Dynatrace) 00:13:33 Oh, sorry, which commit did you mean now?
Matt Wear 00:13:35 I think if you go back, I think it's linked maybe directly to the commit.
Or maybe my link is wrong?
Marc Pichler (Dynatrace) 00:13:45 the… I think I just… I'm missing the link.
Matt Wear 00:13:51 I think this link…
Marc Pichler (Dynatrace) 00:13:52 This one.
Matt Wear 00:13:52 directly to the committee.
Marc Pichler (Dynatrace) 00:13:54 Sorry. No, no, I found it, yeah.
Matt Wear 00:13:57 So… Yeah, so ultimately, I think that this NPM run test CGS and NPM run test ESM, and… NPM run… test double instrumentation, I think.
Those are clobbering, like, the previous.
Marc Pichler (Dynatrace) 00:14:17 the pre…
Matt Wear 00:14:17 Previous reports, so you're only kind of getting, like, the last report without this change.
And that this, this made it so that all those reports are just accumulated.
So…
Marc Pichler (Dynatrace) 00:14:35 Yeah, I think, that's very possible that that's happening, so having these in would be good to avoid running into the same issue again.
Matt Wear 00:14:44 Yeah, so I was just wondering if I should open a PR with literally just these two changes, and if this is the right fix for it.
Marc Pichler (Dynatrace) 00:14:54 Yeah, I think that's a good idea. David mentioned here that it's happened in contracts.
David Luna Bistuer 00:14:59 Yeah, I remember when I was doing changes on a good trip to get the V ports per package.
There was… this was kind of, one of the issues. So, we were running the Tav, test, desktop versions?
And we were getting the same… the similar… well, the similar behavior. So, the last one… so the last version that was tested was removing all the reports, previous reports from the other versions.
So yeah, at least the no clean. I remember the no clean option. It's necessary to have it, so yeah. If you open the PR, Matt, I'll be happy to remove it.
Marc Pichler (Dynatrace) 00:15:40 Sounds good.
Matt Wear 00:15:41 Yeah, so I'll go ahead and open a separate PR for that, and eventually I will open a new PR for declarative config once I… Let's have things working as aspect.
David Luna Bistuer 00:15:56 Sorry, I will chime in, again, while having coverage is good.
The, you were mentioning this the HTTP, which, which is traditional are the ones that you're getting?
It's SallyTB.
Matt Wear 00:16:11 HTTP instrumentation, HTTP, and then the instrumentation package itself.
David Luna Bistuer 00:16:15 Okay, okay, you have to move.
Funny.
Okay, there are… there are some instrument editions here that are moving to a different repository. I was thinking that maybe it was the Fetch or the HR instrument editions. Do you find something similar on a browser instrument edition? Please let me know.
So I'll let, I'll let another people call it the browser stick.
Matt Wear 00:16:37 Will do.
David Luna Bistuer 00:16:39 Okay, thank you.
Marc Pichler (Dynatrace) 00:16:42 Yeah, I think we should just happen in these two, because we're actually having, like, separate tests for ESM and CommonJS.
For the others, I think this should be less of an issue.
I think these are the two packages that have this.
- Right.
Any other topics?
If not, then, I guess we can move on to pack triage, as always, if… If there's anything you would like to talk about, please feel free to, just interrupt, and then we can talk about your topic.
Looks like no new pack reports in.
Took… Core Repo, one in the ContraPo, here we have, OpenAI Instrumentation.
breaks… Stuff.
Hmm… Looks like Datadoc has run into a similar issue.
This does look like a P1 issue to me.
Looks like they also added, like, a reproducer, but do be careful with downloading these things from there.
Yep.
Not sure if anybody's interested in picking that one up.
If not, then we can leave that unassigned for now.
But it is a P1 issue, so… It would be good to have that fixed.
David Luna Bistuer 00:19:04 You can assign it to me. I'll… I'll have a first look. So, Trent is the… the, the AI guy here in Elastic, but… I'll have a risk analysis, and then I'll… Send information to him, so maybe… He's going back on Monday, so then he can have another look, simple look.
Marc Pichler (Dynatrace) 00:19:27 Thanks for taking a first look at that one.
David Luna Bistuer 00:19:30 Impact.
Marc Pichler (Dynatrace) 00:19:32 I would… I would pick it up, but I'm, like.
David Luna Bistuer 00:19:35 No waste.
Marc Pichler (Dynatrace) 00:19:37 Gonna be out of office, too, and then it's gonna sit for a while.
David Luna Bistuer 00:19:40 Yeah.
Marc Pichler (Dynatrace) 00:19:47 Alright… Pr triage, we can actually use now this, new issue that, Meglius… automation, or the automation that Marilla talked about last week opened.
It's actually very useful, for… going through, PRs that need attention there.
We'll have a different, order this time. So, You can just go through it like this, That's actually an issue with our renovate config now. I found that… so, we added this, What's the cart?
Stability Days… thing.
And apparently that doesn't work for log file updates, so we need to go back and change the log file, the configuration for… Just the log file maintenance.
But then it also doesn't… give us the same effect that we would want to have from stability days, so we also need to look into probably making changes to the NPMRC file.
To make sure that… On dire.
Like, days of a certain age are pulled in.
Or packages that have been published before a certain amount of days have been… Are being pulled in here.
I created a ticket to work on that.
Maybe somebody is interested in picking that up, it should be fairly easy to… configure, we just need to figure out, if the NPM versions that we use Are compatible with the option there.
But it's… why we've been kind of accumulating, warnings when NPM installing on the audit step.
Because of the… Packages that are outdated there.
Moving on to the next one… I guess it might be a good time to revisit this. I had initially mentioned that, Might be best to… Keep this open until 3.0, and then switch everything over to this, to time the braking change.
If anybody has an opposing opinion.
Please feel free to just note it on the PR.
It is just a suggestion from my side, we don't have to do it.
That way, I would put the never-stay label on it, to avoid it getting auto-closed, and then us forgetting about it.
But… yeah.
That's this PR here.
This one I had talked earlier, this is Marilla's PR about, moving everything to the stable semconf.
There's also a PR in the contract repo, so if anybody's interested in reviewing that one.
Would also be very much appreciated. I'm gonna go through it.
tomorrow. I'm, like, halfway through the PR now. There's a lot of removed lines, that… generated the Word SamConf and tested it and stuff.
Ideally, I would like to merge both of these in the same release cycle, so that for end users, it's one Just one break, with one release, instead of it being spread out over, over multiple… Weeks.
Which might be… More annoying than having everything change at once.
Yeah, as mentioned earlier, if there's any objections that you have, please, also note them on the PR there.
Then we have… PRs waiting on reviewers, It looks like that had activity 9 hours ago.
So, there's gonna be a shallow merge now.
Yeah, I'll probably have to look into that a bit closer. It's always a bit… Challenging to find out what actually happens with all of these config options there.
And we have this PR by Trent, avoiding double wrapping of HTTP.
David Luna Bistuer 00:26:05 Yeah, there's, now I remember there's a result of comment from me.
Or at least the experience that I have from browser is that… easily.
UCAF, well… Someone else could be grabbing.
the API. I guess it's not the case and not.
So, I think that I'm good with that, so I'll give another round of review on… Let me be put a stamina.
But in… but in browser, it's, we, we got a couple of… issues that we have to solve for fetch and XML HTTP requests.
That someone else was grabbing it by some library.
Not specifically to be an agent or an instrumentation library.
But another library that was instrumenting the… the same APIs. So we were getting errors.
And we had to work with that, so we came with a differentiation.
So we wrap it once when enabling it, and then we get the… the wrap, you know, the wrap method there, so we've been… we never unwrapped it.
And then we are keeping a state that is enabled or disabled, if the instrumentation is enabled or disabled.
I guess that's fine, not…
Marc Pichler (Dynatrace) 00:27:22 Yeah, it's, I guess there's still some possibility that people are pitching that, for one reason or another.
This is probably something that would be, solved by having tracing channel.
support, because then we wouldn't need to patch it all, and we don't need to go through that.
David Luna Bistuer 00:27:47 Exactly.
But this, based on the number of issues, I think that we are safe here now, so… There are more users in notes, and we are now… we haven't had any issue.
For this module.
So I guess that's… that's fine.
Marc Pichler (Dynatrace) 00:28:05 Yeah, then I think that that should be good. I would have to look into it a bit more deeply to be able to make a… Good statement about this.
Maybe since I've brought up the tracing general stuff, we could, look into some… Tracing channel related.
PR, that I did open. So… I've actually been prototyping this, what, Shangsheng, mentioned here about this, using the symbol dispose, and… Using this width scope.
thing.
I'm just wondering all of yours… opinions on… how to best do this. So this PR… Is kind of on purpose, not… Wrapping the context in another object, because… attaching and detaching the context is something that I assume would happen quite often. So, like, having one object every time By doing that, might just add a bunch of, like, small objects that need to be garbage collected.
The… thing that's suggested here is to use this width scope thing, but I suppose this one also, Generates an object that, then has this dispose method on it.
So I think we would run into the same issue. I did run some benchmarks to just see… Like, how it would fare against, our… with implementation, so we have this context with where you can pass in, function, and it seems to be pretty much on par. I didn't measure the garbage collection performance on it yet.
So I'm just asking in the round what you would prefer here.
I had this… Idea of possibly having, like, something, like… This utility function, which then… lets you choose what to use.
So it would avoid the extra allocation.
When you're just using context attached, and then if you want to, actually… Have a disposable, you would do attached disposable, and you would take the performance hit.
Of doing that, since it's a low-level API, I think, should be fine if it's… A bit more clunky to use, because most people should never directly interact with it.
Daniel Dyla (Dynatrace) 00:31:13 What's the performance hit? It's just the creation of that object.
Marc Pichler (Dynatrace) 00:31:17 Yes, exactly. So it's this… you know, I'm just creating… I'm returning a new object that has this dispose.
Thing on it.
And one of the things I've been thinking about is, maybe we could have a pool of, like, tokens that we rotate through, so at some point it would saturate, and, like, as a token is disposed, it's free again, and we just reuse it, But it feels like it's adding a bunch of complexity.
To the whole thing.
And…
Daniel Dyla (Dynatrace) 00:31:52 Yeah, is it enough of a performance benefit, I think, I wonder, to justify the complexity?
Marc Pichler (Dynatrace) 00:32:00 Yeah, there's, I would do some measurements and see if, like, what the actual impact on garbage collection time is.
I'm just assuming that… for example, for GraphQL, and stuff like that, where you would… Have a bunch of resolvers running.
There's always need to attach and detach context.
Generating one new object all the time might be, not advantageous to performance.
But… ever… Try both and see… What the impact is there?
And then I note it on the PR here.
Yeah, I'm not sure if, Anyone has done that, maybe, in, some… Other place, and run into similar things with context management before.
Daniel Dyla (Dynatrace) 00:33:06 One thing we could do is… We could reuse the context object itself, I guess, for returning We were returning a token.
Marc Pichler (Dynatrace) 00:33:28 Yeah, that's what I meant earlier with, like, having a pool of tokens.
is to have… like, I don't know, let's say… A hundred, or, like, a configurable amount of tokens.
They're just being reused all the time, so… If you attach, it just takes from that pool.
Puts the context in there, because the context object is already allocated, right?
And then hands that to the user. The user then detaches that at some point.
Takes that token object and then puts it back into the pool.
But then if you keep holding on to the token object, and you detach it later, it might start breaking stuff.
Daniel Dyla (Dynatrace) 00:34:12 Yeah, and how big is that pool? You're then introducing, like, a max debt.
Marc Pichler (Dynatrace) 00:34:18 Yep.
So, yeah, I think that the only way to answer the question would be by me going and doing some benchmarks and seeing.
Daniel Dyla (Dynatrace) 00:34:31 And it…
Marc Pichler (Dynatrace) 00:34:31 the embedd.
Daniel Dyla (Dynatrace) 00:34:32 what I meant… And I don't know if this is even possible, it's because that token is a… symbol, right?
Marc Pichler (Dynatrace) 00:34:45 Token itself is, is really just a type that I cast the context to, so that's why I don't need any extra locations for.
Daniel Dyla (Dynatrace) 00:34:55 But it's a context.
Marc Pichler (Dynatrace) 00:34:56 Yeah, it's actually called…
Daniel Dyla (Dynatrace) 00:34:57 Why couldn't we just… Add the symbol.dispose property to that contact, like, directly onto it, and then you could… use the using directive. It would still just be the context itself, though.
Marc Pichler (Dynatrace) 00:35:17 Yeah, I'm… I have thought about this, but if some other… Like… When you… when you use that context before, and you kind of hold onto it.
It will suddenly get, like, a dispose symbol on it, and you could use that dispose symbol. That's not the problem for, people that are using, TypeScript and are adhering to the types, but to somebody who might be ignoring these, like a plain JavaScript user, they would just see, thing that they could use, and they might invoke it. It's more of an esoteric problem, I think.
But it's still possible.
I think we wouldn't want to have, like, a dispose symbol all the time on it, because that might interfere with some of the other context APIs that we have.
Which I would like to avoid.
Daniel Dyla (Dynatrace) 00:36:23 Okay.
Marc Pichler (Dynatrace) 00:36:35 Oh yeah, that's, different ways that we could do it, I guess.
I'll just do some benchmarks, and then I'll get back to this PR.
And we'll mention it on here.
One thing to note, I actually do like this, being able to… like, just attach and have this using thing, it's, I played around with it locally, and it is very… Feels very ergonomic. So, if we could have that, then… I think it would be.
Would be great to implement it this way.
Alright, Moving on.
We were… Stopped here, so… This is for the benchmarks thing, updating the… Ubuntu, image that's being used. I think the benchmarks had a little bit of an issue, because the runner is… not responding, not picking up any chops, so I'll actually leave that, until that situation is resolved. I think it's, The same issue that we had seen before, where it ran out of space, and then, Wasn't happy to pick up any jobs anymore.
then this PR here is, factory pattern for the tracer provider, I think the main idea here is to just patch the tracer provider.
Daniel Dyla (Dynatrace) 00:38:58 Yeah, that's exactly what it is. It's, like, us introducing an API that allows them to replace it on… like, creation?
I… I don't know how much I love this.
like, it says it avoids monkey patching, I'm not entirely, like… Monkey patching is what they're gonna do, or wrapping of some kind anyway, it's just… They want us to… make guarantees about where it will be that they can find it to Monkey Patch.
I'm… I'd be interested in seeing the other half of this, to see how the full thing works.
Obviously it's… They're kind of… internal SDK that's doing it, so they may not… Really want to share that, but… I feel like there should be… a better way. What they really want is a way for their SDK to work both backwards and forwards compatible with different SDK versions.
Or API versions, or whatever.
I… I understand that motivation, and I also want that, I just think there must be a better way to handle it.
Marc Pichler (Dynatrace) 00:40:33 So that's where API 2.0 POC comes in.
Daniel Dyla (Dynatrace) 00:40:39 Yeah, the whole… the tracing channel thing solves this, too.
It's obviously, like, a way, way bigger change.
Marc Pichler (Dynatrace) 00:40:54 The tracing channel thing would serve it, because, we would… They could just have their own thing run side by side, right?
Daniel Dyla (Dynatrace) 00:41:05 So, the problem they have is if we add a new method that they don't have yet, It ends up, like, not fulfilling the interface, and if they just cast it, then it's like a runtime failure.
the way that Tracing Channel solves that is that… new features… are new channels, so if an SDK doesn't listen to them, they just… No op, and it's fine.
Marc Pichler (Dynatrace) 00:41:34 You, you meant, you meant, having the SDK emit events as tracing channels.
Daniel Dyla (Dynatrace) 00:41:42 in having the API emit events as tracing channels that the SDK then picks up.
So the… I think what they're doing here is what they want… is… for the… when you… when you create a tracer provider, the SDK creates a tracer provider through this Like, factory, and what they want is to be able to attach No ops to anything they don't.
like, recognize.
And the tracing channel solves that because everything is no-op by default.
This is a way less impactful change.
It just strikes me as, like, a little bit… You know, they just want us to make guarantees about, like, Internal shapes of things.
is kind of what this looks like. The factory… is something that… somebody who's not using Datadog would never use.
other vendors could potentially do the same thing. So, I mean, it's not like it's a Datadog-specific feature, but right now.
Datadog would be the only user. And, like, pure upstream hotel users would never use it. They wouldn't have any reason to.
Marc Pichler (Dynatrace) 00:43:18 I'm actually wondering if the idea is to attach no ops to… an SDK, if we could… Provide that as a… Separate package.
For that, we would have to… So, so the idea would be to, like, before registering it, always pass it through that.
And attaching the no-ups there.
So… You would.
Pass your tracer provider, which might be of any version, to the… Patching function, and then pass whatever output from that patching function.
Into the register.
Method there.
So you would end up with, actually properly patched version that might… Be implementing half of… what the Auto API service is.
And it would always be up-to-date, because it would force us to also implement this.
Whenever we release a new API version, we would have to update that patching functionality there, too.
We might be able to even make it more convenient with types where we have one, Type that we deliver to users that is not supposed to be implementable and have one type that's, implementable, which might only get new functionality, via Optioner.
We are optional.
Properties that are being added.
It's also quite a big change, though.
It would be… It's difficult to find out if that… Would be forwards compatible with spec changes?
Because the spec might define some new, Functionality where you pass in, Span, for instance, and What our no-op returns is not.
Like… what people expect, and it's an OAB.
And, if the operation there is, let's say, ending a span, or supposed to be ending a span, then we'll end up with memory leaks.
So I just stocked myself out of that idea.
Daniel Dyla (Dynatrace) 00:46:17 Yeah, and like I said, I'd want to see the other half of this solution, right? Like, this is providing an API that… does nothing on its own. Like, the factory that they… have in this PR doesn't change it in any way.
it just allows them to register their own factory. And I'd be interested to see what that factory is doing behind the scenes.
Because it might be something we could just implement on our side. There must be some reason they didn't do that, though, because if they were… if they… Have some method to just take any arbitrary tracer provider and make it up-to-date for the API.
Then why wouldn't they have just… suggested that solution to the API and updated the register function.
So there must be something else that they're doing.
And I'm just not sure…
Marc Pichler (Dynatrace) 00:47:26 Yeah. Do you want to ping them again on the PR? It looks like they said that this will be put on hold for a while, Maybe it's not even applicable to them anymore, and they found a different solution for it.
Daniel Dyla (Dynatrace) 00:47:41 No, I'm sure it is applicable. I'll… I can reach out. I'll make a comment on the PR.
I just feel like I don't want to merge this without… Fully understanding how the solution is supposed to work.
Marc Pichler (Dynatrace) 00:47:57 I agree.
I think, just merging this… Especially into the API package, which… We cannot change.
After we merge something.
Without understanding it is not the way to go here.
Daniel Dyla (Dynatrace) 00:48:15 Yeah.
Marc Pichler (Dynatrace) 00:48:16 So I agree there.
Yeah, thanks for, looking into that one again.
Daniel Dyla (Dynatrace) 00:48:24 Yeah, no problem.
Marc Pichler (Dynatrace) 00:48:32 Definitely an interesting one.
Alright, this one I think we talked about last week, I didn't get back to it.
Yet… try to pick that up next. I… Did get the other PR merged that I had.
Taken stewardship off, so I can pick up a new one, and that one's it.
I think I'm assigned to this one already, so I get… To look at that one, too, then.
Then we have a bunch of renovate issues. I guess we can close this, see none one, because… At some point, I did update to… 18… And then I tried to update it.
I tried to update to 19 or 20, and didn't get any further, because the tests were timing out and breaking, and… This needs some manual intervention at some point. Maybe our add… Let the… AI agent look into it at some point.
They tend to be… We could, then… If one has to dig through stuff.
Manually, and these types.
I have the same problem, so we can also close that for now.
Alright.
This PR here is mostly an issue, because we have outdated… outdated examples. This is the gRPC example.
That needs updating.
I will leave that open for now.
So that we can get back to that another time.
By just deleting the example, we would be able to just, like, have this PR auto-close.
config option for Prometheus, default aggregation.
It's aggregation itself, not the aggregation temporality, I was confused there for a second.
We have these aggregation option things.
I have to look into that a bit deeper, if that's… the best way to go about it. I think in… The periodic exporting metric reader, we had a different way of… Providing an aggregation selector.
If I recall correctly, this is a function.
And the function always implies that, it might be able to change after it's registered.
And return different aggregations.
Which is… Semi-true with this one.
It can return different aggregations, but it will only apply to new, New instruments that are being created, so… Using a function for it is a bit of a blunder, because the function always has to be pure, and it's not really documented anywhere.
I'll actually assign this to myself so that I can… Type this up.
And… let them know what the issue is, because the change itself, I think, is, spec compliant, and… Makes sense. We just have to make sure that… the API is… Not confusing in the end.
Right, this one we have said we're gonna… A merge once we get started with… Sdk3.0, Hmm… And this one is still waiting for the… -Oh.
Status, this is the release days, or, like… stability days thing, that I talked about earlier.
Just prevents us from merging stuff that, hasn't been out.
For too long yet.
That title also seems very interesting. Set clock and get tick methods to context API. I'm wondering… Why the context?
Daniel Dyla (Dynatrace) 00:54:08 I think you're getting a tick because you're not necessarily getting the current time. It depends on the clock implementation, or what it returns. Like, is it returning… Current epoch time, or is it returning time since… The start of the application.
I think GitTick is just a more generic name for…
Marc Pichler (Dynatrace) 00:54:36 Yeah, one of the things I'm wondering is why it's on the context API.
It seems that… Yeah, probably just because, like, all the SDKs use it.
It's actually not on the context API, it's on the span. There's something different here.
Daniel Dyla (Dynatrace) 00:55:00 Yeah, it's just a misnomer. Probably they had some idea, and then decided to go a different way after they…
Marc Pichler (Dynatrace) 00:55:10 Hmm.
I think if we were to… Have something like that.
We would probably not want to have it like this on the span, but we would inject it through the… Tracer provider constructor.
Daniel Dyla (Dynatrace) 00:55:28 Yeah, because the span implementation is not meant to be… I mean, this isn't even public, right? You'd have to, like, import it.
Marc Pichler (Dynatrace) 00:55:36 Hmm.
Yeah, you would have to… imported, or the span that you get from the API is still the same implementation underneath, so you could probably.
Daniel Dyla (Dynatrace) 00:55:47 Yeah, but the span you get from the.
Marc Pichler (Dynatrace) 00:55:49 Absolutely.
Daniel Dyla (Dynatrace) 00:55:49 I is, in instance, so you can't get the static methods anyway.
Marc Pichler (Dynatrace) 00:55:56 Yeah, you're right.
And… This implementation isn't public, so they would have no way to import this.
Daniel Dyla (Dynatrace) 00:56:07 Yeah, yeah, I'm sure that they're just importing… like, a deep… import.
Which we don't want them to do anyway.
I would say, good idea. This is a extremely… Naive implementation of it.
Marc Pichler (Dynatrace) 00:56:33 So is this something that we, like… would want.
Daniel Dyla (Dynatrace) 00:56:38 Edge.
Marc Pichler (Dynatrace) 00:56:39 Fort.
Daniel Dyla (Dynatrace) 00:56:40 Custom clocks, as an idea, maybe?
I think anybody that looks at our… clock… having… I'm the person that did all this, right? Like, this… this hairball was spun by me.
And it's super complex.
And people look at it and say, this should not be this complex. And they're correct.
It should not be.
But, if you simplify it, which this is attempting to just… Tack on sort of a simple solution.
You were going to run into all the same problems that, like.
If we were… we could have just used date.now everywhere. That would have been the simple solution, and it would be wrong in surprising cases. And I… to me.
this implementation Tells me this user does not fully understand what is going on with all of the clock internals.
And bringing your own clock as a feature?
opens us up to a lot of those, like, you know, people are like, I don't understand why the time thing is so… And it's just like, I'm gonna add my own little thing here.
Marc Pichler (Dynatrace) 00:57:57 And then they end up with incorrect timestamps, and…
Daniel Dyla (Dynatrace) 00:58:01 Yeah, yeah, exactly.
Marc Pichler (Dynatrace) 00:58:03 Either don't notice, or notice too late.
Daniel Dyla (Dynatrace) 00:58:09 Yeah.
Marc Pichler (Dynatrace) 00:58:10 Yeah.
Daniel Dyla (Dynatrace) 00:58:10 I mean, I would have made the timing logic simple.
If I could have. It was simple before I did all this.
Marc Pichler (Dynatrace) 00:58:18 Yeah, I remember the, the horror.
Discussions around this, and it, Ended up being very complex, and everything, like, every single line of code in there has a reason.
Daniel Dyla (Dynatrace) 00:58:31 Yeah.
Marc Pichler (Dynatrace) 00:58:32 So…
Daniel Dyla (Dynatrace) 00:58:32 the clocks, like, they pause at weird times, and it depends on, like, are you in Lambda, or are you in an Edge worker, or is this a, like, WebAssembly? Like, every runtime has its own little weirdnesses.
I… I… kind of… this piece of code is one of those Ear Be Dragons types of things that… It seems to work.
And I'm afraid to change it.
So they're currently monkey patching to get that level of granularity. What granularity are they expecting?
It says that level of granularity. Can you scroll up and see, like… I would pass a function which returns at the time.
I don't know what they're doing.
They might be returning partial times, because, like… performance.now returns an integer, they might be returning a float.
And they're probably running into weird rounding issues, and they may not even realize it.
If this person wants to come to a meeting and argue for this feature and convince me that they know what they're doing, they're welcome to. But I'm not… Very convinced by a three-line change.
Marc Pichler (Dynatrace) 01:00:15 Yes.
I think the person that opened the PR is a different one as well.
Yeah, I guess we would need to triage the issue here first, and make a decision before accepting any PRs.
I can also type up an answer for that.
And then we…
Daniel Dyla (Dynatrace) 01:00:38 Yeah, I'd like to see a full description of, like, what is the specific problem they're trying to solve here, and how this solves it.
Marc Pichler (Dynatrace) 01:00:46 Yep.
Alright, I think we're out of time. I will, Type that up here, and let them know that, this is what we would like to see.
And… Then we can go from there.
Alright, thank you.
Daniel Dyla (Dynatrace) 01:01:15 Thanks, Mark.
Marc Pichler (Dynatrace) 01:01:15 for training.
Have a nice week, and see you in… Two weeks.
Matt Wear 01:01:22 Nice to you.
Hector Hernandez 01:01:23 Thank you.

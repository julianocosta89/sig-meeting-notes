SIG: Ruby SIG
Date: 2026-06-23
Duration: 38 minutes
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 00:42 Hello.
It's gonna…
**Arjun Rajappa** 00:46 Hello.
**Kayla Reopelle** 00:47 One more minute before getting started.
And if there's anything you want to chat about today, here's a link to the agenda.
All right, hello everybody. I guess we can go ahead and get started.
I'll share my screen.
I think this is the one.
The… Link to the agendas in the chat if you have anything you want to discuss today.
You can start with the SpecSig while everyone's thinking about it.
So… The telemetry policy, OTEP, sounds like it's going to be merged next week, so they're looking… oh man, my connection's kind of slow today.
They're looking for any… Last questions, bits of feedback, anything that might be blocking, so if you have thoughts on this, time is of the essence.
There was also a bit of a discussion about metric prefixes, adding prefixes to metric names.
It This was one where, in my commute, things were a little distracting.
But I picked up that metric views are also… Somewhat connected, let's see what the notes were. They're wondering if this can be accomplished with views. Oh, that's right, there was also… some folks who had discussions on, like, our ideas about changing the way that views work overall, to kind of make them better, since it's a tricky UX experience. So we may have more Stuff about views coming soon.
This discussion… Was kind of interesting related to some of the SEMCOMF work that we're doing.
The GenAI SUMConv just marked a bunch of, values as deprecated.
And that raised some concerns for the Go implementation. What they were looking for, because of the way that Go works, like, each package name has to be unique, and every version is kind of its own package, and so having a bunch of deprecated, values and things that they… Just based on how their setup was, that they'd need to remove, was a little jarring.
And… So, this kind of got into a bigger discussion about, like.
what even makes, like, a valid SEMCOM, like, instance? Like, is attributes what makes something adhere to the CENCOM? Is it the particular piece of telemetry?
the things that I think could be interesting for us, because we've had some discussions about schema URLs, somewhat recently, is that, there may be a proposal in the future to change schema URLs so that they're more signal-specific, or category-specific.
just to kind of avoid concerns about, like, a single span, for example, you know, with GenAI maybe having, like, an equal value for HTTP or, Gen AI conventions. I think because we are… saving all of the incubating attributes as constants that, even if they get deprecated, we still ship those constants in the semconconf package.
This, you know, mass deprecation doesn't really impact us too, too much.
The other thing… there's some stuff about… the post-graduation roadmap. I don't feel really prepared to talk about this one today, but I think there are some things about Contrib that we can, Bring questions for next week.
I was wondering, Matt, if you would be willing to talk a little bit about system packages, since it sounded like from the meeting that you're working on a prototype for them?
**Matt Wear** 06:08 Yeah, the… I guess I'm working on a POC for adding Ruby to the OpenTelemetry injector.
So, this is possible because Schwan recently created the, Ruby Auto Instrumentation Gem, which is kind of a dependency of that. It's not actually released yet, but I'm able to kind of… Work with it from a vendored state, but, But, yeah, I think basically this all kind of rolls up to, I think the injector does roll up into packaging, I'm not sure exactly how that works just yet.
But, but the idea is that… It's kind of similar, I guess, to, the way that the, hotel operator will kind of instrument your applications for you if you weren't using the operator. Instead, we're doing it through the injector, or… packaging, mechanism, then kind of the injector, I guess, would play that role that the, that the operator plays, if that makes sense. But it's basically zero code, Zero code change instrumentation of your application.
It's a… another mechanism of that.
**Kayla Reopelle** 07:35 Okay, nice.
So, the operator is more like for Kubernetes, what environments would the injector be used in?
**Matt Wear** 07:45 I think the injector is going to be Linux… Linux-based, systems.
**Kayla Reopelle** 07:52 Okay.
Sweet.
Cool. Well, thank you for working on that. And I'm glad that the instrumentation gem… we're getting really close, we just have some, like, secret issues that we… I mean, not issues that are secrets, but… You know what I mean? That we have to figure out, and then it should be ready to go after that.
But I'm glad you're able to use it in the vendored state.
**Matt Wear** 08:16 Yeah, I am. I… I am wondering about… Yeah, it's probably, like, a side topic, but, like… Patching bundler require is kind of the mechanism that we're using, and it works awesome for anything that calls bundler require. For anything else, it's a little bit…
**Kayla Reopelle** 08:37 Yeah.
**Matt Wear** 08:38 less awesome. Is that… Is that just the best?
The best overall, way to do things, or the best that we know of so far.
**Kayla Reopelle** 08:47 That's the best that we've found so far, that, like.
you know, as long as… it works in most scenarios, yeah, unless you're not calling bundler require, so… I forget, we looked into some of the other Like, auto instrumentation type… Implementations, and there were always, like.
I think, like, a few more steps that you needed to do to your environment. Hannah, I know you looked into this a while ago, I'm not sure… If you remember what, like, the trade-offs were specifically for the other styles, but, Yeah, I think if you can find a better option, that would be awesome, but, that was the most… Compact solution that we could find.
**Hannah Ramadan** 09:36 Yeah, I don't remember the exact trade-offs, and we did, on the New Relic side, have an issue.
with Sinatra apps that don't call, bundler, require, like, I think Rails does, so that's, like.
not such an issue, but yeah, Sinatra definitely, like, doesn't need to, it's… and so that's, like, one small issue that we ran into, but… Yeah, I don't remember the other approaches. I do think that Datadog actually did do it a little bit differently, I think they did something with the gem file.
But yeah, I don't know, maybe I could find, like… I'm sure we have, like, a dox or trade-off somewhere, I can, like, look for that.
**Kayla Reopelle** 10:22 Yeah.
**Matt Wear** 10:23 Cool, yeah, no, that's fine. I, For now, I'm just going to, go forward with the kind of requirement that your app needs to call bundle required, or you manually need to, set the environment variable, for auto insurance… the auto instrumentation jump to do that.
And then… Yeah, you know, if… If we can find something that's going to be, like, a little bit… That's gonna be completely friction-free, then… then maybe we go that route, but it sounds like there's been… A lot of investigation into this, and… They probably all… all have a trade-off, but.
**Kayla Reopelle** 11:07 And I think it's been a few years since we've looked at it, so maybe some things have changed, too, in the ecosystem itself, and there's new options.
**Matt Wear** 11:17 Cool, yeah, I'll have a look around and see if anything, like, stands out as being maybe… a little less… yeah, has a little less friction, but I'm not sure that I will find anything, so…
**Kayla Reopelle** 11:33 Okay.
Thank you.
**Matt Wear** 11:35 And yeah, and if I come back with something that you already tried and it did not work, then that's fine too, just let me know.
**Kayla Reopelle** 11:41 Okay.
Sounds good. Yeah, it's a… it's an interesting problem, so I feel like everyone's… Eyes and creativity may see things a little differently.
Alright, anonymous bat.
**Matt Wear** 12:04 Oh, that's…
**Kayla Reopelle** 12:04 Who is first on the loose? Is that…
**Matt Wear** 12:06 Probably be…
**Kayla Reopelle** 12:07 Matt? Okay. Yeah, let's… do you want to open up that PR, or just talk more generally?
**Matt Wear** 12:13 I was just talking generally. I was just trying to maybe clean out the things that are easily cleaned out of, core, which are a lot of the dependency update ones.
And I've been, like, looking at, actually, these SEMCONV ones, and… especially after the discussion at the SpecSIG this morning, I just wanted to see, like, if those are actually, like.
Dangerous to, to merge, or if there's any caution, or if generally, as long as the renovate PR is green, we merge it.
And, then the follow-up is that, do we want to, like.
Set it up to auto-release.
**Kayla Reopelle** 12:58 Yeah, I think as long as the renovate PR is green, it should be safe to merge. The couple of issues that we've run into are, like, maybe there's a misspelling somewhere in the semantic conventions, and so C-Spell will fail.
Sometimes there's a new structure that gets introduced to Weaver, and that, Might not be compatible with the way we have things currently set up.
I think my only hesitation with the auto-release would be to make sure that whatever we structure kind of requires Everything to be green, or at least, like, the semantic conventions… Workflows to be green, so that, you know, we're not… like, I know… Sometimes, like, not everything needs to be passing for the next part of the workflow to run, so that would be my only hesitation. But as far as, like, reviewing those PRs.
I've tried, like, doing more in-depth reviews, but ultimately, if Seaspell and RuboCop both look good, then there isn't much more that I look into at this point.
**Matt Wear** 14:15 Cool, yeah, I just wanted to make sure that they… Generally weren't risky, and it sounds like the…
**Kayla Reopelle** 14:21 Yeah.
**Matt Wear** 14:23 the auto-release… Needs to just, like, Need to verify that it's not going to accidentally release something bad, so we need to make sure that enough things are green, whatever those actually are.
**Kayla Reopelle** 14:52 Yep. Yeah, and I think there is a pull request to do auto-release, but I haven't reviewed that one yet. We've only had.
**Matt Wear** 15:01 I think it might be that second link, 2185?
**Kayla Reopelle** 15:04 Oh, I see. This… this one?
**Matt Wear** 15:07 Yeah.
Cool.
For some reason…
**Kayla Reopelle** 15:12 Added some extra, maybe there's a space in there.
Yeah, this one.
So it… Whenever there's a push to that… It'll try to release.
So, the auto-release opens… Only when… We've merged the other one.
I guess maybe I'm not reading this correctly.
Oh, okay. Yeah, I think that… that's a… a good structure.
Just to, yeah, make sure that we're not lagging too much. That does bring up one other question that was raised after the last SEMCOM release. So our versioning for SEMCOM is a little… weird in the gems, because we, We go off of the semantic conventions version now, rather than… the, like, doing a more standard SEMCOM route. The issue that came up with 141 is that we didn't release 141.0. There was already a patch for the 141 semantic conventions.
when we had the PR opened, and so… This version is technically mapping to 141.1.
But down here, this, like, 137.1 is actually pointing to 137.0. The .1 is just because we needed to make a change to the semantic conventions gem itself, the way that the workflow runs.
So my question is, like, for readability.
should we add, I guess, like, a patch, or whatever, a teeny version? Like, one more… version at the end of this, so that if we need to make gem changes, like, that's what we increment. And since the semantic convention versions, you know, can have 3 places, just always reserve those 3 places for that situation.
**Matt Wear** 18:04 not been in a situation where I've had to add an extra digit to the version, and I'm just wondering what… Complications that might, cause…
**Kayla Reopelle** 18:15 Yeah… Yeah, I don't know. I could reach out to Daniel to make sure it's something that's doable in… the toys gem. I feel like we might have talked about it before, and it was okay.
But… Yeah, I guess right now this isn't… technically correct if we're following the exact mapping of SMCOM version to GEM version. It just felt also kind of weird to release a 141.1 without releasing 141.0.
**Matt Wear** 18:54 Yeah, it's a weird thing, actually. So, is that one of the things that… that PR is attempting to solve, is so that we are kind of in lockstep and don't miss a version?
**Kayla Reopelle** 19:05 Yeah, exactly.
It still requires us to see and review that pull request.
Before the next one is released, because otherwise Renovate will close.
and reopen for the point versions. So I guess that could be another solution, is that we, like, try to change the renovate workflow to require a PR for every version, even… Minor patch versions.
**Matt Wear** 19:38 Yeah, I think… If we can do that, it sounds like we solve, like, 90%.
**Kayla Reopelle** 19:45 I agree.
**Matt Wear** 19:45 5%, maybe 99% of the.
**Kayla Reopelle** 19:48 issues here.
**Matt Wear** 19:49 Then we can maybe defer, thinking about the… the TD, which would just be for… For if we had to change anything, which hopefully… is rare.
**Kayla Reopelle** 20:02 Yeah.
And then also change the renovate version.
Or the renovate, to make sure that we have a release even for patch versions.
**Matt Wear** 20:34 Yeah, that's something that's easy enough to do.
**Kayla Reopelle** 20:36 I… I think so, we'll find out. I can take that home.
Cool.
Great.
Okay, anything else on semantic conventions before we move on?
**Bart de Water** 20:56 I, have a PR that I need to push up.
But I complained last week about the pain of having to manually require parts of semantic conventions that I need.
**Kayla Reopelle** 21:07 Oh, yeah, yeah.
**Bart de Water** 21:08 Yeah, but it seems that this is actually pretty doable with auto-loading, and the PR is, like, pretty small. It adds an extra stage to the, to the Weaver pipeline to generate, sort of like a semconf index file, and that declares all the autoloads.
So that when you then do, OTel semconconf, like, say, DB, it'll auto-load the DB file, and you don't have to manually require it anymore.
So, you still have best of both worlds, you don't load a lot of strings that you don't need, which was the concern that you surfaced, but then also, you don't need to manually require it in every file, and… Yeah, I have to deal with that. So, I'll push that up later.
**Kayla Reopelle** 21:51 Okay, sounds good, thank you.
Alright, that's this guy.
Oh, also related. Okay, I see what's happening now.
Yeah, so I guess before… We merge this one, or will we just accept that the gem version is different, or should… I push up, like, an empty release that's identical for 141.1.
**Matt Wear** 22:34 What do you think?
**Kayla Reopelle** 22:39 Maybe… I'm leaning towards pushing up an empty… release, I think things will be a little bit weird, but if 141.1 is going to be the last 141… Version, like, maybe that helps with, schema URLs, which we haven't actually solved yet, or figured out how to use correctly.
Or we can accept that it's just a problem, and if it does become an actual… like, it could be a problem, and if it does actually become a problem, then we can work to make a release to fix it as well.
**Matt Wear** 23:23 I'm fine either way. If… if you think it's easy just to push up another one and avoid the problem altogether, then maybe do that, then we merge that, then this.
then the PR to auto-release, and then hopefully these problems go away.
**Kayla Reopelle** 23:39 Yeah, okay.
I will see how difficult that is.
Anything else? Well, I guess we don't have anything else on the agenda, so anything else on core before we just start looking at… Stuff.
Sounds good. Alright, let's see who we have.
Yeah, we have some of those. Renovate PRs, it looks like some are approved. We cleared out those PRs that were called out in the… Whatchamacallit?
I see we have two declarative config PRs. I apologize, I did not get a chance to look at this last week.
Arjun, I see you here. Did you want to chat about any of, your PRs that you have opened?
**Arjun Rajappa** 25:16 This week, I'll spend some time on this and finalize this.
**Kayla Reopelle** 25:22 Okay.
Sounds good.
I guess… With this one, It has been approved, it does have a… maybe I'll just reach out to Robert one more time and see if he can take a look, because it's failing on just a RoboCop issue.
So it doesn't feel like it's a huge thing, but I was kind of waiting to review it more fully until the RoboCop was fixed.
So I'll… I'll check in with him on that.
Okay, and issues… Nothing new this week. This was a… something I noticed, there was a… recent pull requests to bump Minitest, and I've seen this happen in a few PRs lately, that Jaeger is getting its dependencies updated as well, even though we're not that gem is, like, deprecated, and we're not gonna make any more changes to the code itself. So I think contrib has a… section and renovate to exclude deprecated repos, and we should probably do the same thing for, the Acre repo in Core 2.
Or, not repo, but gem.
Okay, any contribib topics before we just open up the general?
Page… Alright, I see you have a new PR.
**Bart de Water** 27:27 Yeah, related to some work that I've been doing, I was like, this could be useful to have. Maybe the… the first commit is pretty straightforward. I think the second one is maybe… It's a bit more forward-looking with adding an attribute that is… has a proposal in ZenConf, but sort of, like, hasn't fully gone through the motions yet.
But… I think it'll be very useful to have, because sometimes, you know, like, you have a query that, like, affects a lot of rows, but doesn't necessarily return them.
And I follow the SEMCOMF proposal's definition of when we should be counting them and not, because otherwise the PG adapter itself will just always give Like, a zero integer in case, which is not the end of the world, if we prefer to, like.
not, sort of, like, have the pending SENCONF proposal decide what we should be returning, and if we just say that, like, this returns the raw adapt, database adapter value.
**Kayla Reopelle** 28:33 Okay.
**Bart de Water** 28:35 Which, by the way, if I remember correctly, I also looked at what Active Records instrumentation does, and that also always does just return what the Postgres adapter would return. So, there is some precedent in the community, I guess, for just passing it through raw and not trying to… Add any interpretation on top of it when to surface that number or not.
**Kayla Reopelle** 29:00 Thank you.
Hannah, the first… I mean, the first thing that comes to mind is, like, our SEMCOM migration for our database adapters. Hannah, how do you think this fits into that migration?
**Hannah Ramadan** 29:16 Yeah, I think I'd probably want to see this merged first. I have a draft PR that does all the duplication for that environment variable.
been a bit slow to get that done, so I think if we can do this, and I'll take a look at this PR as well, and then… start working on the rest of the migrations. I think that would probably be the best path.
**Kayla Reopelle** 29:42 Even though it's, like, mixing SEM versions between… like, it's an unstable attribute, but… It's… it's, like, past, I guess, the version that we currently have.
**Hannah Ramadan** 29:57 Right, I think I… wouldn't… odd… Oh, I see what you're saying, okay.
**Kayla Reopelle** 30:06 I, I.
**Bart de Water** 30:06 Yeah, it's like a proposal that barely has even gotten traction at this point, so it's a bit speculative.
**Kayla Reopelle** 30:16 And I guess I don't even know if our current gems, like, have a consistent SEMCOM version, like, maybe they're already mixing things?
**Bart de Water** 30:26 I think this particular implementation even just, like, has raw strings and doesn't actually rely on any of the constants, so there's… that was actually come to realize it's also a bit of an open question of, like, should it be using the constants? Is there an effort to migrate over to constants? .
**Kayla Reopelle** 30:46 Yeah, that's… that's a.
**Bart de Water** 30:47 Great about that.
the pattern as it was, I was like, I'm gonna open one can of worms at a time.
**Kayla Reopelle** 30:52 I appreciate that, we don't need worms everywhere, we can keep them.
contained.
I guess the Trilogy adapter…
**Bart de Water** 31:02 Yeah, that one seems to have stalled out. I, if we're settling on an approach here, I can take a stab at recreating one for Trilogy, so that there's a bit of equivalence, because I'm, Because, my understanding was that it needs to be… at least SEMCOM says that there has to be an opt-in thing, because you might be leaking sensitive data that way.
**Kayla Reopelle** 31:25 So we figured.
**Bart de Water** 31:26 I'm following at least that, like, that part of the semconf, attributes.
**Kayla Reopelle** 31:33 Okay, so are they both opt-in, or is.
**Bart de Water** 31:35 They're both opt-in, yes.
**Kayla Reopelle** 31:37 Okay, so… yeah, so maybe then… With that, the semantic conventions version matters a little.
less? I don't know, semantic conventions are so tricky.
Does anyone else have thoughts?
**Bart de Water** 31:57 They're great when they do what you want them to do.
**Kayla Reopelle** 32:01 Yes.
**Hannah Ramadan** 32:04 I do feel like if they're opt-in, and we are trying to move to stable, it's, like… I think that's okay, too.
like, I like that piece. It makes it feel like… is, like, still experimental in people choosing that. They, like, recognize the risks.
**Bart de Water** 32:28 Yeah, I can tweak the README and the… for the setting, as well, a little bit, that, you know, adding some caveats there that this is not standardized.
**Matt Wear** 32:42 So are these… These, db.response.returnedRows, they're kind of… not firmly specified, he… you just kind of added them in this PR?
**Bart de Water** 32:57 Returned rows is in sendConf, affected rows isn't yet.
**Matt Wear** 33:02 Okay.
**Bart de Water** 33:04 But, like, when you do, say, a delete, you know, you might return 0 rows, but affect 1,000, so I still think it's a very useful thing to have, which is why I added it, and like I said, there's some… prior art here, where the, SQL.ActiveRecord instrumentation does emit both of these as well.
**Matt Wear** 33:26 Right, and this has been open since November, and… Is there any pushback, or…
**Bart de Water** 33:34 No pushback, and this basically raises something that was implemented for Azure Cosmos specifically to a generic DB convention.
**Kayla Reopelle** 33:46 happening.
**Matt Wear** 33:53 Yeah, I mean, I feel like that PR is doing the right thing, I do feel like… I don't see any reason why this shouldn't become part of semantic conventions, but it's like, it's hard to, like, bet on the future, But yeah, I don't think it should hold up your PR at all.
**Kayla Reopelle** 34:26 Nice, and maybe it's a good time… sorry, my tabs are everywhere… maybe it's a good time to go back to that Trilogy PR as well, and now that we have kind of a SEMCOMF…
**Bart de Water** 34:38 Yeah, if this is the direction that we're okay with, I can… ask my friend Claude to redo the same thing.
**Kayla Reopelle** 34:48 That's good, Let's, are folks good to take a look at that this week, and we can reconvene next week?
Take silence as agreement.
Alright, anything else in contrast?
Oh, that's sad.
Riel would like to be moved to Emeritus.
Okay, the rest of these have been open for a while. Is there anything else in Contrib?
People want to talk about today?
Alright, auto instrumentation… Schwan, were you here when Matt was talking about, the… shoot, I already forgot, the injector, project?
**Xuan Cao** 36:01 Yeah, yeah, but, I haven't captured, sorry.
**Kayla Reopelle** 36:07 Okay.
Is there anything on auto instrumentation we want to talk about today?
**Xuan Cao** 36:13 No, no, nothing particularly interesting. One thing just, I think it is a good idea to start adding those to agents from town.
**Kayla Reopelle** 36:25 Nice.
Yeah, that'll be our first one.
**Xuan Cao** 36:35 Oh, and also, I changed the… the check for weekly, not daily.
**Kayla Reopelle** 36:40 Oh, nice.
**Xuan Cao** 36:41 Oh.
Not create too many noise.
**Kayla Reopelle** 36:45 That makes sense.
Okay, great. Cool.
Alright, well that's, our agenda for the day. Is there anything else we want to discuss?
**Bart de Water** 37:14 I had another PR that I think.
**Kayla Reopelle** 37:17 Oh, yeah.
**Bart de Water** 37:18 basically ready… .
**Kayla Reopelle** 37:21 Is it in Contribt?
**Bart de Water** 37:23 In contrip, yeah. 2407, it's a small bug fix.
**Kayla Reopelle** 37:28 Room 7. Oh, okay, sorry that I missed that.
**Bart de Water** 37:31 grape, yeah.
**Kayla Reopelle** 37:41 Is there, anything synchronous you want to talk about this one? Or is it more of, like, a, please take a look this week?
**Bart de Water** 37:49 Just, yeah, just to please take a look.
**Kayla Reopelle** 37:51 Okay, great.
**Bart de Water** 37:53 It's just we're using grape in a slightly different manner, and this is a bug fix for making sure it emits the… The right instrumentation attributes.
**Kayla Reopelle** 38:02 Nice.
Cool, thank you.
Okay, if that's it then, I will see you all next week.
**Matt Wear** 38:28 Yeah, thanks.
**Hannah Ramadan** 38:30 Excellent, too.
**Arjun Rajappa** 38:31 Bye. Bye-bye.

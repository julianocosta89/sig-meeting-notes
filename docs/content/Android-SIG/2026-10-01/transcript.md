SIG: Android SIG
Date: 2026-10-01
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Vishwan aranha** 01:34 Hey, guys.
**Cesar Munoz** 01:35 Good morning. Good afternoon.
**Ben Joseph** 01:39 Nice.
**Hanson Ho** 01:44 Hello.
**Cesar Munoz** 01:46 Hello.
**Jamie Lynch (Palo Alto Networks)** 01:51 Okay.
**Cesar Munoz** 01:53 the So just in case, some of you, might not have… I have not noticed, so Jason, I think he won't join us today.
I think he's on Pto already.
I have a pretty bad sore throat right now, so.
If somebody can… Drive the today's meeting. That that will be very helpful.
**Jamie Lynch (Palo Alto Networks)** 02:27 Yeah, I'm happy to go ahead and do that.
**Cesar Munoz** 02:30 Thank you, Jamie.
**Jamie Lynch (Palo Alto Networks)** 02:33 See if I can share my screen.
So, pretty light agenda so far, so I'll give it a couple of, minutes for folks to… Add items on, and yeah, we can make a stop.
So, I guess we can just make a start on this PR, and then if other folks add items to the agenda, we can follow, follow up on those later.
Okay.
**Vishwan aranha** 04:22 Gonna be a very quick one, just have approvals, I just need someone to merge it. Some maintainer.
**Cesar Munoz** 04:30 All right.
**Jamie Lynch (Palo Alto Networks)** 04:33 Cool. So there's one, two, three approvals.
I'm happy to go that much, if everyone else is.
**Cesar Munoz** 04:42 Yeah, it sounds good to me.
Thank you.
**Jamie Lynch (Palo Alto Networks)** 04:48 There we go.
**Vishwan aranha** 04:51 I have a couple other session and native crash PRs, but you can… you guys can take a look when you get a chance. Some of them are in drafts, but I'm actively updating them.
And yeah, whenever you get a chance. This week, we have been busy with Hackathon at Grafana, so… Haven't looked much into updating anything else.
**Cesar Munoz** 05:11 Thanks Vishwan.
One question. You say those are in draft.
So…
**Vishwan aranha** 05:17 No, someone…
**Cesar Munoz** 05:18 adding.
**Vishwan aranha** 05:18 But the ones which are ready for review, I switched them to ready for review, yeah.
**Cesar Munoz** 05:23 Got it. Thank you.
I'll have a look.
**Jamie Lynch (Palo Alto Networks)** 05:28 Yeah, I'll also try and take a look at anything that's out of draft.
**Vishwan aranha** 05:33 Thank you.
**Jamie Lynch (Palo Alto Networks)** 05:41 Okay, any other topics?
**Ben Joseph** 05:49 So I just pasted one issue. This not, I mean, I create, I think I created the issue, but somebody else has created a PR, for the physical screen tracker.
I know this has been, Let's debate the topic how we want to do this. So I think, like there were some questions, and the author has answered that So, if there's any feedback, if you guys can take a look.
**Jamie Lynch (Palo Alto Networks)** 06:29 Got it. So… That is linked.
So this is the issues we want.
Small screen tracker to have the ability to use composed names along with.
Activities.
In 5 months.
So someone's opened the PR to.
Fix that.
So, what action do you think would be good to take with this? Like, do we need any further discussion on the original issue, or…
**Ben Joseph** 07:19 just.
**Jamie Lynch (Palo Alto Networks)** 07:20 folks to take a look at the PR itself.
**Ben Joseph** 07:23 Yeah, I just wanted to bring your attention. I think this was opened a while ago and like kind of got lost. So just a reminder, that's all.
Home.
**Jamie Lynch (Palo Alto Networks)** 07:38 Cool. Yeah, I can try and take a look at that. Either after this or tomorrow.
I'm… I think Hanson would probably have.
Thoughts as well, as you kind of, like.
Covered the whole navigation tracking in quite a bit of detail.
**Cesar Munoz** 08:04 Yeah, I noticed it's been sitting there for a while, but… Yeah, apparently only last week they've addressed some comments.
So And just to make sure, Ben.
So, for you, it kind of likes… this looks like… a nice… addition. I mean.
**Ben Joseph** 08:29 Yeah.
**Cesar Munoz** 08:29 you.
**Ben Joseph** 08:30 I.
**Cesar Munoz** 08:30 I don't want to be in your way, I just want to get a review.
**Ben Joseph** 08:35 I… I… I feel like this… these are, you know, separate.
like, they are fragmented at this point, and I would definitely would very much like to see them come together.
apart from that, like, I don't have a strong opinion, so that's why I asked for, like.
You guys to take a look?
Also, this person doesn't seem to be attending the SIG, so I thought, like, yeah, might be good to… Just revisit it.
Yeah, I would say, like, yeah, I have interest in this, so… That's another thing.
**Cesar Munoz** 09:16 I see.
I'll take a look at this. Yeah, that's fair enough. Yeah.
**Hanson Ho** 09:20 well.
**Cesar Munoz** 09:21 Thank you.
**Hanson Ho** 09:22 Sorry.
**Jamie Lynch (Palo Alto Networks)** 09:28 Anything further to discuss from Alvin?
**Ben Joseph** 09:35 Sorry, what was that, Jamie?
**Jamie Lynch (Palo Alto Networks)** 09:37 I was just asking if anyone wanted to add any final thoughts onto that one. It sounds like we're… Jennifer.
**Hanson Ho** 09:46 I haven't seen it. It's the first time. I've only looked at Ben's stuff before. This one, I have not seen. Looking at the headline.
They… they are, related, but also unrelated, because we're talking about the legacy instrumentation, and where we want to take that, so… I'll comment when I have a look.
**Jamie Lynch (Palo Alto Networks)** 10:09 Cool. Hanson, you're up.
**Hanson Ho** 10:12 Yeah, so I wasn't there last week, but I want to talk about the federated client-side registry.
Repo's been created, I think we talked about that. I have some updates to make today to get the first scaffolding in, so that, the registry actually publishes, with, well, with no attributes at the moment. But soon there will be others.
Adding, browser, ones, and then eventually porting.
app session, all the other ones that are effectively client-side, only. We're gonna be deprecating the existing ones, and then consuming it, or rather, publishing new versions of it. Well, a new version publishing the same conventions.
At the same stability, eventually, over in this other registry. Which means that.
repos consuming, artifacts, or registries, that is defined in semantic conventions, like the main one, will have to be modified to get in the new versions of.
session.id, things like that.
So that part is, you know, relatively easy to change, just a consumption, just pulling in a different thing, maybe changing it to the V2 formats. But longer term.
which nothing we have to decide right now is how we want to deal with our registry. Right now, it's not defined as a V2 registry. It is not publishing a registry that folks can depend on with attribute groups and all that stuff.
So, it is… it is kind of like the old style. If we move into the new style, what do we want to do?
Folks in the browser world, the idea is to push all the common ones.
And all the platform-specific ones into, this client-side registry, where we have, quicker, kind of, loops to review.
And, publish, and all that stuff. So… we only want to do that for conventions that we want to preserve, and we have a bunch defined in our semantic convention that we may not want. So, one thing to do is to kind of catalog all this stuff, and then figure out whether we want to kind of keep it in our registry, but internal, and no one… not publishing it out, and whether to migrate some of them, and turn them into real semantic conventions. So I'll be creating issues, in this repo.
For these attributes. And then we can decide, as a group, how to handle, or the general rules of how to kind of migrate.
our consumption and production of semantic conventions into the new world. So this is more of a heads-up rather than a, hey, here are the things to look at. But so… Excuse me.
Watch out for that in the coming weeks.
**Cesar Munoz** 13:24 Sounds good. So, just to confirm, the, I guess, ideally.
this repo… We'll provide this, schema.
I don't know, URL, if you will, that we can use in our semantic convention module to fetch the ones that we need for Android, and then generate the Kotlin, okay, color of it.
**Hanson Ho** 13:51 Yeah, there's.
**Cesar Munoz** 13:52 it.
**Hanson Ho** 13:53 Go ahead.
**Cesar Munoz** 13:54 No, I would say that… For me, it sounds great.
And I… I really don't have… Like… A reason why to keep.
most of the stuff in the Android repo.
I mean, if anything, to be honest, I will… kind of expect the maintainers of this new repo to kind of be cautious of what they accept in there, because, as you said, when something gets in here, it's like.
Now we have to support it as a… Client convention.
So… I mean, if you have some ideas of what you would like to support.
From what we have right now in Hotel Andre, then… I think that could be a good starting point.
**Hanson Ho** 14:47 Yeah, I think I mentioned this before, like, that was the pre-pre-announcement, this is the pre-announcement. So right now, we are consuming the registry and generating our own source file, so that we could do stuff like, you know, create, event classes that actually bind to whatever CK we're using, version we're using to produce events.
So, if we choose to, we can still consume it that way. So registries are there to be consumed, as a set of conventions, that are versioned.
you know, OTEL, Savant's Conventions Java publishes artifacts that are source code in Java, that have attributes, constants defined. That's, like, the easy, frictionless way of consuming it, but we are more the advanced use case of taking the registry itself.
finding the attributes we need, and then generating a source code for it. The first move will not change that. We are just saying, hey, instead of pulling it from semantic conventions, 1.44. We're also pulling from, client side.
dev, maybe, 0.1 dev, or whatever it is, and then kind of building it that way. But the next step would be, well, we have all the stuff that we pull from local repos to generate, like, you know, what used to be hard-coded constants. Where do those go?
Do they stay where it is? Do we make them true semantic conventions?
so it has meaning for everyone? And if we do, do we have to change the names? If we change the names, we have to deprecate and move, and there's a procedure for how to do all that. And with a repo, that we're publishing.
the deprecation part is actually pretty easy. It'll, in a robotic way, say, hey, you know, what you point to was this, it's actually this other thing now, and you go to this registry with this schema and this version, you know, to consume it.
So, if we choose to do nothing.
we don't have to do anything, but I think there are things that we can do to kind of start making this a little bit more manageable, especially in terms of deprecation. Because right now, we have a bunch of things where it used to be called this, and then we're gonna call it this, and we'll use a Boolean to use legacy values, and then populate one, populate the other. Now, once we get on the train, there's gonna be a managed way of basically aging out And deprecating and moving to new attributes, when we so choose. So we have to take that first step, which is what the list of issues is going to be initially. Like, how do we get on the train? And then where the train goes from there is what we have to decide.
**Cesar Munoz** 17:30 Got it.
I mean, that sounds good to me. I was mostly kind of just referring to what that means for Hotel Andrew.
So, you know, now we're gonna probably migrate some of the stuff that's defined there over to the new repo, or maybe not, or maybe some.
And then just… Choose a new registry URL as one of our sources.
And I'm open to that, if that's kind of at least the initial… Idea. It's just that I don't have right now at the top of my head.
You know, which… Of the attributes that we have.
defined in Hotel Andre.
Are good candidates to move to this new repo.
And… and I'm… I'm really not… Too opinionated on that.
So if you have some ideas of some attributes that we define in Autel Android that You think will make sense for the client's new one.
that… I think that could be a nice way to start, probably.
See ya.
**Hanson Ho** 18:34 Yeah, yeah. That's what the list of issues will be, because there are going to be ones where I think Jason's extracted all the constants and put them into the registry.
**Cesar Munoz** 18:46 Thanks, Haya.
**Hanson Ho** 18:47 But… whether we want to put it directly into the new one by creating new ones, so the deprecation step skips, like, one step, if we haven't done that, or we go, every single step. We'll decide, I think, as with each set of, of, of.
well, I guess the… with the attributes from each set of instrumentation. I think that's a good block, to kind of divide the stuff into.
So hopefully.
**Cesar Munoz** 19:17 Yeah, I mean, for the ones that… that will change something, like the name, or… So yeah, that will complicate things a bit, probably.
know I was gonna say I know that Jason I I think he has some experience with that in the Java world.
maybe we can do something similar, but I… yeah.
I'm up for, Suggestions on that side, yeah.
**Hanson Ho** 19:48 I think some of them have been, like, the Jank stuff, for instance, have been moved to the actual semantic conventions. Are actually semantic conventions now. Those will be, moved outside the scope of this project. Those are considered kind of, like, moved.
It's the ones that are, like, not officially part of the semantic conventions. Those are the… with… and some of them have, like, correct names with correct namespaces, it's just not, like, defined. And some of them are… don't have the right namespace.
Those are the ones that are like, do we skip the step of making it?
the correct namespace, but still hard-coding and not publishing? Or do we… and then having this attribute of, like, legacy versus new? Or do we just, like, skip that step and just first define it in the semantic convention first, so that, you know, we make one jump instead of, like, two jumps. Like, the location will exist once rather than, like, a deprecated thing. It never existed to it existing, so…
**Ben Joseph** 20:49 So, what… So I'm just curious, like, what would be the difference once we… is it going to be transparent to the project? Like, if we move something from the Android to the client-side, project?
how will that reflect? Is there going to be a change in a pack? Like, I know we are still generating the source for this, so would there be any difference, say, a change of package name or anything, or just a dependency where we import it from, or is that all that needs to change?
**Hanson Ho** 21:21 So, there should be no change if the… if the string itself is the same. If we are currently publishing, you know, app.foo, and the new string convention is going to be app.foo.
And we are publishing it right now as that, then… We will just have a more, stricter guarantee that When we release with the semantic convention version, get going forward.
That will be, you know.
that will be codified. Right now, if we put in a constant, there is no support level. We're not saying, you know.
I guess by Semver, you know, there are things that we guarantee in terms of, like, what's changed and what's not changed. But there's no provenance of tracing that attribute back. It's like, when was that attribute declared? Oh, it was declared, you know, in Android version.
you know, 2.1, or whatever it is. But now, the provenance can be traced… when we actually move it to the federated semantic convention, the provenance can be traded, traced back to, like, you know, some semantic convention registry outside of our repo.
If we declare something that is, like, android.termination, or something like that, I don't think that exists, and we decide that the semantic invention, that the Android namespace is not something we should use, we should use app.android, or whatever it is, then we're gonna have to manage A new version will be published with that.
Semantic conventions, and the old one is, is just… not either… we either do the trick of legacy versus new, new being Spanish convention, legacy being whatever we publish.
Or, like, the third option, which is, you know, not great, is having, like.
legacy, new instrumentation, and then, like, in the future sometime, we'll have, like, you know, it's based on semantic invention.
But that's almost like, you know.
Understanding what it represents, the string itself is going to be unchanging, unchanged if we decide not to change it.
So it's not a build brick, but a semantic.
break, if you will.
**Cesar Munoz** 23:46 Right, it's like, the end user… But my understanding is that the end user won't get affected.
As long as we keep the same names. And I guess that's the tricky part that Hanson was mentioning earlier, what happens when there are new names?
For example, I know that In Hotel Andre, we were defining an attribute name, I think it was last.screen.name, or something like that.
And that's definitely going to change if we make it a Unofficial attribute.
So… that's when I get… that's where I guess… Hanson is still probably working on what to do in those cases. I know, I think… The… my understanding is that the official or like the central repo for semantic conventions. So they allow to… they allow you to define a… Stability level.
to each attribute. I'm guessing we can probably do the same here, and maybe… We are allowed to introduce breaking changes if a non-stable attribute name.
changes later?
So maybe that could be a way, but… but it's probably… you know, gonna cause some issues, but I guess users should know that they… they created queries around those Incubating attributes, they're, you know, they're up for some changes.
Maybe that could be a way, but I don't know, maybe you guys… Have some… some ideas.
**Hanson Ho** 25:28 Yeah, that one is the… that one's actually probably the more straightforward case, because, you know, if the names change, it's very obvious that things are there or not there, and it's broken. I think for that case, we can leverage the dev versus stable. In fact, each registry will be publishing a dev and a stable registry, so client-side is like the repo, but there's an individual dev registry and a stable registry.
Stable registries only contain stable elements, and then dev registries contain everything.
In theory, Dev is not stable, so it can be liable to changing for version.
But one thing we've done in this project is say.
Even though, like, last dot activity or whatever.
somebody is using it, so I think what we're saying is, even because we didn't declare level stability, we are being more careful about managing change. So I know it's almost like… our level of implicit stability is stronger than what Dev guarantees, in terms of semantic conventions. When we move on to semantic conventions.
we can choose to be a bit less strenuous in terms of, what we change, what it means. That is a decision that we have to make.
that is not a mechanical, you know, this is basically saying, hey, what are we gonna do when we break something? The more subtle one is, if the key… it's almost like… The meaning of the attribute?
is as important as the key name. If… the value changes in terms of, like, or in a backwards-breaking way. If it used to be a string, that could fit any value, with the same key, like app.foo.
But in the semantic conventions, after discussing, we decided it's not going to be a high cardinality string of anything. It's going to be an enum of these five values.
The meaning of that is different.
So… The thing will exist as an attribute, that is a string.
But what it means will now be fully defined elsewhere. It's… it's what do we do with that? It's like… it's like those… those are the… those are the stupid cases that we're going to be talking about for… for potentially a while. And it's… which is why I want to kind of, like, do it, you know, instrumentation by instrumentation. There's going to be, like.
a flow chart of, like, you know, here are the six paths something could go.
So…
**Cesar Munoz** 28:07 I see. And you think this is… Based on how you mentioned it, it sounds like the… the biggest issue At least… from what you said, that I understand is that would be the attributes that exists right now in Auto Landry, because We kind of publish them without any… Stability level.
So… if I understand correctly, in the future, when we start defining new attributes or new Conventions, and we defined them with a deaf stability level.
then it would be easier in those cases. But the ones that we have right now in the instrumentations and everywhere else in AutoLandry are the… Okay, so, so… I was thinking that it really would be nice, but, well, we'll have a lot of time to discuss this.
If we could… Kind of like… synchronize the… Like, the creation of… or the migration of these attributes.
Over to this new, client semantic convention repo.
with the, Kotlin.
SDK migration.
And that way, maybe we can just kind of start from scratch on a 2.0 version.
where we… I mean, definitely users will have to see that as a flag that things will… will… will break.
And… and then we can start.
Over, kind of, like, with these new attributes and stuff that will have the proper stability level and things like that. So maybe it would be nice, one way, I guess, to address it. If it's just this one-time, one-off problem.
**Hanson Ho** 30:07 Yeah, that's a… that's a… that's an interesting… thing I hadn't really thought about, which is we declare everything brand new in 2.0, everything is Kotlin, everything is bounded to semantic conventions, either dev or stable.
if you want to depend on 1X, it'll kind of exist in perpetuity for stability, you know, bug fixes. But we're not going to change the, the legacy.
names, and then in the new one, that's where we're gonna put all the new stuff in. It's a pretty big… it's a pretty big change. So, this is definitely.
it may even be bigger than the API change, because API change, at least, is… you can compile and see what breaks. This is… this is like, yeah, the attributes all will be defined in a certain place, and they may or may not be what you expect before, but they are all documented.
And then we could basically say, this instrumentation supports this version of the semantic conventions, for client-side and, core.
That would be really nice, but it'll be a really big change. So, something definitely to discuss.
**Cesar Munoz** 31:20 Yeah.
Cool.
**Hanson Ho** 31:27 More to come.
**Jamie Lynch (Palo Alto Networks)** 31:28 Anything else folks want to discuss?
I think we can probably leave it there and get some time back. Oh, go on.
**Ben Joseph** 31:41 Just a question on that, whatever we are discussing. So if we want to add a new convention or a new attribute today.
What is the recommended path? Do we go ahead and add it within the Android repo, or should we place a PR for the client-side repo?
**Hanson Ho** 32:06 I would pick a name… well, don't… so… Ideally, it would be to the client-side repo, but I would say it'll be probably a day or two before we're ready to merge new conventions.
So if… but until Hotel Andre releases, it doesn't really matter, it doesn't exist yet. So, you know, right now, don't block on anything if you have an attribute rating in the… OTEL Android registry, just check that in. You're adding one on top of A whole bunch, and we'll migrate. Do your best.
**Ben Joseph** 32:39 No, that…
**Hanson Ho** 32:40 you.
**Ben Joseph** 32:41 Yeah, my question is more like in the near future, like once this is in place, like before we do 2.0, what in that time, what would be the recommendation? So it's obviously the client-side repo, I guess.
**Hanson Ho** 32:57 Yes, in that time, create, proposals for updating semantic conventions on the client-side registry. We can get that merged a lot quicker. It doesn't… there's just, you know.
you could… you know who to bug, if, if, if, you know, it doesn't get merged in time. Get that merged before you start, or before… yeah, get that merged, and then.
we'll release probably, you know, in a high cadence, and then we can change the dependency to the version that we need, bump that, update the generated code, then you can depend on it. In the meantime, you know.
put it anywhere, as long as before it's released, it doesn't really matter where the constant comes from, what it means, because no one's using it yet. It's when we release, that's when you know, that version has that, then the Providence ought to be tagged, which we can't right now, so…
**Cesar Munoz** 33:57 I have an estimate, a rough estimate of one.
When will be the first release?
The first registry from this new repo.
**Hanson Ho** 34:06 Could be today, I have a PR out for a while. I'm adding two right now.

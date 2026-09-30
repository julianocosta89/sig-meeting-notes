SIG: Client SIG
Date: 2026-09-29
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Hanson Ho** 01:43 Hey, hey, hey!
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:47 Hanson How's it going?
**João Oliveira** 01:51 Not bad.
**Hanson Ho** 01:52 you Hey, Joe.
And under the weather, and… Crazy weekend, so I was gonna get some stuff done, didn't get stuff done, but… You know how it is.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 02:09 I know how it is, yeah.
**Hanson Ho** 02:13 Let me project, or keep… I always say project, and I feel like younger people don't know what I'm talking about.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 02:22 Rejector.
**Hanson Ho** 02:23 Yeah.
Yes. I share my, my, my slides.
In my projector. Whoa.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 02:35 Hi, Ted.
**Hanson Ho** 02:36 Hey.
**Ted Young (Raintank, Inc. – Grafana Labs)** 02:38 What's up, y'all?
**Hanson Ho** 02:43 Alright.
Y'all can see this? I'm terrible at taking notes, but I'll try, unless someone is… Better at it. Feel free to… feel free to… Take notes.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 03:01 Mmm.
**Hanson Ho** 03:17 Well, this is gonna be confusing in a few weeks when, daylight saving times is over for most of you.
I'm… oh, we're… I'm in Vancouver, and our province isn't doing Daylight Savings Time, so we're gonna be, or rather, we're not going back to, non-Daylight Savings Time, so we're gonna be one hour offset. I don't… Yeah, so I think things are gonna stay the same for you all, but I will have to… Adjust. That'll be fun. The first week will be fun.
**Jason Plumb** 03:49 Was BC actually doing it?
**Hanson Ho** 03:51 Yeah, we're doing it.
**Jason Plumb** 03:52 Oh, that's so awesome, because it's gonna come down the West Coast. It's gonna happen. I'm feeling good about it.
**Hanson Ho** 03:58 I hope so. I hope so. Yeah. First, Washington or Oregon, and then California, and then, you know, and we're good.
**Jason Plumb** 04:07 I think we passed it and we're contingent on California or some nonsense.
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:10 It's like an all or nothing thing.
**Jason Plumb** 04:12 Yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:15 But… Yeah, whenever this starts to happen, then we discover which OTEL meetings were scheduled In which time zone?
So there might be, and we did just redo a lot of the meetings, so there might be a little chaos. We'll see what happens.
**Hanson Ho** 04:36 I don't think… Well, actually, not only.
I think it'll be okay for you guys, for you folks, because, nobody's… few people are doing it from, from… I think we're getting a new time zone designation, like PCT or something like that.
So… It's… it's back to P… ST?
Then it should be okay.
**Ted Young (Raintank, Inc. – Grafana Labs)** 05:01 But also, like, Europe does their time zone switches slightly offset from when… North America does theirs, so there's always a little bit of chaos.
**Hanson Ho** 05:13 British summertime, and I don't know if there's another one for Europe.
All right.
Wait 5 minutes, I think we're good to go. So feel free to put more topics on the agenda. Some of these I'm hoping we can go through pretty quickly.
So the first one will be quick. There's the PR, please review for infra setup validation. No actual conventions are there, so, there is a publication workflow, it has been tested, but there are no conventions, so if you click on it, it does nothing, or it publishes a version that does nothing. Has nothing.
So, please review so we can… Get more stuff in there.
Alright, Morton?
I just put a topic for you for… to talk about the, source code generation, so…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 06:09 Yeah, yeah, so this, this was… to be perfectly clear, this wasn't my idea, but it was discussed in Slack, whether or not we should have This repo should be generated some, like, language-specific artifacts, and actually publishing them to .
Well, to, registries, like NPM or Maven. I created an issue for this, it's the issue number 13.
Did just… I did a little bit of, like, research on that.
Let's see, let me open up this issue.
Basically, my recommendation would be, like, to… to not do this immediately, unless somebody asks for it. I feel like it may be, adding, like, additional Maintenance burden on us.
And… since nobody's asking for it at this point, I don't think we necessarily need it. I think it would be sufficient to just include, the.
The artifacts, that are recommended in the.
in the the V. 2 of semantic conventions.
Which would be, like, the, the YAML files of the… the resolved attributes.
And just attach it to the releases. Okay.
And, you know, our… repos, like the… for the SDKs, like the browser and Android SDKs, they can still generate.
You know, we can still generate our… Our constants from from this repo without having having something published from here.
What do you all think?
**Hanson Ho** 08:02 So, my main concern, is just reducing the friction of using these.
I think a lot of, the initial, when we have nothing, it's fine. But when we start migrating existing workspace, existing conventions, from existing… that have already been published.
Folks that want to use it have been using it, through… Java through JS, through whatever, you know, they had, will need artifacts unless they want to go and set up WeWeaver themselves, which is… which is fine, which is easy. But I think, it would just be, like.
one little less point of friction. It's like, oh, I gotta set up Weaver in order to consume this, so why don't I just hard-code it, you know, and I'll just change it. And I figured.
the publication part of it, will need, you know, some maintenance work, so you're definitely right there. But if we set it up in a different repo, if we set it up, you know.
anywhere, someone's gonna have to maintain it, and I think because we are likely gonna only need a handful of languages initially, doing it here might just be, like, the easy thing.
And I know, like, Oto Android, for instance, already kind of consumes and generates stuff, in a bespoke way, so, you know, that project doesn't need it. But if there are other projects that are consuming existing, conventions, like, then they would have to either set it up, or do something, and this… those just make migration, I think, easier and a little bit less friction, so… Maybe we don't do it for every language that we think of right now, but only do it for the ones that, where we know there will be existing consumers when we migrate.
And kind of, you know, add as we need to.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 10:04 So I can speak for, like, JS, real quick. Like, there is, like, one consideration for JS, which is… The JS SDK does… publish its own semantic conventions package.
And… they came to a decision at some point. So they have, like, stable conventions, and they have incubating conventions. Incubating conventions are exported from a different path.
And they actually… recommend that… People don't consume those, because they can… they can change in… in minor versions, so they're… they can break all the time.
So, like, when… when package JSON, like, pins the… the version of the… well, you don't want to pin… you don't want to pin, like, the actual… the exact version of the… of the package, so… If you… if you do, like, a carrot… install, then you could be getting breaking changes for the incubating semantic conventions. And here, like, we're gonna have most of our conventions are gonna be experimental.
Pretty much to begin with, so… for like Js, it would.
I think we would want to, Follow the recommendation of, not importing from that package, and just, like.
Hardly on copying.
copying or hard coding those experimental conventions instead.
**Hanson Ho** 11:33 I think the good thing with V2 is that we can define effectively from the same registry a dev stream and a kind of stable stream.
and version them differently, both in the registry, so the actual schema URL will have, like, dash dev, which can include, like, all the experimental ones, and then, like, without dash dev, it will be, like, the stable ones. And basically create analogous artifacts.
for publication, if we choose to. So, I think with V2, there's a bit more flexibility in terms of, like, what gets generated. You will know what you're depending on. So you're not just depending on, you know, the… client-side, registry, depending on the dev version, or a dev flavor, a specific version, and the stable, you know, flavor of a specific version. So hopefully.
The version thing will be a bit less confusing, especially if we version along with the version number in this repo, because… If we, say, have a different, like, versioning number, and, you know, it brings in, say, you know, the core changes as well as the, local changes, then that's, like, a different versioning. So hopefully we can avoid that mess just by having the same version numbers go forward here.
I think by default right now, we are effectively doing the no-generation thing, so this is just the additive. I think even in the README and things like that, it says, we're not generating any artifacts. This is like, you know, if we did this, it would be like, you know, changing that, so… So we definitely don't need to do it now, but like, you know, in the medium term maybe. Ted?
**Ted Young (Raintank, Inc. – Grafana Labs)** 13:14 I was just gonna note that I think in Python and the Gen AI SIG in particular, they're doing a lot of really aggressive work at trying to use Weaver.
To help maintain instrumentation around semantic conventions, because they've got this issue, right, where the semantic conventions for Gen AI are changing very rapidly.
And they're also trying to, like, write and maintain quite a bit of instrumentation. And of course, they're all the AI nerds over there.
And Weaver's a deterministic tool, but it… in theory, pairs well with AI, you know, coding practices, if you use it right. And I know that Ludmilla and Trask are pretty heavily involved in that SIG.
So it might be worthwhile to check in on what they're up to, and that's probably where But we can probably get the best feedback right now for what's… You know, what's a good way to set this up, and what's helpful or not, because they're kind of going through the same… Same problem, basically.
The only caveat I would say is, like, we might not have as big a problem on the client side as other languages, and that Often what their problem is, is they're having to replicate the same instrumentation in many packages, and it seems to me that on the client side, that's not so true.
Or at least, like, the instrumentation we're trying to write now is, like, more like the core stuff, that it's not, like, trying to maintain 30 HTTP client implementations like they're doing in Java.
**Hanson Ho** 15:02 Yeah, also, like, the fact that we don't have to have an indefinite expanding language of… list of languages means it's actually a tractable problem. Like, I wouldn't want to have, like, 30 different artifacts that we publish every time. That would be… Yeah. Not great. But, like, if we do, you know, 4 or 5?
Eventually, that will cover, I think, the vast majority.
**Ted Young (Raintank, Inc. – Grafana Labs)** 15:25 But at any rate, that's just pointing out, like, we might not normally think of the Gen AI SIG as something associated with, like.
how to do semantic conventions and lay it out, but they're doing a lot of this right now for the first time, so it might be worth asking them what they're up to.
**Hanson Ho** 15:45 Cool. I can do that.
Let's see what they think.
**Ted Young (Raintank, Inc. – Grafana Labs)** 15:55 And Trask and Ludmilla would know, so it's also, it'd be easy just to go to them and be like, what's going on?
in Python that we could borrow from over here on the client side.
**Hanson Ho** 16:06 Cool.
Alright, we'll take a look at that and see how we proceed.
A couple other things that we kind of briefly touched on last time, but, one I want to talk about.
bit more formally. So for approving, changes to the repo, we discussed in Slack, again, something we… or Gen AI, you know, points to a decent kind of methodology, which is Want approval for editorial… For editorial-only changes, so, like, changing like, descriptions and things like that that don't materially impact, like, the conventions themselves, existing conventions. And then two approvals from folks from different organizations for new and breaking changes. So, if we add a new convention, that might be a little bit, you know, a little different. We don't want, like, you know, one org to be able to, like, ramp things in, which is, I think, totally reasonable.
Any any thoughts about that?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 17:11 Sounds good to me.
**Hanson Ho** 17:14 Cool.
I'm not gonna say, silence is… And okay, implicitly, but I also need explicit objections.
To stop this.
Okay.
So assuming tooling and documentation changes are same as above. So if we decide to, like, publish, or, you know.
you know, do… comments for workflows to not break or not get flagged by, you know, code reviews, that's one approval. But if we're, like, adding a whole new process to, like, I don't know.
validate everything using fancy stuff. I don't know, I'm making stuff up now.
Two approvals.
And then for one additional thing I'm proposing is, like, things like, do we publish artifacts for versions? We should talk about this, in a SIG rather than just, you know, doing it, looks good to me, you know, and shove that in. So that's, like, an extra layer of, of.
of carefulness. I'm okay if… Let's talk about that, if that seems too arduous, but I think… when we're setting stuff up, I'd rather be a little bit more, a little more… forcing us to talk about it before. So…
**Jason Plumb** 18:44 I would say that's fine, just don't discount the maintainer agency. Like, you know, as maintainers, you have agency over the project, so… I mean, I appreciate you wanting to be thorough and to gather opinions, but it's also in your… In your careful hands.
**Hanson Ho** 19:01 It's too easy just to get the maintainers to be like, it's good, push it, this is… Checks and balances, right?
**Jason Plumb** 19:08 Yep.
**Hanson Ho** 19:10 Last thing, unless folks have additional things to add, the migration of existing namespaces. So I see Martin has one that, is about browser. It… Are any of those in any existing, well, I guess, are any of those in the, in the existing core registry, or are those, like, new-new?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 19:32 So I opened this draft Pr this morning, which has anything that's in that Pr is brand new. It's it's not in the core registry. The core registry does have some browser attributes.
And events, I think one event. Which needs to be… which will need to be migrated, but I think we would do it separately.
**Hanson Ho** 19:54 Okay.
So, for all intents and purposes, we could assume this… we can just treat this as a new one, because no one else is… Correct. Okay, okay.
Cool, so let's… let's see how that goes. There should… there should be enough, there should be enough… well, I mean, once the PR is merged, we're able to, like, start doing releases, like, dev releases, and, we can… we can… try that out and see what it's like. The bigger one is the session namespace, and the app namespace, and the whatever other namespaces that folks… Are any of those stable, or are they all under dev?
Currently.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 20:38 So Sessions is definitely not stable.
app, I'm not actually sure, so…
**Hanson Ho** 20:47 So, we should come up with a process for, like, what do we have to do to actually move that stuff. I mean, first, you know, deprecating.
And then, like, putting it hours, and then making sure if there are consumers that, you know, they're well warned well in advance, et cetera, et cetera.
Martin, I think you were… you were going to look at which namespaces are good candidates last time. Did you have a chance to do that?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 21:15 Yeah, So, I mean, the app and session, for sure. Hold on, just give me a sec.
I think I shared, like, there's a… There's a list of.
under code owners. There's in in the semantic conventions, core semantic conventions like shows.
Which, which, like, client-side approvers own which, Which… Namespaces?
So, I think I would… That's a good start.
There are not many of them.
There is… Like, end user, there's app, device, mobile… So yeah, I think we probably will need to go… One by one, and see if, like, each of those makes sense, like, to port over.
**Hanson Ho** 22:21 Yeah, some of them we might be… might be a good chance to, like, completely get rid of, or, like, deprecate, but not revive, especially if… if they are either confusing or whatever. But… that might be a second change. Like, first get the stuff that we actually do want to keep, and then the ones for that we don't, we… we… Think about how we do that.
Cool.
I can take a look at this… oh, unless some… does somebody want to take a look at this and create issues about migration, at least?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:56 Yeah, I can… I can create issues for each of those namespaces, and we can… so we can have a discussion about those individually.
**Hanson Ho** 23:25 Raw.
Yeah, and then once we have that list, we can start talking about, prerequisites and process, because some will probably need a bit more, warning and or artifacts, and others may just be… no one's really using this right now, are? So, you know.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 23:48 Yeah.
**Hanson Ho** 23:50 Cool.
All right, any other topics for semantic conventions or otherwise?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 24:01 The only other topic that I can think of, I also created an issue… Yesterday, for… Let's see which issue is that.
Yeah, it's issue… Number 11… Hold on.
It's basically like we had last week, we were discussing… Whether or not.
like, platform-specific conventions should live here, and I think we made a decision that, yes, they should. I just wanted to document it, so… Okay.
**Hanson Ho** 24:43 you.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 24:43 Issue 11.
**Hanson Ho** 24:45 This one. Are you guys seeing this? Am I sharing a tab?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 24:49 Yeah, we can see this.
**Hanson Ho** 24:50 Okay, cool.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 24:52 Alright. Yeah. So this is the issue about it. And I opened a Pr.
That updates the readme.
To note this, to… to update the scope of this.
I think eventually we'd probably want to put it in contributing.
Contributing, Doc, But, yeah, Just FYI, and I think if nobody has objections, we can… and you agree.
Hanson and Jared, then you can merge this.
**Hanson Ho** 25:35 I'll take a look at this after.
All right.
Anything else to discuss about this stuff or otherwise?
Cool. Check Slack. I got a bunch of stuff additional for this, once this first thing is merged, hopefully. I don't wanna, like… I'm already adding commits to it, and I don't… I don't like it, but, you know, it is what it is.
Cool. Have a good, Tuesday night, or afternoon, or morning.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 26:18 Thanks Hanson. See you. Thanks.
**Jason Plumb** 26:20 Hanson, everyone. Bye.
**Ted Young (Raintank, Inc. – Grafana Labs)** 26:22 the.

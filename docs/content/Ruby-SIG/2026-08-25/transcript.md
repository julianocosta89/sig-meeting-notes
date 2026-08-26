SIG: Ruby SIG
Date: 2026-08-25
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Kayla Reopelle (New Relic, Inc.)** 00:19 Hello!
**Matthew Wear** 00:58 Whoa.
**Kayla Reopelle (New Relic, Inc.)** 01:01 Hello!
Alright… Don't know if Hannah's joining us today… So I think we're good to get started. I can share my screen.
Oops.
Okay, hey, we do have a Hannah. Hi, Hannah.
**Hannah** 01:31 Hey, guys.
**Kayla Reopelle (New Relic, Inc.)** 01:34 So… let's see… Spec SIG today… I feel like this might have some relevance to us, just since we're working on declarative configuration. I started reviewing the spec this morning, and I have some questions, but since I don't… fully understand it yet. Matt, I'm wondering if you could talk about this one, and whether you think it has, context to our current PR.
**Matthew Wear** 02:05 No context for the current PR, this is… I'm not sure why they use this example exactly, Whoa.
Possibly it could. My… my reading of it was that, there's… There is something called instrumentation slash development, which is, like, a separate place in the declarative config that is not JSON schema, exactly.
And… that's ultimately going to break, I guess, you know, when it becomes, when it becomes stable, when they remove development from that… from that field, because it needs to be part of your YAML.
But… Yeah, as I'm looking at this, I don't… I'm not familiar with this exporter Prometheus slash development, unless that's also a development part of the spec.
But… Oh.
In any case, I don't think this, like, blocks any of the work that we're currently doing. I think we, you know, move forward with what we have, and then… When… whenever this is decided, then we'll kind of adapt what we have to support it, but I think, Yeah.
**Kayla Reopelle (New Relic, Inc.)** 03:52 Nice, sounds good. Yeah, yeah, that's helpful. So, just… It doesn't seem like we need to change anything right now, or consider this for handling the configs and development.
Cool.
Don't know, can you guys hear those, like, beeps?
Or, like, chimes from my computer.
**Matthew Wear** 04:19 I'm not hearing any beeps.
**Kayla Reopelle (New Relic, Inc.)** 04:20 Okay, great.
Let's see… is this more… we already have that rolled out, as a follow-up.
from last week's meeting, we were talking about whether we needed CodeQL if we had Zizmore installed. I got a response, and it sounds like Zizmor is only for CI, and CodeQL covers everything else, so we do want to have both of them running.
So I made the admin changes required to enable CodeQL as a… or to, I guess, require CodeQL to pass, but it doesn't seem like it's enough yet, so I'm gonna keep working with Thompson Tomo on that for, the contrib repository, and… If we like it there, then we can move it to the core repository, too.
Yeah, I'm not sure… If any of these are really important for our group right now, because we already have… propagators… Kind of set up.
And… We discussed the service name last week, And since you already have kind of an implementation for that, Matt.
I don't think we need to take any action until… This gets a little more settled.
Is there anything that you wanted to cover?
In this meeting today from the Spec SIG.
**Matthew Wear** 06:00 I think that's it.
**Kayla Reopelle (New Relic, Inc.)** 06:02 Okay. Great.
Okay, so I haven't put my reviews on the declarative configuration PR yet, I just have more general questions right now from playing around with the example.
I think that this has kind of decided to be maybe in phases or not everything at once, so I didn't want to add a bunch of comments until I understood the intention more.
My main… question. I guess I'll pull up the… PR first… Kind of around, like, how the setup is supposed to work, and what the expectation is.
like, going forward. So it seems like when I was playing around with the example application.
These lines were really crucial.
for it to work, like, if I took them out and just set the environment variable The, configuration wouldn't be applied.
I was kind of under the impression from the documentation that I was reading that, there shouldn't need to be any code changes for declarative config. Is that… accurate? Is that part of the plan? Am I misunderstanding things? Where are we at in terms of, kind of requiring people to add code to use declarative configuration?
If anyone is talking, everyone is muted.
**Matthew Wear** 07:57 That's a good question, actually.
I think… This needs to exist somewhere.
And…
**Kayla Reopelle (New Relic, Inc.)** 08:13 Go ahead.
**Matthew Wear** 08:14 Yeah, I'm not sure if you're supposed to just, you know.
do, like, a Ruby-R that basically has that… snip it in it, or if we are supposed to, go one step further, and, I guess as soon as the SDK is required, see if there is a config, and then do this.
Dumb.
Trying to figure this out a little more.
concretely, I feel like… I think the reason why this is, like, a hard answer, or a hard question to answer is that I think… I'm not sure that anybody has this completely finished, or maybe… Maybe this is as far as most of the SIGs actually are on it?
You have this minimal, Minimal stanza.
**Kayla Reopelle (New Relic, Inc.)** 09:23 Yeah, that would make sense. I mean, I think it could have… A place in, our configurator for the SDK, but I don't know if the config… like, tooling is supposed to be SDK agnostic, I guess since we're requiring the SDK.
It wouldn't be, but that's a slightly different question that I have.
The example… just looking at these docs that were for users, it does seem like Java's implementation at least behaves this way.
But… It really seemed like you just needed to have the file and set the environment variable, and then… Everything else, should just be handled by the SIG… the SDKs.
So, I'm fine doing it in phases, if that's something we want to think about as a phase two.
Xuan, I see you're unmuted as well. Did you have anything you wanted to add?
**Xuan Cao** 10:33 They're in different phases.
**Kayla Reopelle (New Relic, Inc.)** 10:38 Okay, added in a different phase.
**Matthew Wear** 10:43 Yeah, I think that makes sense, and we can kind of… try to figure out what this exact behavior is, but that's what Java is doing that I'm guessing that's what is probably expected.
**Kayla Reopelle (New Relic, Inc.)** 11:02 Okay, and then the other… question, I think, just for synchronous discussion, the rest of it I can… put on the PR, was this behavior… here, with environment variables. Unfortunately, I landed on this, or I don't know.
for whatever reason, I landed on this first before the specification, so this is kind of what I was using to analyze it.
But I tried doing this environment variable… or not environment variable substitution. I was looking at this bullet point right here, where all environment variables are ignored unless you explicitly add them to the config file.
I was able to set hotel resource attributes, and… Leave the config as it was, and it overwrote the attributes list that was here.
I know environment variables, you know, are kind of… the, like, top level of things usually in Ruby. Is this… A feature that we're planning to add later as well, or is there, like, a reason why environment variables are overwriting the config file?
**Matthew Wear** 12:20 Environment variables are, like, a complete can of worms for us currently. So, the… It's basically the next phase, but we need to… we basically need to strip all these from, like, our code everywhere.
Then you would just kind of interpolate them into the… config, and then the config would kind of pass them down. It's… I think that's gonna be an undertaking to, To actually get working.
**Kayla Reopelle (New Relic, Inc.)** 12:55 Yeah, yeah, that makes sense.
Okay, nice. Yeah, those were… oh, and I guess as the third thing that's maybe easier to talk about synchronously.
I noticed that the structure of the library is different from kind of how the spec is structured for config. Like, there isn't necessarily a… configuration provider, or, the other sort of class? Was that, like, an intentional… design choice?
**Matthew Wear** 13:34 So… Config provider, my understanding is that this is for the,
**Kayla Reopelle (New Relic, Inc.)** 13:41 I see. I missed that it was in development. Sorry, go ahead.
**Matthew Wear** 13:46 I thought this is for the instrumentation part of the, of the… Of the config file, there's something called Instrumentation Development.
And… The config provider, it's kind of like this top-level thing that lives above, like, tracer provider, meter provider.
Okay. And it, it allows you… This is where your instrumentation can, Whole properties from the declarative config.
So, we haven't… This is only Tracer providers, so there's no support for instrumentation configuration in this PR yet.
**Kayla Reopelle (New Relic, Inc.)** 14:36 Okay.
I did see those instrumentation classes, though, so is that doing something else?
Or I guess they're just instrumentation… it's an instrumentation file.
**Matthew Wear** 15:12 Is this just installing instrumentation, not necessarily… Oh.
**Kayla Reopelle (New Relic, Inc.)** 15:18 Oh, I see. Okay.
So it's installing it, and then after it's installed, building the map with the configuration?
**Matthew Wear** 15:31 I don't know, maybe Xuan can, clarify.
**Xuan Cao** 15:38 Oh, yeah, that's, that's… that's… Yeah, that's the JSK Exclusive file.
For the, for the, let me find this closer, simple.
You don't have the ammo?
So those config YAML, they have a field that I… expectations.
So, I was thinking those, those, per user, too.
If I work on the instrument.
Yeah, but basically, that's the idea, to build those… to build the instrumentation maps.
**Matthew Wear** 16:20 you're kind of breaking up there, so… I didn't hear everything, but is this, Is this reading the instrumentation development node of the YAML, and trying to build a map out of that, or… It just… Something else.
**Xuan Cao** 16:39 Yeah, this is… it's trying to read those, information nodes.
inside YAML.
To build the map.
**Matthew Wear** 16:48 Alright, so maybe… so that's where Config Provider technically does come in, and maybe… maybe it would make sense to remove instrumentation from this PR for now, because I think that's, That's another phase that we can work on.
Separately.
**Kayla Reopelle (New Relic, Inc.)** 17:23 How does that sound to you, Xuan?
**Xuan Cao** 17:35 Yeah, yeah, I can't echo list.
**Matthew Wear** 17:39 Just because there is… there's technically spec for how this is supposed to work, And it does introduce this config provider, which, I don't know. I… I personally don't like, because I think you can implement this without a config provider, like, it just… introduces this… New global that you need, that your instrumentation can't really work without.
And, like, the way that Ruby is set up, you can always… you can pass the configuration in as you're trying to do, Xuan, and I feel like Whenever you can… Pass things into a, To a piece of code that's preferable to just having some global, that you… depend on.
**Kayla Reopelle (New Relic, Inc.)** 18:32 Is this part of the spec that we should, like, comment on, since it's still in development?
And… suggest something else.
**Xuan Cao** 18:42 So those are the links I post, based on the chat, this is where I think, where I have the idea to have…
**Kayla Reopelle (New Relic, Inc.)** 18:54 Okay.
**Xuan Cao** 18:55 I don't know, I'm not sure if this, like.
I'm not sure if my understanding is…
**Kayla Reopelle (New Relic, Inc.)** 19:04 Yeah, interesting.
**Xuan Cao** 19:08 Maybe this is, like, more general.
for example, the HTTP should have, for RubyKids should apply to all the HTTP, clients, not just HTTP.
**Matthew Wear** 19:24 Yeah, so this is this development instrumentation node where… General is technically a section that should… That's kind of for shared, shared configuration that could be used between multiple instrumentation.
So,
**Xuan Cao** 19:44 Yeah, but if you look down, there's, like, configure languages, intermission libraries.
**Matthew Wear** 19:50 Yeah, then you'll get the movie tag.
**Xuan Cao** 19:53 Yeah, I'm not sure what… they don't have any examples for this, but, I was assuming that's, Wait, that's where we, user can… I would…
**Matthew Wear** 20:09 Yeah, so this is where the user can configure their instrumentation. It's just kind of like the spec There is this development spec, anyways, for this part of the, of the YAML that says that, It should be wrapped in a config provider.
And then your instrumentation should use this config provider, and it should expose It can fake properties.
Where you can read the… the properties for these.
**Kayla Reopelle (New Relic, Inc.)** 20:55 And so I think right now.
what you have is, if I'm understanding it correctly, kind of extracting all of the configs that instrumentation define, and making them available as keys?
In this section of the config?
**Xuan Cao** 21:18 I need to look again to see what it does.
**Kayla Reopelle (New Relic, Inc.)** 21:21 Okay, yeah, no problem.
**Matthew Wear** 21:24 And, yeah, for… For what it's worth, like… I'm working on the JS version of this thing, and… And I kind of did it the same way, where I did not have a config provider, and I was just kind of passing things into the instrumentation, and then… They told me, this is wrong, you need a config provider, But you really didn't need a config provider, but rather than, make things difficult. Bye.
I went that route.
And then… I don't know, if you want to look at files changed, and check out the HTTP instrumentation, you can kind of see… Boom.
Well, yeah, I guess I have wrapped the, the… The actual config provider nonsense.
below this apply declarative config method, so I think that's on the instrumentation.
Object.
**Kayla Reopelle (New Relic, Inc.)** 22:47 Oop.
Yeah, because I haven't done.
**Matthew Wear** 22:52 We work for instrumentation.
instrumentation to us… Possibly.
**Kayla Reopelle (New Relic, Inc.)** 23:08 Oh yeah, I see config properties here, config provider…
**Matthew Wear** 23:16 Yeah, so technically there's a config provider, but I guess I've nested it so low, that nobody really even interacts with that, but,
**Kayla Reopelle (New Relic, Inc.)** 23:32 Okay, interesting.
**Matthew Wear** 23:36 But yeah, so the… the… I guess the interesting things about this is that it, is that I do kind of keep a list of… Everything that the instrumentation ends up configuring.
And then… I check that against the list of properties that, Was passed in, and we'll at least warn if there were any Properties passed in that were not used, so that you at least know that this is not a valid option, because this is… it's kind of like a… The whole declarative config is JSON schema, so, like, if you're missing something, you know, that is actually part of the schema, then the config is just invalid, and you will fail to start. But if you make it that far.
Then this is kind of like a free-form art of the… Of the schema. So…
**Xuan Cao** 24:36 If you are…
**Matthew Wear** 24:38 Yeah.
**Xuan Cao** 24:38 In the, in the, in the PR for the rupee.
If you kept… Take a look at this generated by us.
Yeah, those are, I'm not sure if this is a… It considers, take predators, but those… Those modules Built based on the… Or generally based on the schema from the… On this repo?
So, yeah, like you said, we don't want a freeform kind of a… Dude.
you know, to have user to define whatever they want, you could have something that's not right, Wikipedia.
I think this is the idea to constrain them, to restrict them to certain behavior.
I'm not sure, just… as, big providers.
Because… And after we parse the YAML file, everything will go into this, no.
These paradors, interpreters of propagator will read from those, strat.
**Matthew Wear** 26:03 So… Yeah… I feel like your mic is not very good today, so you do keep breaking up, but if I'm understanding properly, like, I think… like, config provider does not work on any of this stuff. It does not work on any of the stuff that's actually been schemaed, as far as I understand. It's like… Completely for the instrumentation node, and that's just… a global that's available to your instrumentation, so it can config… configure itself based on what was ever in the YAML. That's kind of the… the extent of the config provider's, interface and responsibility.
In any case, I think, It might make everybody's life easier if we, handle the instrumentation development node separately, like… In a follow-up, whether we reintroduce this or we, go… Another route, and just kind of… At least use this to seed, kind of, the… The tracer provider portion of… I'll declare the config.
**Kayla Reopelle (New Relic, Inc.)** 27:43 Yeah, I think, I think that… Sounds good. Then we can, you know, get something out to users to start getting feedback on it, too. And we know that this is in phases.
Anyway, so that we can, kind of add that… Automatic config file support, you know, figuring out what we're gonna do with environment variables, so… We were always going to release a subset of features.
I can, include that in my comments, or, Or, Xuan, if you get to it first, either, either way.
Yeah, that's all I wanted to talk about on declarative config today. Thanks for talking through it with me.
Oh boy, we have a new… This just showed up.
Hannah, did you add this?
**Hannah** 28:42 Yes, yes, I just threw that on.
**Kayla Reopelle (New Relic, Inc.)** 28:45 Do you want to talk about it? I think, Maya? Yeah.
**Hannah** 28:49 Yeah, I'd love to. So, I added this kind of, summary of an issue that I'm having, as I am working on migrating the database libraries to support the, semantic convention new attributes for stable.
And so, I opened up a PR for LMDB, and James and I are having a discussion on what the span kind should be.
So I included a link to the PR as well as to the spec. And, I made this chart earlier for myself, because I feel like I've been walking in circles, and changing my opinion so… too frequently, so I feel like I needed… I need some help in this, decision.
So the root of the issue, I guess, is LMDB doesn't really cleanly fit into either span kind of client or internal. And, like, I put, some, like, bullet points on… what each… kind says it is, and why LMDB doesn't necessarily fit into either. Right now, we emit client.
And James' position is that it should be internal.
And so I… yeah, made this, like, pros and cons.
like… table.
And was hoping to see if I could get some, like, opinions on this. I can… I can walk through each of those bullet points, or, like, if you guys just want to, like, quickly, like, read over, I… I think… where I'm at right now is potentially maybe, like, a little bit more leaning internal.
Only because it's true that, like, nothing really… in the language itself, it's a little bit, like, hazy of, like, using, we may do this for internal, and so I think… that… it… because it just doesn't cleanly fit into client, maybe it's best as internal. Initially, I was super stoked on keeping a client, just because that's what we have right now. It's not a breaking change. Honestly, I'm not really even completely sure what what span kind is used to inform, or how that might impact end users if we change that. But this is the kind of thing that, moving to stable conventions, we should probably kind of decide on right now, and what the decision is may impact, like, later libraries.
So, yeah, unfortunately, not a lot of… other libraries instrument, LMDB, and I couldn't find anything else that was really using the span kind of internal. It seems to be, like, a newer addition, to allow for some flexibility, so that we don't, you know, people aren't, like, pigeonholed into things for client that don't fit client.
So, yeah, I… I would love… an opinion on this, if y'all need time to, like, digest it, click around on links, that's… that's fair. But if anyone has any initial thoughts, especially about, like.
how changing this mankind might impact people, I… I… that's a piece that I don't really know.
**Matthew Wear** 32:31 I don't know, before I read any of this stuff, my gut feeling was, like.
This would just be client, but after reading that… the spec that you kind of Brought up, you know, it's clear that the spec was changed to… from must to should.
And that, you know, a May was added for it to be… Boom.
Classified as internal.
So, it sounds to me like this wording was added probably Pretty… Just such a situation.
Oh.
So I think… my… I don't know, my feeling is that both are correct.
But maybe internal is slightly more correct?
If that makes any sense.
**Hannah** 33:30 Yeah, that's… that's where I ended up. I think I'm ending up. I… I don't… Do you happen to know, like, what the downstream impact of changing span kinds could be?
**Matthew Wear** 33:44 So, it really depends on, like, the backend. I think the backend wants to, like, Wants to look at a client, and… You really want to look at, like, you know.
A transition from client to server.
You know, that kind of pairing.
And that's… That's usually… indicates that a request has happened.
So that's kind of like a, You know, that's… that's a point where your trace becomes distributed, you know?
So I think that's really kind of the… The real, reason to have a client's fan, but, like… I don't know, we've been… the SIG has been through this throughout pretty much the history of hotel, but… it's just like, I think, like, the… the idealistic view behind that is, like, you know, every outbound request has this pair of client and server spans.
But the real world is a lot more messy than that, and we end up having this situation where we just have, like, nested client spans, which really does not make any sense, but… It's hard to get away from that, because you… Depending on what instrumentation you install, you don't really know which client is the real client.
you know, So… I think I'm getting off on a tangent, but I think, you know, those are my… that's my understanding of the client span, is that you're really looking for Back-ends, like, a significant thing for a backend, I think, would be where you transition from client to server.
Other than that, like, I don't know that it has, like, any… Real useful meaning.
**Hannah** 35:45 Okay, no, that is really helpful. That makes me feel better about moving this to a different span kind.
So… Thank you, that's a really helpful, that, especially on, like.
the spec language was updated to allow for these kind of, like, hazy situations. So… I think based on that, I'm comfortable moving that… this to an internal span kind. It is the first One that we're gonna have that's internal? I don't… I guess we could… I don't know if that really means anything, but, Yeah, I guess.
Just to call that out. Cool, I'm… I'm happy with that.
If anybody else has any other thoughts, would love to hear. Otherwise, I'll update the… PR to change that kind.
**Kayla Reopelle (New Relic, Inc.)** 36:42 Nice. Yeah, I'm good with that, too. I think that makes sense.
**Hannah** 36:49 Okay, cool. Thank you, guys.
**Kayla Reopelle (New Relic, Inc.)** 36:54 Okay, next topic, contribib-related… We… though I haven't been able to find it, James Thompson posted on the Hotel Ruby Slack today that we had a failure for HTTPX come through this morning because there was an error message that changed in a patch release.
And that caused one of our tests to fail. And so, he was wondering if our appraisals should use an equal sign instead of, Twiddlewalka to avoid, unexpected failures on patch releases.
I feel like we're making tons of changes to… our CI, to our appraisals, to our dependency management, I think a lot of things have… been pushed through, and I know this is just yet another change. I wanted to… Also, use this as an opportunity to check in with how we're feeling about where the CI is going, and how those other management things are going.
In addition to, like, answering the specific question.
Yeah, what are everyone's thoughts and feelings right now?
**Matthew Wear** 38:26 On the specific question, like… In theory, nothing should change.
Or… nothing should break on a patch.
And I do feel like we kind of want to know that, if something does…
**Kayla Reopelle (New Relic, Inc.)** 38:46 Yeah, yeah.
**Matthew Wear** 38:49 Like, as inconvenient as that is, and really, it's just… maybe… I think the fault is our test, more than anything.
**Kayla Reopelle (New Relic, Inc.)** 38:59 Yeah.
**Matthew Wear** 38:59 But… really, even to blame the test, I think it's kind of probably wrong, too. It's just… it's just one of those things, I think. It's like, you… you wanted to assert that this certain error happened, and Maybe, in retrospect, there's a better assertion you could have made, but, But, yeah, like, anything… so, my feeling is that… Patch release breakage should be… Boom.
Should be rare, and when it does happen.
we want to be aware of it, and we want it to be our fault. But if it is ever the library's fault, then I think, That we wanna… Be aware of that, too.
Because that's… Hey, that's something that could impact users.
**Kayla Reopelle (New Relic, Inc.)** 40:02 Yeah.
**Matthew Wear** 40:03 Where's this one… This will not.
**Kayla Reopelle (New Relic, Inc.)** 40:08 And so I, I think here… Like, one of James' goals lately has been to adjust the CI so that If there's a failure due to a library version change, it's limited to the scope of the Renovate PR that's updating the appraisal.
So I think right now, like, the HTTPX, though I haven't found it yet, it didn't look very hard or for very long.
If this is a failure, it could be failing on a lot of PRs.
If we have this hard equal sign, it would only be failing on the renovate PR whenever it opens up to bump that.
patch version on HTTPX.
So I guess, do we like that workflow to… Address those kinds of failures.
**Hannah** 41:17 Sorry, Kayla, in the… in the photo walker version, what we have right now, where… where is that failing? It's not just 1PR, it's multiple places?
**Kayla Reopelle (New Relic, Inc.)** 41:26 You know, let's just look together.
I don't know… so it would be… in what he reported, it was the HTTPX, let's see if it's in here.
Where'd you go? I saw a failure. Here we go. Brilliant. Okay, there it is.
So, right now… HTTPX is failing. It only released a patch update, and it's failing on this PR that's unrelated to HTTPX. So the CI looks broken here.
If we change it to a hard equals, then… it would never be updated except in the renovate PR. We wouldn't get any, like, lazy gem updates.
And so the failure would be scoped to just that, instead of this PR as well, before the renovate had been merged in.
**Hannah** 42:27 And… I mean, kind of what Matt was saying, like, this is pretty rare, right? Like, I don't know… If we've seen… I don't… yeah.
It does feel like… If it's not really that big of an issue.
I don't know if it's worth changing it, and… I… I do like the position of, like, if a failure happens, like… It's nice to actually know about it.
**Kayla Reopelle (New Relic, Inc.)** 43:05 And I think we still would. It would just be in… in one PR.
**Matthew Wear** 43:11 So your alternative… this alternative suggestion is that, Appraisals are using equals, and then… Renovate will bump every patch, and then we'll find out in the Renovate PR.
**Kayla Reopelle (New Relic, Inc.)** 43:27 Yeah.
then it's bumping all the patches in a group, but that does probably mean more renovate PRs.
**Matthew Wear** 43:38 I guess I'm fine with either one. I don't have a strong opinion, because we'll still get that signal.
**Kayla Reopelle (New Relic, Inc.)** 43:44 -
**Matthew Wear** 43:51 But again, these should be rare.
**Kayla Reopelle (New Relic, Inc.)** 43:53 Yeah, yeah.
I don't know when the last time is that we had something like this, so… Okay, so… I guess, any strong feelings, one way or the other, before we close this one?
**Matthew Wear** 44:16 I feel like both of them will work.
**Hannah** 44:22 Yeah, no strong feeling. I think knowing that we will get notified of the failure, which is good, somewhere.
I don't do a lot with renovate stuff, so… If… if it is going to create more PRs or issues?
That might suck, but, Yeah, on the other hand, I don't… if James has, like, a vision, I guess, for the CI, and this fits into that, that we all like, and it's easier, then… Maybe that's worth doing, if James is willing to take it on.
But again, no strong feelings either way.
**Kayla Reopelle (New Relic, Inc.)** 45:12 Okay, sounds good. I can add a comment to that effect in Slack.
Thanks.
We got 15 minutes left. We can… go through, you know, issues and PRs on each of these. Before I do that, is there anything else that people, wanted to discuss together today?
**Matthew Wear** 45:43 Nothing.
**Hannah** 45:44 Yeah, nothing for me.
**Kayla Reopelle (New Relic, Inc.)** 45:50 Okay, great.
let's see, I guess we really only have 3 minutes if we're gonna have polite meeting time, so… are folks comfortable with skipping that part today and just ending a little early?
Or would we like to go through them all together?
**Hannah** 46:10 I'm okay ending early.
**Matthew Wear** 46:12 Same.
**Kayla Reopelle (New Relic, Inc.)** 46:14 Alright.
Great. Okay. Well, thanks everyone for the discussions today, and we'll see each other on Slack. Have a good week.
**Matthew Wear** 46:25 Thanks.
**Hannah** 46:26 That's interesting.
**Xuan Cao** 46:27 here.
**Kayla Reopelle (New Relic, Inc.)** 46:28 Meet.

SIG: eBPF instrumentation
Date: 2026-04-15
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/fqVWZ55zrRTLZjVwaJ6RUIoz4ywa64lCcGl8dtkecZf2Ov2HsELiSD2Qhry5qcpu.hWyp60XB9hONEMog
============================================================

## Zoom Recording Transcript

**Giuseppe Ognibene | Coralogix** 00:38 Are you sleep, Brent?
**Stephen Lang** 00:42 Honey.
**Tyler** 01:06 Hey, how y'all doing?
**Giuseppe Ognibene | Coralogix** 01:10 Hi, Dallas.
**Tyler** 01:55 Cool, so, I'm looking at the agenda, we definitely have a fair amount. We can wait a little bit longer, though, we're about a minute and a half past the hour. I guess if you haven't yet, please go ahead and, Add yourself as an attendee, and if you, have more agenda items, go ahead and add them as well, and we can jump in here and get started in just a second.
Cool. Awesome. Okay, welcome everybody. Yeah, so today, to start us off, Nimrod, you wanted to talk about managing issues, going through that.
**Nimrod Avni** 03:05 Yeah, we had some discussions internally about how we manage issues, and I think that we have… a lot of issues that are open, that are either already solved, or no one's making any progress with them. And, like, from what I'm seeing in, like, other repositories, even OTEL ones, we can… do, like, we don't need to be, like, really strict about it, and I think that's ultimately an opinion of, like.
What we want to do, but we can have stuff like… Like, first of all, having the issue of, like, stale requests, like, stale issues, like, issues that have been open, and no one's discussed them for, like, a couple weeks or months, and then we can say either we give up on that, or, like, the original, guy who opened the issue, just ignored it, or… I don't know. And I think maybe we can even… I tried to do it for a couple of my issues, but we can go over some of the already open issues and see if any of them were already solved, we can just… resolve them. And, yeah, also doing, like.
Maybe even having, like, a workflow of, like, when you open an issue, you can, like, select if it's a bug, feature, docs, whatever, and it will automatically, like, automatically tag it for you.
Like, we don't need to, like, over-engineer that, like, in my opinion, but we can do, like, a bit of automation that can make… our lives better, so I wanted to hear your, opinions on that.
And I think we can… like, I guess maybe we need to go to… One of the hotel maintainers or something, to get some… I don't know, even automations with, like, automatically tagging issues as stale, or whatever, that's what I suggested, but if you have any other suggestions, I would love to hear it.
**Tyler** 05:01 So that's all within our power. You as a maintainer of the project are able to set up all these kinds of things. I'm very hesitant on closing issues automatically with automation like that.
It sets a bad precedent for a lot of, like, people that are sitting there waiting for an issue, and it also sets a bad precedent for sitting there waiting, so you're kind of in a rock and hard place on that one. You know, one side, people are not getting anything done for their issue, the other side is just, like, if you just close it without, like, any sort of update on it, like… It also feels bad. I do think that, like, the… the cleanup of issues that are complete is kind of a helpful thing. It's a… unfortunately, this is, I think, where, like, being a maintainer, this is part of the responsibility, is doing this.
And doing it periodically. I definitely noticed, I think Giuseppe was actually doing this recently, finding a bunch of issues that were already done, and just, like, commenting on them.
So, I mean, it is something that people can absolutely comment on, and help in the process.
I was just looking, like, we have 130 issues, like… I know that probably feels a lot to, people new to OTEL, but, In the grand scheme of things, like, it's actually really good. Believe it or not, and so I do think, though, that you raising this question is a really important thing, because you don't want to get to the point where, like, you know, you're thousands of issues deep at this point, and, like, you can't really you know, triage at that point. So, yeah, I think that… I think that… we can come up with some sort of policy. I don't know what that policy is. I know in Upstream Go.
We use… Robert, correct me if I'm wrong, I think it's 2 years, or something like that, like, where if nothing's been done, It's… it's closed automatically?
**Pellared** 06:57 I didn't remember at all, maybe it was one year.
**Tyler** 07:00 Yeah, okay.
**Pellared** 07:01 Please subscribe.
**Tyler** 07:03 Yeah, but yeah, I mean, something on the order of, like, of that timescale, I think, seems reasonable. There's also nothing really stopping people from, like, keeping things around for archaeological evidence, like, closed or open is always… it's always there, right? So, like, it's a good way to kind of frame it.
I think your suggestion around templates is, like, really valuable. I just noticed this yesterday, actually, as well. I was opening a few issues that, like, we don't have any, templates that can help a lot.
Just in the sense that, like, you know, a bug, a feature, even those two alone, can be very helpful.
there's a lot of really great templating systems, or the templating support that GitHub has actually added, recently. So, like, you can have it so it's essentially, like, a form, so it comes in the way that you really want. That helps a lot. We haven't really seen this problem, but, like, especially in bugs, in other upstream projects, like.
you get a lot of very low-value, comments, like, this isn't working, and you're like, that's great, like, I don't… what's the actual problem? How do I reproduce it? Like, all these other things that you actually want to know in those things, you can ask them to, like, fill these out in the process.
So yeah, I mean, I think templating is a great idea. We can also set up that instrumentation or automation to, like, close things out. Again, like, that's just a GitHub action, if I'm not mistaken, that we use upstream. It's just, like, a steel detector. We do the same thing for PRs as well.
Go has way more of a problem with this than I think this project does. But yeah, so, like.
just kind of giving you the lay of the land there, like, I think that… I think it's good. I think it's great that you're thinking about this, but I also think that, you know, maintainer triaging is very helpful here, and just trying to, like, go through issues, and not… exorbitant amounts, but something like, you know, if you can get 10 issues done a week, all of a sudden, you know, by the end of the year, you're very much on top of these kinds of things, so, yeah.
**Nimrod Avni** 09:00 Got it.
**Tyler** 09:01 5 maintainers.
**Nimrod Avni** 09:03 Yeah, I tried to go over a couple stuff, and there's some stuff that I'm either not super sure, or, like, not, part of the stuff I thought, so I don't know if I should resolve them, or is anyone, working on them. I guess bugs we should pretty much always keep until they are solved, but there are some there that are even… either discussions or on features that are in development, or… Of course, all the roadmap is also in issues, I guess we can kind of… ignore that. But yeah, I can, like, draft up something, and then if you have any, like, whatever, like, regarding our policy, we can, I guess, always change it, so I'll try to get something done.
**Tyler** 09:46 Yeah, yeah, I think that whatever… whatever you want to do as, like, a starting point, that sounds good.
The… the question that you have in the doc, if I'm not mistaken, about, discussions versus, issues, that's a… that's a… It's a tough one. I do think that, like, it's really annoying sometimes when you do just have, like, a really authentic question, and an issue.
Some people don't like using discussions.
It sometimes also doesn't where it works the other way. Like, people have a… just, like, they think it's a question, and then it turns into, like, hey, that's actually, like, a really good idea for a feature, or something like that.
I think you can go… from issue to discussion, I don't think you can go from discussion… So there is a little bit of, like, if you do start with the discussion, it's hard to make it into an issue, other than just, like, creating a new issue and then, like, copying stuff in.
So, policy-wise, I'm open to whatever you want. I do think that, like, maybe just directing people there might be helpful, especially if, like, that's their position, and they know that it's just, like, a quick question, but, Yeah, I also think Slack's a better solution there as well, but… things aren't archived if they're in Slack, I guess is the downside, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:06 One idea would be on the issue template, when they're about to open, is maybe you can just say, if you think this is a question, you can start a discussion instead.
Let's see…
**Nimrod Avni** 11:16 Rediscussion, or Slash.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:18 Yeah. If you… yeah, I feel you just need an answer to your question, But if you want to report a bug, or suggest a feature, or, you know, that's fine, but if you want to ask if this should be a good idea, go ahead and do it.
Yeah.
That's great, I mean, I wish Mark was here. Mark is really… he's on vacation, but Mark is really into this sort of cleanup of… bug issues and so on, proactively. Does that. So… I mean, we can even, like, maybe… Just, had a bug bash week.
One week, all of us, which is sort of, as maintainers, on a mission to kind of clean up the backlog of issues and figure out what's real, what's not.
**Tyler** 12:06 Yeah, and one of the… one of the things, Nimrod, that you bring this up, like, I had slated for the V1, like, stable release is going through all the bugs, we have.
And just, like, classifying them as well, and saying, like, this is a blocker for V1, and this isn't a blocker for V1.
Which is usually done with, like, a labeling system, as we've done in the past, so, Yeah, so maybe, like, actually, like, a prioritization, might be helpful here, like, if people are thinking, like.
it's really important or not. Obviously, like, maintainers can always change it, but yeah, if you wanted to think along those lines, that's eventually where I was gonna go with this as well, because, like, a really quick inventory.
Also, if people would like to go and, for your bug bash idea, find bugs, I think it'd be really helpful prior to the V1, so… We get things addressed before, before we stabilize it, but… Not everything needs to get addressed either, so, yeah.
Cool. I think.
Yeah, Matthias got something like this. Yeah, that's… very easy to set up, there. Another place to go take a look at the issue template, is the docs repo, so opentelemetry.io. They've got, like.
A lot of really great templates in there as well, more than others. I think the collector as well, it becomes a little bit helpful, like, more helpful for labeling.
20 different labels on a particular issue, around, like, you know, what component is this for, that kind of thing. So, yeah, this is where templates can be really helpful.
All the other… almost all the other repos, I don't know about all of them, but almost all the other repos have templates, so we could take a look at… or anyone who's looking to do this can take a look at their… Those issues, so yeah.
Cool.
Alright, Nimrod, are you okay if we, move on on this one?
**Nimrod Avni** 14:08 Yeah, definitely.
**Tyler** 14:10 Okay.
Awesome. Okay, Rafael, you wanted to ask a question about our config.
**Rafael Roquetto** 14:23 Yeah, it's, more like, You know… We've been looking at our config, and, you know, there's a lot of work on trying to streamline the config options.
And… I feel we have a lot of options. Maybe they're necessary, I'm not saying they're wrong, or anything, I'm just throwing it out there, like, as food for thought, not something that I have anything more constructive to say about it, but sometimes I feel like we have so many knobs.
And it's really difficult to make sense of them. But maybe if you don't know what you're doing, you should just stick with the thoughts. So I'm not saying it is necessarily a bad thing, but I just wanted to… Ask your guys what you guys think in general, like, if it's worth, down the road spending some time to try to maybe, you know, streamline those as well, and… Or not, or it's just the nature of what we do?
**Tyler** 15:19 Yeah, I definitely see this as a large part of this Configv2 work that I've been working on. I… I think, just to answer your question directly, like, this idea that We have a lot of knobs, I think is… is… There's nothing… I think inherently wrong. Obviously, like, if you're just putting, like, switches into the config.
because you think it could be useful, it can definitely lead to a bloating of the config, and people are overwhelmed with it. But I think that this is one of those things where if you structure the config a little better, like, what you're saying is if you leave it in there and, like, people just don't touch it if they don't know what it is, it can be better suited, because you can take a lot of these, Fine detail control knobs, or other, like, tuning knobs.
Around features, or around performance, or something like that, and you can put them in sections that users don't don't care about. And I think that's kind of, like.
one of the goals, actually, of this PR, and so I kind of wanted to Thanks for bringing this up, because I think this is actually really important. One of the goals is specifically that, like.
out of the box, our config should work, which it does already. Like, our default should be sane, right? But the other thing is, is if, like, you really want to, like, achieve… common tasks from, like, a user space, say, like, You know, scoping a particular, instrumentation, scoping some sort of target, then you should be able to do that very easily, and it shouldn't be too confusing, is kind of the idea, around, you know, where in the config you should be looking and where in the config you should actually be touching. So, yeah, that's kind of like… leading to this whole question around, well, a lot of these details in how maybe you'd want to tune this thing, you know, where should they live compared to the other things? I think, like, putting things in this, like.
you know, some sort of, like, engine structure. There's this other thing I've got in here, like, now that's, this daemon structure. Like, these sort of, like, detailed tuning things are really easy to just not pay attention to when you're a user that just wants to, you know.
tune some sort of, like, runtime instrumentation, or tune some sort of, matching pattern here, right? Like, this is completely separate at this point, and there's not, like, any confusion around, like, this doesn't relate to the other thing, so I just look in this one specific area. So I, like, and the default should work for all those other tuning parameters, is kind of the idea.
So I, yeah, I guess I kind of wanted to… sneak in, a request that maybe we could talk a little bit about this, or touch in on this issue. Rafael, I don't know if that helps.
**Rafael Roquetto** 18:03 Yeah, that does help, I'll have a look. What made me think of it a lot is, I was looking at Giuseppe's, like, the map changes, which, by the way, it's good, I think it's the right thing to do, so I'm not going against that. It was just, like, an inspiration, because when I was reviewing that PR, I had trouble kind of understanding, okay, we have the queue size, we have the map size, what happens if… We, you know, misconfigure one and the other, and maybe that's just the nature of it. Maybe that's… it is what it is, and I just need to know, you know, how to operate those knobs.
But it just got me wondering, if… not in that in particular, but it was just an inspiration, like.
If we could do this better, but yeah, that's why I wanted to ask. But I'll try to have a look at this config as well, and see if I can add something constructive to it, and maybe down the road, like, revisit some of those things, and… maybe there is a better way of doing things, maybe there isn't. Maybe we would already, you know, it's the nature of what we're trying to solve, and it is what it is. So I just wanted to bring that up to see if anyone had any other thoughts on that.
**Tyler** 19:12 Yeah, I'm a big fan of, like, when you're writing something and you have a lot of the implementation in your mind, it's very easy to say, like, we need this config, for this thing, right? But then as the end user.
Yeah, like, really, what does that person actually care about? You know, because it's very easy to say, like, here's these 3 knobs, right? But the end user actually doesn't care anything about those 3 knobs, they just care about, like.
does it work or does it not work, right? So maybe they just want, like, an on-off switch instead of, you know, 3 knobs that each have their own, like, numerical value to them, or something like that. And so I think that, like, it's, I don't think it's a problem to start with config like this. I do think that, like, it helps, once you have it, to take, like, a step back and say, like, okay, like, as an end user.
like, do I know the difference between a queue and, like, a batch size and, like, a buffer or something like that? Like, these are all very implementation-specific terms, and, like.
they're not obvious at all to the end user, right? So then how do you make them obvious? Because… This may be very helpful for them to tune, and maybe that's just through writing a ton of documentation or a blog post showing you, like, hey, this is what you do when this particular situation arises.
Or it could be, like, do you structure your config differently? Like, is there a way to, like, make this actually, like, work?
Or it could be, like.
hit the 80% target of all defaults that you would ever need, and, like, maybe you have dynamic allocations for these things that are, like, gonna work for everybody, and then you turn on that dynamic allocation, or you turn it off, or something like that, right? So, like… Yeah, these things, I think, are good to ask these questions.
I do think hiding them away is helpful.
And I do think we need to have… Some sort of agreed-upon standard here, because it's easy to have configuration bloat.
So, as, as, you know, we migrate into some sort of new configuration pattern, like, what is the… what are the questions that we're asking ourselves when we're adding to that, or refining it, or changing it, or something like that, I think are important. So, the concerns that you have, I think.
around a specific issue, I think are important to capture, and make sure they're captured in that PR, Raphael, around, like.
because that's one of the other things I really want that PR to serve, is not like, here's the new config, and then, like, we just keep adding stuff to it in the, you know, the old-fashioned way. It's like, if there's a… if there is a new way to think about it, like, it needs to be captured in, like, there's a meta doc in there.
I'm like, here's some, like, ideas and principles around this that are really important there. So, yeah, I think it's helpful just to, like, document those kinds of things as we go through into that process.
**Rafael Roquetto** 21:52 Yep, okay, sounds good.
Thanks.
**Tyler** 21:57 Cool.
Yeah, as a call-out, go ahead.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:01 Yeah, I had a comment. I sort of had that in the back of the agenda, but I moved it out because I think it's related. So… the config as it stands now, it's even a slightly bigger problem, for self-serve users that do not actually spend time reading our docs, or start with our Helm chart, or anything like that.
They don't know the product, nobody wants to read docs, so they use AI these days to generate the config. Now, when you think about it, what our AI is trained on is our examples.
Like, they look at the GitHub repo, and they consume our codebase, and they train based on that.
the examples are full with options nobody else should be using, because they test something specific, like an edge condition or something like that. And to give you a perspective of this, we just had a customer that had reported a high usage of memory, which ended up being than using the unmatched path, which we say, do not use this. But all the tests we have use unmatched path, because it's the most reliable way to get a path.
And not worried that something is turned into a low cardinality thing. So, if you ask the AI to generate an OB config, you'll likely make tons of mistakes and actually… you know, get a lot of food guns in there.
So, I don't know what is a way for us to kind of generate something that would help AIs get better at configuring OV.
In general, like, even when we get the new config and whatnot, is there a way to… Kind of publish something, or… I don't know, make sure they pick that up.
I really now am at loss, because this is becoming a bigger, bigger problem. We never used to have these issues.
But now, I've seen a couple of AI-generated configs in the past that just had completely… Bogus stuff in there. Like, random options being set that just… Alright.
**Rafael Roquetto** 24:03 Perhaps we could… I don't know if these agents.md or all these files, they work very well, so that's one thing to verify, but we could have something for, like, AI… just like we have for code review, AI config guidelines, where we can maybe craft like, standard… config that that's your starting point, a simple one, and kind of doc… or we already have documented the fields, and tell you, I look here, look there, and, like, give it some guidelines. Start from this config, and don't bloat it, you know, like, unless you know what you're doing, like, maybe something like that. I don't know, maybe I'm stating the obvious here.
**Tyler** 24:46 So that… that… that'll work really well for, like, developers here, but it won't work really well for, like, end users, unfortunately, because a lot of the AI systems are just going to be going off of, like, the… the actual, LLM, and that LLM has been trained on data that's not going to be in that, like, it's not going to read the agents, that MD, right?
It's going to look at other blog posts, it's going to look at all of our testing, it's going to look at all of these other things, and it's going to be training off of those things, right? And so… To Nicola's point, like, I… I think the answer actually is, like, one, you could… we can… I think the hotel actually is trying to work on an FCP server. I think that might be an Austin thing, or it might be a… somebody else think, but that could be really helpful, like, if your… if your end users are using an MCP server for OTEL, like, we can try to hook into there, and you can… you can… kind of collaborate with what Raphael is just talking about, like, essentially move that… Definition of what a good, config is to that MCP server. I think that's gonna be the edge case. I don't think a lot of people are gonna be using that. I think they're just gonna be using ChatGPT.
Which means that, I think.
what you'd want to do is write a lot of really good blog posts around config, so, if you want to do X or you want to do Y, like, basic functions of the config, or have really good docs around this. I think that that's another thing that the LLMs, like, as they go through their training in the next cycles or two, are going to pick up, and it'll become the de facto standard.
it could, you know, very easily just be saying, like, let's look over this, like, routes policy and say, like, hey, this, like, you know, skips these things, like, you should not use these. This is used for only, like, only use this in a situation like this. Like, an LM can then very easily pick that up.
In its training data, and I think an AI could be very smart about saying like that. If you put that in, like, plain English, like an empty file, like we put in our doc somewhere, like.
it'll figure that out. I do think also, like, this config V2 provides a, like, ample opportunity for this, because as we're going through a new config, like, it's gonna have to write a V2 config, right? It's not gonna be able to write the V1 or whatever we want to call these, like, versionings, right? So… as we build this thing, it's going to look at all of the examples we build around it.
And so I think that this is, I think, a very apt opportunity that you're bringing up, that, like, if we design this in a way that an AI can better easily, like, figure these things out, if we can hide things in a, like, you know, in a way that, like, they aren't going to touch, I think is also really helpful.
And then maybe the other option is, like, if we do have foot guns in the config, like, maybe we remove them.
Or we put them in a section that's called, like, unsafe or something like that. I don't know, but yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:37 Yeah, yeah. Yeah, that's a good idea, that's what I was thinking as well, like, have a… if you want to use that option, you have to enable use developer options or something.
And that must be in the config. And if you mention it, and you haven't used explicitly that developer mode or whatever, then it just warns you and says, sorry, I ignore this option, that's not supposed to be used, unless you're in development mode or something.
I think… But then it will train on our tests again, unfortunately, and… and maybe the thing is, like, sorry to interrupt for cutting you off, I was thinking, because we build a lot of this stuff for the test environment, so certain options should not be available unless you build OB with a special flag that is… we are building that with tests. So use the main OB, those options would just not be available for you, and we'll tell them, you know, sorry, that's not available.
That's an internal option. You shouldn't be using it.
So then, by our tests, which builds a Docker image with a separate Docker build image, then those will… Are able to use those options with some time.
Crap.
**Nimrod Avni** 28:54 I wanted to say that I think, like, in every project, basically, like, I think Mattia also commented that, like, the LLM trains on a version that is way, way… like, it's not even the current one used, so I think… a lot of, like, hard… like, if you go to, like, it depends, like, what hardness are you using, but I think most of them will do… a, you know, a web search of trying to get the current config, and not, just relying on other training data, especially for a product, let's say, like, OB did. We're not, like, a really, like, a React or something that we have millions of.
**Nikola Grcevski @ Grafana / OpenTelemetry** 29:31 Next, let's.
**Nimrod Avni** 29:32 examples, we have, like, a couple blog posts and GitHub. So I think, I think most of the time it will do, like, either a web search or… or… yeah, and I think if we have something that is… like, human and LLM friendly in our repo, and in, yeah, and even in, like, articles. It doesn't need to be in the training data, more of, like, it needs to be clear that this is, like, the recommended configs, and we should, like.
direct it away from, like, testing and whatever, like, testing configuration.
That's, like.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:09 Don't look at the tester.
**Nimrod Avni** 30:10 If you go now and say, give me a React config, or whatever, or like a collector config, I guess it will do some web search on the config and not go through its training data.
I'm hoping, at least.
**Mattia Meleleo** 30:26 Now that I think about it, I got into this today. I wanted to deploy some app on a GKE cluster, so I instructed the cloud code to… To do that?
And it was stuck in a loop where it tried to fetch the correct config from the documentation of Obi, but it was not working, so I had to point it out in the in the local repository, and to go in the correct version of the config, and it then managed to find the JSON schema for the config, and to make a correct one, but it was not working when I'm pointing it Generically.
**Tyler** 31:14 I also wonder if, like, it does a lot better at, like, markdown? Is it having this, like, meta documentation, the thing that, like, you know, Nimrod's also building off of the JSON schema, and just, like, documentation about it?
Would help as well. You know, like, in finding… finding that documentation maybe easier for it to parse, especially if that includes, like, you know.
You probably don't want to use this in this section or something like that of the config options.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:44 Okay, so maybe it's the thing we need to go and check.
what Chase schema generates, and specifically look for the options that are bad, or people can shoot themselves in the foot with, and then just go, hey, don't use this. This is for internal testing only, or something like that.
Yeah, like…
**Tyler** 32:03 just putting a generic warning, I think, is helpful there, and, like, it should be able to figure that out. And it can show up in the docs as well, like, there's nothing, like, in… because there's, like.
this meta, like, description stuff in, JSON schema that you can include there, and you can include comments in YAML. So, yeah, like, we can… we can do the things like that. I think it actually might be… That might be one of the best ways to start, working on this, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:32 Thanks.
**Tyler** 32:32 But, I do also think that, like, MCP and RAG are, like, your best friends here, if you can get people to use them. But, Yeah, I guess if you're talking directly to a customer, and we have, like, an MCP server at OTEL, then you can tell them, like, hey, like, this will solve your problem in the future going forward, but, like.
to the general public, like, that might not… all the other things, I think, are more helpful here, so, yeah.
So, I guess that being said, I'd like to move on, and I'd like to say, please take a look at that Configv2 options. There's a lot of docs in there as well, so please, those are important, as we've just talked about. And then, yeah, I'd like to progress that one as well, and iterate on it.
There's a lot more to say there, but there's a lot more to go. So, let's… keep… Progressing this, sorry, I'm trying to find my meeting notes.
Giuseppe and Nimrod, I think you are up next. You wanted to… Talk about, the, the OB stats, the, yeah, the TCP, Stats.
**Nimrod Avni** 33:43 Pito, you want me to go? You wanna say it yourself?
**Giuseppe Ognibene | Coralogix** 33:47 As you wish.
**Nimrod Avni** 33:49 I can start, and we can…
**Giuseppe Ognibene | Coralogix** 33:50 Hell yeah.
**Nimrod Avni** 33:51 Basically, we want to… start, like, pushing towards, like, a semantic convention for all the, kind of, TCP… we're starting off with, like, TCP stats, and, like, I think that's the same thing that the open telemetry Network were producing, and there's some other… some other producers of similar metrics. And we didn't find a lot of, like, we… like, the only kind of… Similar stuff we found is there's a couple system metrics that don't really match what we, what we are exporting with the stat metrics. And, there's also some hardware metrics here, And I know, I think Sven? I think he was also, interested in doing… I don't know if it's only for the flow metrics, or for the, or for general, like, TCP and network metrics, but we wanted to, kind of start pushing that, and we… like, I and Pino, we never tried to do it, so if you guys… if you guys have any opinions on, like.
what, like, on this convention stuff that we should push for, or maybe even the process of, like, we should open, like, is it starting with, like, only a PR to the semantic convention repository, or do we also need to come up with a concrete plan, or is it only, like, a… we should, like, a discussion. I never tried to do anything like that, so I don't really know,
**Mario Macias** 35:25 Yeah…
**Nimrod Avni** 35:26 Better…
**Mario Macias** 35:28 I've… I've, I've tried, doing this for the… But also for the network flows, and… Yeah, you need to insist, because, for example, I tried, I contacted people, yeah, okay, maybe you should go there, you are bumping from one place to another, then you forget, I forgot, and then it's still pending. So, probably, we can add this To our proposal of… of also network flows… network flow metrics, and the same way we have network flow… bytes, we can have network flows, TCP, RTT, or something… Something like this. Another option will be to the existing network metrics, proposing to add, proposing to add, maybe source and destination IPs, so you can… you can just add in a couple of… of attributes to the existing metrics.
Maybe you get it also already resolved, it's faster.
But, yeah, otherwise…
**Nimrod Avni** 36:40 Yeah, I'm still not… like, I know we have the net only and stats only, I'm not… Like, I don't know if, semantically we want to differentiate between flows and our stuff that are more, like, network-specific for, like.
**Mario Macias** 36:56 gap.
**Nimrod Avni** 36:57 TCP runtime, TCP resubmissions, whatever.
Yeah, I'm not a semantic convention guy, so I don't really know, but I guess we can… like, just open some PR with, with, I don't know, some suggestion, and then people will push back, and we need to, like, continue on. I guess that's the…
**Mario Macias** 37:21 Yeah, yeah.
**Nimrod Avni** 37:22 That's the main gist.
**Mario Macias** 37:25 Okay.
Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:27 But I guess, being optimistic, I guess your question is, should we just drop the OB prefix, right?
**Nimrod Avni** 37:33 Like, we have… I think we have it now, just to differentiate, like, to say, okay, this is not, like… most of the stuff that we produce are semantic conversion, and of course, in the… if we suggest it to upstream, we're gonna drop the OB one, but… Nikola Grcevski @ Grafana / OpenTelemetry 37:48 Hmm.
**Nimrod Avni** 37:48 I think, for now, it just signals that, you know, this is a custom metric that OV produces, and… Like, it's subject to change, and once we have semantic convention, we're gonna go there.
Hello.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:03 Yeah, it's true. So one approach would be to not have an OB and just have it like that, and just hope that what we propose gets accepted, maybe with variations. Maybe that never happens. But these things move slow, and I think we probably shouldn't hold progress.
**Nimrod Avni** 38:19 No, this is not for, like, we want to continue pushing that, but, like, in parallel, try to get… You know, some agreement on, like, Because I think it's easier to, I don't know, for other consumers of OB to build products around these metrics if they are stable and not, like, say, okay, this only works if you have OB, and the metrics are prefixed with OB, and… Nikola Grcevski @ Grafana / OpenTelemetry 38:43 No.
**Mario Macias** 38:46 Yeah.
**Tyler** 38:49 So, I definitely think if you want to get these merged, you're gonna need to engage with these, like, SIGs. It's, like, well known that, like, the semantic conventions is a great place for, PRS to go to die, and, like.
If you want this to get in, I'd recommend trying to go to one of the SIG meetings, and talking to people in person, and just kind of asking where this can actually take place. Sounds like, Mario, you might have already, like, connected with some people.
I know, I mean, I know people, like, in the semantic convention world, but the problem is that it's a very fractured and federated world around… so, like, the networking metric people don't talk with, like, the Gen AI people, or vice versa. Like, there's 20 different areas, right? So… Yeah, like, I don't know exactly who to point you to, I don't know who's on the networking stuff, but it may not be a lot of people, but I do know, like, if you go to the SIG meeting and you pretty much just say what you've just said, to them, they can point you in the right place, or they can say, like.
you're now the guy, and so, you know, go ahead and, like, let's… why don't you review some docs, and, like, now you can come up with these things. It'll help progress your PR pretty easily, I think, if you do something like that, yeah.
**Nimrod Avni** 40:05 Okay, I think we can start to push that, I guess.
**Tyler** 40:10 Yeah.
**Mario Macias** 40:11 The… I'm sorry.
**Tyler** 40:14 Go ahead.
**Mario Macias** 40:15 No, I mean, do you want to meet… Tomorrow, or any other day this week, or the next week, and maybe we can pack all this improvement, all this proposal with the current network metrics, and the other suggestions, so… the other suggestions from… from Sven. I think there is already some… some work done in… in an issue in… in… in our repo, so maybe… maybe we can go… I don't know what do you think is the best idea, to pack everything into a single proposal, or better, smaller.
Fragmented different proposals for each of the changes we want to do.
**Tyler** 40:58 I think both is what you'd want to do. I would come to the SIG and say, like, holistically, this is what we want, like, we want to hit all of these different areas of networking, and here's, like, the five-stage approach that we want to try to get this in. So, you know, we want to try to do these stats metrics, we want to try to do these flow metrics, we want to try to do, like… And saying, like, these are the things we're gonna tackle, and, like, these are our priorities, so… because, like, coming to them and saying, like, we want to add 100 different things, like, that's not gonna work. Coming to them and saying, like, we only want this small scope may not motivate them enough, so I think… doing both is a very helpful, approach, and showing that you've thought about this as well, I think is going to be very helpful.
**Mario Macias** 41:35 Okay.
**Nimrod Avni** 41:37 Yeah, I think we can maybe, like, after seeing together, like, kind of say if we can unify, like, the network metric and stats metrics, if they are, like, the same fundamentally, or, like, should we… Consider them, like, different stuff, or, like, if it should be part of the network metrics or something else, but… But yeah, I agree, you can come around this.
**Tyler** 42:01 Yeah, that's going to be one of, like, the main questions that they ask you. You know, if you're adding 20 metrics, can you add 5 instead? Like, is there a way to represent and encode the same data in a smaller set of metrics? Like, are there different dimensions that you can capture on a single metric that will, like, so… you know, for network I.O, it's really easy to say, like, flow, but, like, flow in or flow out, right? Like, so you'd really want to do something like.
some sort of flow, and then have an attribute be the distinguishing factor here. And so, like, these are some of these questions they're gonna ask you around, like, are there ways to consolidate these? Are there ways, you know, what has been thought about? Like, why is this metric unique, I guess is a good way to think about it.
**Mario Macias** 42:41 Okay.
**Tyler** 42:42 In a lot of the… questionings are gonna come to, like, how is this gonna get represented on the backend? So, like, if you take this, and I want to re-aggregate this in some sort of user-specific way.
two metrics are very hard to, like, pull together in some systems. Metrics with the same, like, name, but have different dimensions are easier to pull together in some systems, so, like, that is.
**Mario Macias** 43:04 There's this.
**Tyler** 43:04 Something they think a lot about, yeah.
**Mario Macias** 43:07 Okay.
**Tyler** 43:11 But yeah, if you don't make progress in the next week, I think, Mario, you work with, Lyudmila, and there's lots of other people in the world that I know in the semantic conventions, but, like, you can ping them, or you can ping me, and then we can make sure this gets.
**Mario Macias** 43:26 Okay.
**Tyler** 43:27 Movement, yeah.
**Mario Macias** 43:27 Okay.
**Tyler** 43:30 Okay, yeah, thanks for taking this on, though. This is… this is great. This is… This is really important work, Although I do say, be careful what you get good at, because now you become our semantic conventions point people, by doing this. But yeah.
**Nimrod Avni** 43:48 Maybe I can do it.
**Tyler** 43:51 I have high hopes.
Okay, Rafael, maybe I'll ask you this SOC trader, I added the roadmap at the end, is this something you just want to quickly shout out so, we don't get lost?
**Rafael Roquetto** 44:04 We don't need to look at the PR per se. I just wanted to bring it to people's attention, because it's gonna be a big PR, I'm still working on it. So, the motivation for this is, when I was doing .NET, the first attempt of .NET to injecting the trace parent.
into… on ingress to have the .NET propagate. That didn't work, like, messing with the packets doesn't work.
But that kind of, is reminiscent of that code. And we have a different, let's say, issue reported, where someone is reporting lots of CPU usage on the target processor. It was a Redis example.
Where OB's adding, like, 10% on top of, CPU. It's a, it's a, like.
corner case, I guess. I traced that to, being, K-probe overhead, especially TCP send and receive message.
And, I thought, well, maybe I can try to reuse this code that uses, like, socket programs instead of, K-props to see if CPU gets better, and it gets much better, it's, like, way lower overhead.
So that's, yeah, that's the PR in. I mean, it's a big, big PR, we're gonna try to slice it even in the smaller ones. Mattia has a, HTTP2, context propagation PR app that I want to, you know, after that merge, I want to rebase on top of that, because I can reuse a lot of his code, which is awesome.
So it's just a heads up. That's all I wanted to say about this, so you, you know, when you see this coming up, this huge thing, you don't get surprised.
**Tyler** 45:46 Gotcha. Okay, thank you. Yeah, I'm also, very interested in Mattia's HTTP2 PR.
**Rafael Roquetto** 45:54 And, just real quickly, and then once this gets in, it's gonna be disabled by default, as experimental, so orthogonal. And then down the road, what I would like to do is do some reshuffling of the codes to be able to share more code between all the parts, so we don't have duplications, so it's a, like, long-term thing.
goal.
**Tyler** 46:16 Awesome. Yeah, that sounds good.
Oh, I guess Mattia actually had to drop, so I was gonna ask him about that, but yeah.
No worries.
Okay.
Cool. I did want to jump in and talk a little bit about our, goals and just check in. We are now in, April.
Believe it or not.
So I just wanted to… maybe we can jump through this really quick.
Okay, cool. So… Maybe just kind of go down the list, Yeah, let's just go down the list. So… This table, V1, I'm still working on this. This is definitely really great. We got that support matrix in, really big step towards, solidification of this. Next up is then, the config, I think, is kind of the biggest one on the list. There's also a stability around telemetry, which we kind of just talked about some of this telemetry stuff, but I think there's, I think, more around how we want to migrate this. I think I just saw, before I got on here, a comment from Nimrod around using Weaver here. I haven't responded to… But there's a lot of really great things going on here. We are progressing on this, so, I think this is actually pretty accurate. So, just in the triaging portion of this, I think we're doing pretty good.
Epic, for the additional protocol support, I don't know what the status on this is. I think, Nimrod, you're on here. I think that we have… Fair amount done.
**Nimrod Avni** 47:46 Yeah, and I think even we added a couple stuff that were not, like GenAI, and NAT, and Couchbase.
Yeah. So I think we added a bunch of stuff, but… Yeah, there's some, like, the Mongo stuff we, I don't think we reached, I think.
If I remember, Steven, you had planned for… Nats, I think we can check off, right, Mark?
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:13 There's a PR, but it's not merged yet.
Okay. You know, this happens.
Yeah, there's some comments on it that's almost good, but I think there's some comments… .
**Nimrod Avni** 48:28 So I think, yeah, Mattia's on the gRPC context propagation. I think, Steven, you had plans for AMQP, right?
**Stephen Lang** 48:38 Yeah, I've not started on this yet. I've not looked at it.
**Nimrod Avni** 48:42 And… Yeah, I don't remember what else we add, like, we think we added more stuff, but I can't remember.
**Rafael Roquetto** 48:49 There is a…
**Nimrod Avni** 48:50 A question of, like, whoever needs, like, Redis PubSub will, add it, because, like, I think it's… Like, Like, we added usually because of customer demands and not, like, because we just want to add… I think you also added, like, the JSON RPC and MCP and stuff like that.
**Tyler** 49:10 Oh, yeah, yeah.
**Rafael Roquetto** 49:12 And there is also the AMS SQL PR that's, I guess… Nikola Grcevski @ Grafana / OpenTelemetry 49:15 Almost there.
**Nimrod Avni** 49:17 Yeah.
**Rafael Roquetto** 49:18 Yep.
**Nimrod Avni** 49:19 So it's a bunch of stuff.
**Tyler** 49:21 This is great.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:21 It's gonna be really comprehensive, guys. Yeah.
**Rafael Roquetto** 49:25 This is awesome.
**Nimrod Avni** 49:26 No protocol left.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:28 behind.
**Nimrod Avni** 49:28 Act.
**Tyler** 49:30 Yeah, I… I'm… I'm getting lost. So, I'm just gonna say this. So, if you can… Actually, could you… yeah, Nimbra, could you fill it in, or, if you want to leave a comment or something, like, yeah, I can… I can update it a bit.
**Nimrod Avni** 49:41 Does it need to have, like, a corresponding issue or something, or just to update the…
**Tyler** 49:46 Do you have an issue open, link it as a sub-issue here, it'd be great, because it helps show us progress, but if you don't, then that's not, critical. I think, I think, like, some of these, again, like, we've talked about maybe just cleaning these up, because it actually may be done, or have things done, so… Yeah, so just, yeah, if you could just go ahead and update where we're at, and then, yeah, we can, we can… work on that one. That's great, like, this is great progress. There's tons of stuff going on here, so, yeah.
**Nimrod Avni** 50:12 Cool?
**Tyler** 50:13 Awesome.
Okay. Also, the, support the .net?
This is another one I definitely wanted to check in on as an epic.
**Rafael Roquetto** 50:23 Yeah, so… after my first approach failed, then I got sidetracked with the stock tracer, but I'm… I've really… next on my priority list, like, really high, so I want to get to it in the, you know, incoming week or something.
I have some.
**Tyler** 50:40 Oh, cool.
**Rafael Roquetto** 50:40 of how I'm gonna, tackle this. So, give me, like, one or two weeks, and I'll give you a better update.
**Tyler** 50:48 I gotcha. I've got, Pyotr and, Robert, I don't know if he's still on the call, they, they've definitely responded to this from the… Oh, yeah. Okay, yeah, from the Smokehouse. If you had any other questions, they've… they're really good experts in the .NET world, and, like, if they wanted to talk specifics, I think that they can help you. The internal, like, under-the-hood stuff, that's probably where you're gonna come in, Raphael, but, like, yeah, if you wanted to, like, sync with them on that, yeah.
**Rafael Roquetto** 51:14 Absolutely. Cool.
Yeah. Appreciate it.
**Tyler** 51:18 Yeah, I'd appreciate your…
**Pellared** 51:20 I have it in my to-do list, because I have shared some things with Nikola already. I wanted also to make it public there, but I just didn't have found, like, even 5 minutes to just, you know, clean it up and send it. So yeah, it's on my list. Nikola, do you think… do you think that I shared are worth sharing also there?
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:41 Sorry, sharing a what?
**Pellared** 51:43 Remember that I shared you some messages some stuff regarding .NET, but this is just for paragraph notes. I thought about just sanitizing it, cleaning it up, sending it in… Nikola Grcevski @ Grafana / OpenTelemetry 51:52 Yeah, yeah, I think so, yeah. I think that will help. I think it's on the right track, what we want to do.
**Pellared** 51:59 Okay, so yeah, so an action item to me is that, yeah, I will publish something there, hopefully end of this week.
**Tyler** 52:08 Perfect.
Okay, next up is the OTEL API SDK integration. This is something, I think, that hasn't been actively being worked on, but is, still on the goal.
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:20 Pardon, yeah.
Yeah, still, some stuff has been done. I think, But not everything. I'm still working on a bunch of these issues.
In the background.
Mainly, I mean, you know, at KubeCon, we had the discussion that, you know, we could augment a lot of this stuff.
For even SDKs when they don't actually have certain features.
not be able to maybe do it all automatically, but, But we'll see. I'm still working on this. A lot of stuff will come. I wanted to get the Go stuff out of the way. It's not tracked here, I don't know, maybe we did track it.
**Tyler** 53:02 the, you're talking about specifically, like, the unification of the Go, yeah. …handling? Yeah. Yeah, okay, yeah. Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 53:09 That's not tracked in here, but I think it's, it's a must if we want to, support everything for all languages.
I mean…
**Tyler** 53:20 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 53:21 Yeah, sort of like, Go used to be the best one we supported, now it's sort of the worst, because all the new features don't hit it, like payload extraction, none of that cool stuff.
So…
**Tyler** 53:33 That's… that's maybe a good point.
could you take this as an action item and just have… open an issue, and we can… we can backport this in? I think this is something that's always been on our list of goals, I just don't think we've identified it and, like, captured it here. Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 53:46 Capture it, yeah.
**Tyler** 53:47 Yeah, yeah, just… just so we, like, can visually, like, communicate to people that we're actively working on that as well, because I think that's important. It's gonna be really helpful, like you're saying. And I don't think it's discounted, because it's not some big, fancy feature. I think it's, like, important work, so, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 54:04 Yeah, I got context propagation to work, so that… that's good. I tested with various combinations.
go instrumented with the regular stuff, not instrumented, and this and that. It sort of works. Yeah. I'm gonna tackle HTTP next, HTLS next.
So once I add that, I think we should be really on par, and then it's about extracting the body from the existing one and passing it on through the larger buffers.
So, couple of things, but I'll write it all down, yeah.
**Tyler** 54:36 Cool. Awesome.
Okay.
Kind of last epic is this improved integration test quality?
I don't know if there's been too much work on this, I think I saw Steven on here. I don't think they've seen… sorry, that's not the right thing to say. There's been a lot of really great work on it, I just don't know if, the beast of the CI system is, is yielding yet, I guess is maybe a better way to say that.
**Stephen Lang** 55:01 Yeah, I think the… so the PR that I raised recently was not exactly part of this epic, because I think this epic is… is more Roberts that was tracking the refactoring around Doppler tests.
Whereas the PR that I put up was… Just, like, a generic report to try and get an idea for flaky tests.
**Tyler** 55:22 that and tackling flaky tests in general, but yeah, I think that… I guess you're more triaging, but I think it… so, I am excited about your thing, because you're also gonna help measure it, and I think that's gonna help us, like.
justify a lot of these refactors and seeing if, like, we can help stabilize this, so I think that's, like, extremely important, and it's really helpful if we start doing that now, as well as later, but yeah, so I'm really excited about that one.
Robert, I don't know if you wanted to also add anything on this?
**Pellared** 55:56 I use more time or sleep less.
**Tyler** 56:01 Anyways.
**Nikola Grcevski @ Grafana / OpenTelemetry** 56:01 I wanted to give praise. I mean, the change you made, Robert, to make the tests not use that custom build tag integration or whatever we had. That's been a lifesaver for me, because now I can, in Visual Studio Code, debug the tests, integration tests, and step through, rather than spend 5 hours tweaking whatever I've copy-pasted from another test.
That… that was massive.
That's extra.
**Pellared** 56:31 very good feedback, because I was not sure about the value of manufacture.
**Nikola Grcevski @ Grafana / OpenTelemetry** 56:35 it was massive. For me, it's been, like, now that I can go and hit run, because I think Mario used Go… this other Go editor from… The same company that makes IntelliJ? I don't know, what is it called? .
**Pellared** 56:50 rings.
**Nikola Grcevski @ Grafana / OpenTelemetry** 56:50 Goland. Yeah, I used Goland. For him, it always worked, but I think I always used VS Code, so for me, never did. But the other thing I wanted to say, while I was writing the new test, I noticed something that might actually help with his flakiness. I think we're… with, I think where a lot of our tests are doing, when they do require, they're passing the T of the function rather than on the sub.
when you do, like, require with eventually, I think there's a lot… there's a lot of bugs like that. So I got bit by that when I was writing a new test, and I was like, why is it not working? And then I was like, oh my god, I'm using the wrong T here, the wrong test.
testing, so I think this might be the reason why we have so much weightiness.
**Pellared** 57:39 Like, I think one of the reasons is also that it's using, like, Jaeger and stuff like that, which makes this very, as you know, so I think there are… but feel free to put it as comment or something, because probably if even someone would find time in either Cloud Code or Codex or anyone, probably it would be perfect to find and fix, though, kind of… Nikola Grcevski @ Grafana / OpenTelemetry 57:58 Yeah, I think so, yeah.
I'm gonna go myself and just kind of look over the tracing test, which is a lot of these fail, and I think there's a lot of mistakes like that. So I'm just gonna go and clean that up as well.
see if… I think it should help, because I had been down… the rabbit hole of analyzing some of these failures, and I always come up empty-handed. I'm like, everything in the logs says it should have worked, but it didn't work.
And same thing happened to me, I was writing this new test. It was like, the log says the right thing, but why is the test not finding it? And I spent a lot of time, and I realized, oh my god, it's supposed to loop, but it dies immediately, because the T up there never catches it, and whatever.
So it never actually tries multiple times. So if you don't get another the first time, we report the test as failing.
And in the logs, sure enough, like, a second later, the thing came out, and it should have been in there. So, it's, yeah.
So, fingers crossed, that solves a lot of this, so… Oops.
**Tyler** 59:07 Yeah, definitely, definitely some… some good stuff still… still to come there.
Okay, we are pretty much at time at this point, so we could stop on this one. If you have other things in the roadmap that, we didn't get to, which is a lot, and it's not correctly labeled as, actively in progress or something like that, please go ahead and update it. If you can. If you can't, ping me, and I can update it for you.
I think that we're doing a lot of really great work, and I just want to make sure it's captured, and we'll communicate these sort of things out.
But other than that, yeah, we are… actually right at time. So, with… I guess with that then, we can end the meeting here. Thanks everyone for joining, and I will see you all in a week's time, or asynchronously. Till then.
**Rafael Roquetto** 59:49 Thank you. Bye.
**Nikola Grcevski @ Grafana / OpenTelemetry** 59:50 Bye.

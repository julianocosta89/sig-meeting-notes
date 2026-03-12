SIG: Semantic Convention Tooling
Date: 2026-01-21
Duration: 51 minutes
Zoom Recording URL: https://zoom.us/rec/share/cOclMirzhuOxvgmeSbwZVj3dpkabqo1KD18xME50rsoasROoAWQWlhhe8F30zlOA.Z0j6S7FzqoliKaZM
============================================================

## Zoom Recording Transcript

**Josh Suereth** 01:21 Morning, folks.
**ariannavespri** 01:24 Hello.
**Josh Suereth** 01:25 Or afternoon.
**ariannavespri** 01:29 Afternoon, yes.
**Laurent Querel** 01:53 I only win.
**Jeremy Blythe** 01:56 Hello.
**Laurent Querel** 01:58 Who knows?
**ariannavespri** 01:59 So?
**Josh Suereth** 02:06 Oh, I was muted. I'm just filling out the schedule a little bit here. Let's, everybody fill out your names and add your agenda items, and we'll get started. Wait, whoa, whoa, what just happened?
How did everything get deleted?
Oh, I see.
Okay.
Ugh.
**Liudmila Molkova** 02:43 Hey, folks!
**Arthur Silva Sens** 02:49 Hello.
**Josh Suereth** 03:20 Okay.
Alright, is Arthur here yet?
**Arthur Silva Sens** 03:25 Yes, I am.
**Josh Suereth** 03:26 Alrighty.
I'm not looking at the thing. Oh, here we go, now I have picture-in-picture. I can see ya. Do you want to get started with, your question here?
**Arthur Silva Sens** 03:35 Yeah, Jeremy and I have been discussing on the PR about the… the right implementation that we want. I… the way I implemented the inference, comment.
is that we receive an OTLP message. There is no registry in this command at all.
And whatever we get from the message, it becomes a full schema.
Jeremy shared some feedback that his vision was more, like, infer is a subcommand of life check.
In live check, that means there is a flag that you provide a registry.
And then we compare the LTLP message with the registry provided in the flag, and we infer the differences. For example, we create a sub-registry.
That imports the parent registry.
I… This is a lot harder than I expected initially. I would be happy to work on this, but, like, I would need some help understanding.
**Josh Suereth** 04:46 Yeah.
**Jeremy Blythe** 04:46 Yeah, I guess I'm… I'm wondering what… as a team.
think of the idea, because I was just like, That was my… my… initial thought was, LiveCheck is… LifeCheck is already telling you things that are missing.
Maybe I want to respond to the things that are missing by adding them to my registry.
Right. That's the thought process.
**Josh Suereth** 05:12 Yeah, I'm… I'm a fan of walking before we run.
**Jeremy Blythe** 05:15 And also, I don't want to, like…
**Josh Suereth** 05:17 if you think about small composable pieces, I think what you're suggesting, Jeremy, would be a good extension.
Right? But, like, I think inferring initially is still useful on its own.
Like, basically, if I ask the question, is… What it does now.
problematic in some way, or bad? I think the answer's no. Like… maybe, Arthur, we could expand it to, like.
you are open for a certain window of time, or you get a command that tells you to quit, and so you can accept more than one OTLP batch to do infer. But, like, what you have now, I think, is a reasonable use case one, right?
And then I also see what you're talking about, Jeremy, where, like, you… you have a dependency.
Right? So you pick your dependencies and say, cool, I want to infer a registry with these dependencies, and LiveCheck would tell you the diff. I see that as an advanced use case.
Or, like, a thing we could build towards next.
Okay. But also, is it, like, I wouldn't call it live check.
Like, to me, LiveCheck is the thing that I run in my integration test.
to validate telemetry, or that, like, I think you want to give this a different name. And so it can use the live check engine, right? It can be part of the live check crate.
But I would give it a different name, because it's a different, like, use case. Like, Weaver's a bunch of small little tools, right? We expect people to call generate a couple times for different, like, code gen. They're gonna call it once to do markdown.
wants to do the, you know, Java or Go, or whatever, So, I would, I would see them doing the same, just, like, there would be an infer command that would be different than live check.
Where live check is limited to only, like, validation, and infer would do, like, LiveCheck++, where it could be, cool.
you give me a dependency, I'm gonna resolve things, and I will infer differences from that dependency, and tell you about problems with that dependency that you're not matching, right? That… that makes sense to me, but I would still call it an infer command, as opposed to trying to bundle it all into Live Check.
Even if it uses the same engine, and I think that could be a phase two, like a step two, you know what I mean? Like, we could start with, we don't handle dependencies in infer as a known limitation, and we can expand to handle dependencies Like, at… later.
**Jeremy Blythe** 07:49 It does, absolutely, it does. I just felt that there was a risk, like, if I'm capturing OTLP, And I'm making RPC calls, let's say.
I'm gonna have a bunch of RPC. things, which are fully defined very well in the hotel semconconf.
now my infer command is going to redefine RPC. and all the things, rather than referring to the hotel ones. So now I've got… so now I've been… what's been created for me is a definition that is redefining things that are in OTEL. So, that's fine, it just means that later on, when I want to depend on hotel.
and reuse those attributes, I'm gonna have to deal with, collisions that I've created. Which is okay, but I just… That's the first step, right? That was just my feeling.
**Liudmila Molkova** 08:43 We can be even smarter if you receive something that has schema URL.
And we should also check if schema URL is present. Then it becomes your dependency.
And if it doesn't, then who knows where it came from?
**Josh Suereth** 09:01 Yeah, yeah, that's super naive. I really like that, Linmilla.
Because that's not a hard algorithm to implement, I think.
**Laurent Querel** 09:13 So first, I like what, Joshua said. I think, definitively, for me, I see the use case of, For me, the basic use case is someone that never heard about Weaver.
Convention, I want to start Bumps clutch.
Definitively useful.
Again, registry info instead of registry life check. Makes sense. What you said, Being able to detect when something was… somewhat existing in the Sevente Convention. I think it's something that could happen even without the… for me, it's decorated from the infirm.
It's another thing.
The ability to detect if something has already been defined.
Somewhere?
And led the opportunity for the user to reuse it instead of reinventing it.
Looks like another function that we could create.
Because that could happen with any registry, especially with the BT registry scenario.
We could imagine two teams doing things, and because they are in the same company, they are using the same terminology, but with different description.
And that's something that could be useful to have as a command, independent of the infer.
That could be also applied in the use case that we just, we just described.
**Arthur Silva Sens** 10:58 Okay, I really like where this is going, because it makes it easier, a little bit easier on my side.
And also, because… I like that… there is future work, so I can continue to improve my breast.
For this PR specifically, then… what… what I would need to take care is make… make sure that whatever I implement Can be expanded in the future, and it's not something that goes completely against the future plans.
**Jeremy Blythe** 11:36 Yeah, I think what you've done so far, don't get me wrong, I think it's great. I just, want to make sure we're heading in the right… we're heading down the right path.
So, sounds like the consensus is that we are.
there were a couple of notes in there, I think I tagged… I think I tagged you, Lamilla, or Josh? I had a question about span event, and this is my ignorance. Is span event also event?
**Liudmila Molkova** 12:00 Let's kill them. They are being deprecated, we have not merged.
**Jeremy Blythe** 12:06 Okay.
So a span event is not an event.
**Josh Suereth** 12:10 A spend event, like, if you see one.
Infer an event, and get people to move over to an event.
We could even issue a warning saying, hey, like, events are going away, you should move to… You should move… spend events are going away, you should move to event.
**Jeremy Blythe** 12:27 Right, I think that's what Arthur's done, right? So when you see a span event, you're inferring an event.
**Arthur Silva Sens** 12:31 Yeah. Two.
**Jeremy Blythe** 12:32 you've done… so, that's correct. But in live check.
I'm not checking the span event is an event.
**Liudmila Molkova** 12:42 That's…
**Jeremy Blythe** 12:43 Oh, I'm doing something.
**Liudmila Molkova** 12:44 of the spec yet, it's not deprecated just yet, so we should get there, but yeah, that's a great point.
I feel like the new features we make shouldn't care much about span events.
And realistically, we don't even have means to… define span events in semantic conventions. We define them as events.
And we add this… the events section under spend, but this part we should not do. We shouldn't add them under the spend.
**Jeremy Blythe** 13:18 Right.
**Arthur Silva Sens** 13:19 Another question is about entities, if we should be inferring entities, or we should wait for… I don't know how stable they are right now.
**Josh Suereth** 13:33 We're… we're trying… yeah.
I think if you see it in the protocol, it'd be okay to infer it. We can't actually generate them yet, because the specification and SDK work hasn't landed.
They're still… it's still held up in, like, code review. So, Yeah, if you… if you defer entity inference and just put a to-do, I think that's fine.
Right? Like, again, I think we should take the same approach we did live check. So, like, Infer, we should call it, like, an alpha feature or a beta feature. Take what you have, let people try it out, get feedback, get bug reports, and evolve over time. So, like, to Jeremy's concern around, you know.
this might infer things that are already part of SEMCOM, and your dependencies will be wrong. Let's just call that out in the docs about it, you know what I mean? Like, just say, hey, this is available.
here's some use cases where it works really well, try it out, here's things that we know aren't working, and we'll fix them, right? Like, I think that's the approach I'd like to take here.
So… I don't remember, I think in V2, when you call dash dash v2, we issue a warning that says this is, like, an unstable feature.
We could probably do that for your future, and then you have carte blanche to basically implement pieces, make it as useful as possible, and some of these hard decisions we can defer and fix them later, and as people try it and, like, make requests, we can prioritize what to fix over time. You know what I mean?
So, I like that going forward. Like, let's put it… let's have this output some sort of flag that says, you know, this is a, experimental feature. And then, let people open up tickets, and some of these hard questions, if you wanted to, like, avoid inferring entity for now, cool, put a to-do, right?
We can open a ticket that says, implement entity inference for Weaver and fur, and if people thumbs up it, we can prioritize it.
**Arthur Silva Sens** 15:41 Sounds good to me.
**Josh Suereth** 15:43 Cool.
Really exciting stuff, man.
**Jeremy Blythe** 15:48 Yeah, it's really cool. I like that you, you've used it already, and… like, accelerated one of your PRs. It sounds… that's pretty awesome.
**Arthur Silva Sens** 15:57 Yeah, I was postponing that PR forever, and that info really helped.
**Jeremy Blythe** 16:03 That's excellent.
**Josh Suereth** 16:05 That's awesome.
Cool.
So, I want to talk about, out-of-the-box defaults for Weaver, if that's alright.
this is related to Federation. We have a slot with, Jurassi's podcast called Telemetry Drops to talk about Weaver, and we want to start advertising to the rest of the hotel community that we're ready for people to kind of create Their de facto, template things, and I want to get a set of instructions for how they would do that, and I'd like to have that set of instructions kind of written up shortly. My thinking is… we… this… We want to allow out-of-the-box defaults, and I'll get into the proposal, but in terms of onboarding templates, we would ask people to design templates against the V2 schema.
and put them in this registry, and then that is what we'll include in Weaver going forward.
We would not have the templates, like, support both V1 and V2, we'd ask them to just support V2, and we'll document that case, and we'll implement this thing over time. There… we can document… so I can write a document for how to write a V2 template, how to put it into a GitHub repo, and how to reference it, because all of that works today.
Right? There's no… there's nothing that blocks people from writing these… these out-of-the-box templates. What's missing, though, is then, once they're built, how do we make it easy in Weaver?
So… let's just go through some of the issues and concerns here, and I want to hear feedback. First of all, did everyone read this, or should I walk through it quick?
**Jeremy Blythe** 17:59 I'm in 3 at once.
**Josh Suereth** 18:01 Okay.
I'll walk briefly through it. It's basically 3 pieces.
First, the requirements and goals, because this is the important thing for us to agree on.
We want to make sure that people who are writing language policy or documentation Generation are able to contribute independently of Weaver releases, and cut releases, and that sort of thing, right? We don't want to force them to kind of understand Rust, necessarily.
That's the whole idea behind the Open Extension.
we want… that means they need a stable version of Weaver to work against, so if we make a breaking change on main by accident that we didn't release, they're not broken. So we can incrementally do things, we can, you know, make deprecations and that kind of stuff.
They need to be able to test and verify their templates, and they can release independently. Next is Weaver can decide what versions of templates and policies are to pull in by default. So, if the template registry adds a new thing.
That is somewhat experimental.
and they have, like, an alpha phase, Weaver can say, cool, we only depend on, like, the stable things, if we want.
In, like, an out-of-the-box Weaver distribution.
Okay?
We can talk about what that means, but that's the idea behind this.
We need some kind of smoke test to make sure that, like, whatever features and capabilities we have to pull in this registry works on every commit, so we don't break it over time, and then we need to update our release So that we can bundle these in some way.
Either in the executable, in the docker, or we have, like, a zip-based distribution, like, something, okay?
Cool.
So, the other thing is, we want Weaver users can override the out-of-the-box templates.
And out-of-the-box templates can be referred to by simple names, similar to how the out-of-the-box ANSI one works today, where you just say, I want my diagnostics to be an ANSI or GitHub issue format, where, like, if it's in a GitHub action, it'll open the GitHub note on, like, a file line thing, right?
That's, we want… we want those.
Okay.
So, the proposal's three pieces. One is, we need to expand how we do virtual directory to actually, support Or prevent supply chain attacks?
So, right now, we just download whatever file's there, but we don't do any verification whatsoever. So, the proposal's basically, let's add some verification steps to the files we download, and give people capabilities around that verification.
So for GitHub, we don't support referencing a specific commit, but as you know, in, if you use Renovate, that's, like, a very important thing, is to refer to specific commits as opposed to tags, and that sort of thing, so… or just downloading main.
So that's step one. There's also, for zips, I think we should actually support, looking, at least, for signatures, signature files, and validating against a signature.
Yeah. Okay. The next thing is, we want to create a OpenTelemetry Weaver Templates repository, which, if we agree in this meeting, I will open an issue right now to create that, because I think this makes sense to do no matter what.
We create a repository there, we'll add instructions for how to contribute, for what to contribute, and we'll set up a new set of code owners and things, where when people want to contribute, we bring them in as a code owner of a directory for their you know, language or whatever. And we'd see this with ourselves, and start from that process. And lastly, we want to update our release process now to pull in these default templates. So I want to have a configuration file, personally, so that this is clearly controlled.
and very clear what we're pulling into the default for Weaver, where it'll have, like, links out to say, we're pulling in this template, this template, this template, and here's the name that users resolve it by.
As opposed to… there was a proposal to have conventions, we'll talk through that.
We update our build process to grab and cache these in some fashion for Weaver itself, so that we can run tests with these defaults and that sort of thing. And then we want to include some kind of manifest on release of what, like, our build of materials, if you will. This is, again, about supply chain.
Okay.
So, then I get into details about specifics. We can talk about this, you know, these are, like, just requirements. The idea behind the template repository, is I'm thinking of a, you know, name slash sla- name… type slash Specific name?
format here.
So, we would have a set of types of things, like code gen, checks, where checks… I need to figure out how to differentiate live check from just, like.
overall resolution checks. I think we want a term for that. I was using advice versus checks, but I don't like that.
Because live check could be a real check, or could be advice.
Like, it could be this is a failure, or this could just be a warning, or sorry, an informational.
Anyway, and then diagnostics is the diagnostic output, right?
Oh, go ahead. There's someone talking?
**Liudmila Molkova** 23:47 Yeah, I was just going to suggest something stupid, like schema check and telemetry check.
**Josh Suereth** 23:53 Yeah, that, that, that's fine, too. Yeah. Again.
Feel free to put that on the thing, because I'm not going to remember.
Or comments on the PR?
what's important to me is the shape and the names we can figure out the right name for. So if we agree that it's like a, you know, a thing slash thing, I feel like this gives us a lot of flexibility.
not super complicated for people, but still more complicated than just saying ANSI, right?
Okay.
So then, inside of the Weaver release process, we just make a config file. I'm using YAML, I don't care if it's YAML, I don't care what the config file is. The important part is the config file has, these… these names kind of split. We… we actually… I'm splitting the three things that we import.
As the policies we import, where it'd be check slash semconf would be, like, the String that you would use, and this is where we find it and load it.
You know, for template, the template argument, it'd be code gen slash java, doc slash markdown, but this is the structure we'd have, so we can just write down what we need to include, and we can expand this over time, and I think it'd be easy for people to contribute to this file and read it, so they understand what the hell they're doing, if, like, a template author adds a new thing and wants to have it baked in by default. The thing I'm not… super comfortable with is, you know, this has to be a get SHA, so we will have to do verification that that SHA is a tag that corresponds to release. It's not too hard, it's just a little annoying.
And the other part would be, I would love if we could have Renovate.
Understand this file, and automatically suggest version bumps when the template releases.
That's… a TBD. Like, we'll see if we can figure that out.
I think that's a reasonable thing to do, and that's something we could do in the future. So imagine we have this file in Weaver, imagine we have renovate… like, this is the future, right? We have Renovate set up, so it automatically bumps these versions on major releases of things, and then Weaver's build process knows how to bake this in by default, so you have no downloads.
Unless you opt into a download by referencing a remote URL when you specify your template, or whatever, in your Weaver command.
Okay.
I did a lot of talking.
Oh, the… this whole process, build process of this.
This is just a proposal for how we hide it in Rust, so we can change the implementation details of it. Inside of Rust, you would call these three methods anytime you want to access one of the built-in things. And so, we can change how we build it in. If we want to put it in the executable, great. If we want to look it up on the file system, great, because we're returning results of errors.
You can fail to find the default, we'll have to deal with that in Weaver in some way, but I think this makes a lot of sense.
Okay, cool.
Feedback, thoughts, comments?
I'm gonna switch over to… the notes, so I can take notes.
**Liudmila Molkova** 27:07 Okay, I'll start, let's do it. I really like the proposal of separating the templates into a common repo.
That can be shared.
there are some defaults that we've, I think, will need to be baked in.
But in general, it makes total sense to me. I think there is a lot of details that we'll need to figure out, right? Like, best practices, reusability, and whatnot, and I would hate to read a lot of ginger code, but, that's fine.
I think we will figure that out.
**Jeremy Blythe** 27:47 I like it too.
Kind of adjacent to this. I was looking at… there was a… there's an issue… where there's a request for Jason L.
as output for… from LiveCheck.
**Josh Suereth** 28:02 And then…
**Jeremy Blythe** 28:04 I was thinking… I've got some code. I'll put it in a PR so we can comment on it, but I think there's a common… output.
problem where I don't want a template just to put double braces around it and have Mini Ginger go through a template processor just to make JSON for me, when Sirday does that.
And it can make YAML, and it can make JSONL, and I don't need the template engine for that. So I've kind of… I've done some code that puts that in an enum.
Where template is one of your options for outputs. Anyway… And I think that solves problems we've seen with, like, weird escaping, and YAML getting screwed up, and it, like, the template engine, like, reorganizing the tags and stuff like that, where, really, it's not a templated output, it's just one of the standard, like, serialized outputs, right?
But I'll put my PR up and then… See what you think.
That's kind of a decent one.
**Josh Suereth** 29:05 What's be offensive there, Jeremy. I hope you don't mind this option I added.
**Jeremy Blythe** 29:09 XML. Yeah. No, I agree with what you're saying, like, that makes a lot of sense of.
**Josh Suereth** 29:17 like, template is an output type, and if you specify a template, great. But, like, maybe if you're just dumping to JSON, why are we firing this through?
**Jeremy Blythe** 29:27 Right?
**Josh Suereth** 29:28 So, like, yeah, why are we firing it through Jinja? That's just a lot of potential failure, yeah.
**Jeremy Blythe** 29:33 And there's this long-standing issue that those templates are the code that they make is designed to be embedded in an HTML page. Like, that's the point of mini ginger. So it's all escaped as if you're putting your JSON in an HTML page.
**Josh Suereth** 29:48 Yep.
**Jeremy Blythe** 29:49 And… you're… Almost always not.
when you're doing a JSON output or a YAML output, you just want the thing, so… Yeah.
Escapes, and… anyway.
**Josh Suereth** 30:01 We have a bug from Ludmila from a long time ago that I could never figure out, and I think that's probably what it was.
**Jeremy Blythe** 30:06 That's exactly what it's doing, yeah. It's making YAML that you can put in a web page.
**Josh Suereth** 30:11 That's… yeah.
Oh yeah, I forgot to put YAML here.
That's more important than XML, you know?
What are other… well, anyway.
Like, we already have, what, 1, 2, 3… we have two that we know people use, which is JSON, YAML, and Template. So, Template being the one that exists now. So, I feel like that absolutely makes sense as a thing to do. I think you can do this independently of my proposal as well.
Right? That seems like a thing you could just… you could just do across Weaver.
**Jeremy Blythe** 30:42 Yeah, 100%.
Cool. But I think it goes… Sorry, I'm going off topic, but I think it goes in line with other things we've been talking about, making the configuration interface better, where, like.
any of these things output stuff, like infer outputs things, live check, everything outputs stuff. And so, if we make the command line consistent for out… for outputting, and it goes to an object, it's like an output processor that does all of that stuff.
We have an opportunity to realign how you describe how you want your output.
and process it in a very consistent way across all of Weaver, I think.
Anyway, sorry, that's an aside, really.
**Josh Suereth** 31:22 I… I like it, though. Go ahead, Lauren.
**Laurent Querel** 31:26 Yeah, I like the proposal.
A few things, the open telemetry-river-templates.
Why naming this, repository, slash templates, dash templates, and why not artifact or something more general?
Because here, we don't necessarily have only templates, we have policies.
We have expression, GQ expression, and so on.
**Josh Suereth** 31:54 Yeah, we have JQ and… I don't see his… Is this the right name? The other… the other option is to call it packages. I…
**Laurent Querel** 32:04 That's… yes.
**Josh Suereth** 32:05 Or extensions, yeah, I don't care about the name so much as the existence of this thing, and I agree with.
**Laurent Querel** 32:12 For sure, me too.
**Josh Suereth** 32:13 I immediately… I think… so from a marketing perspective, we want people to write templates more than anything else, even though we're gonna put policies there.
But I agree with you. When I made the name, I'm like, okay, this doesn't really encompass the mission, but at this point, I don't care. I wanted to finish this proposal in under 10 minutes, because I didn't have enough time to write more.
**Laurent Querel** 32:35 No, that's perfectly fine. I was just thinking that maybe we can find a better name, but I definitely would agree that the proposal is much more important, and the idea behind it also. The second part of my feedback is, I'm not entirely convinced that we need to put the… The default, artifacts, packages, Into this repository.
Because that will force us to… so first, when we will review them, why do we have to go into a different repository?
For me, it's more the contribib side.
done by other people more than the ones that are fundamental for the way that wever is working. For example, all those, GZON and C, DH, DH, I would put style, stuff.
I can understand the benefits of having them into the contrib repo as an example, but that, adds to us, some additional, Gymnastic to go to a different, repository to add some additional check that will not be necessary if they stand into the same repository as we were.
**Josh Suereth** 34:04 So, yeah, I'm going to respond to that subscription to our DevSky. There's a second thing I want to add, which is, Martin, who's not… I don't think he's here, has comments about… Just using that convention. So Martin had a comment about, we could just have a convention where if you specify, like, name slash whatever for your template or your Ricoh policy or something, we know to go to that repository to look?
And so we don't have to hard-code anything.
But this goes into, like, I have two concerns. One is supply chain concern, and to you, specifically to answer this thing, I actually think forcing a hard line gives us one good value, which is we can't cheat our APIs anymore. So, if we want to have open extension.
We want to have the violation, or the finding that we have, right, be usable as both a GitHub action, or an ANSI output, or a text output, right? What this does is it forces us to think about that API, because there is friction.
Because when we want to render it as a GitHub, you know, comment that links to a line of code.
We have to do that in a separate repo. So we have to think about the API of what we expose more in Weber.
Because there's that jump of somewhere else, right? And we have to think about not breaking it, because we don't own all the templates that people use and say, oh, well, no one writes their own temp. Like, it forces us to make that API good. So if we think it's a valid extension point to keep.
I think having the extent… having, like, some of the defaults be somewhere else… there's a value to it. Now, there's a limited value, and we have to decide, you know, how much lives elsewhere, how much lives locally, because I agree with you, it will cause friction. It's just… In my mind, it's intended friction.
Right? Like, some of this, I think, is on purpose.
**Laurent Querel** 36:04 all the output for the errors, for the standard output that we use, I mean.
we expect to get them… they are there, because otherwise that will force us to do some additional modification into either And I'm not sure that the value that you are expressing is really exercised with the default one, because anyway, you will add into the the GitHub workflow, some way to capture them, put them locally, and then we can build a Docker image, or we can build the unbeiled version into the executable.
that will not make a big difference, because that's not the same way to capture an external contribute for a standard user in standard templates versus the ones that are used internally. For me, it's two different paths, so the value is not validated.
In some way, that you're… the value, at least, that you… you were… Expressing, in my opinion.
**Josh Suereth** 37:08 Gotcha. So, I think that… I'll take a… let's make a decision about… Which… defaults.
Stay, and which… Move.
And which we just dropped.
Because I think Lyudmila actually raised this about there's some defaults we should just not have anymore that aren't providing any value. But yeah, I agree with… what I was trying to get at is I think there's a, there's a continuum here. There's pros to having them out, there's pros to having it in the same thing, and so… like, I… when I… when I make proposals, I usually take a hard line to figure out where the middle is.
Let's figure out where the middle is.
So if you have a proposal of, like, you want to go through the list, I should… I can add this to the proposal of, here's a list of all the known defaults, as… right now, I just mentioned them briefly, but I didn't actually list out, here's the things that are included.
We can do that and say, this moves, this doesn't, and do, like, a checkbox. That makes a lot of sense to do. Go ahead, Lamila.
**Liudmila Molkova** 38:14 On this note, the… I think… the first point, there are things that are essential, they will be pulled in regardless if anybody uses them. For example, the error templates.
And they could live and waiver, honestly!
I have a hard time imagining somebody overriding the defaults for the Weaver errors.
Like, why would we even need it to make it configurable, extendable? But anyway, there are things like quad generation. Do we want to make every template for quad generation in Weaver?
we… we don't do this today, and we feel comfortable with it. We don't really review what language SIGs do with the code generation.
like, if we, reference in any way bacon, or just weak reference to… some external repo. I think it makes sense, it doesn't change anything in our current process.
And maybe we can kind of use the principle that if it's part of the river, if it doesn't really make sense to… usually to change it.
So let's… let's keep it… just in Weaver. If it's something that people normally would extend.
Let's keep it separately.
**Josh Suereth** 39:39 Okay.
I think that's the right principle there, in terms of whether or not to keep this code in Weaver or not.
one of the goals behind this defaults crate is that we can hide whether or not we have it locally, right? So, if we wanted to say, cool, In the config file, we could say cache equals true, or embed equals true. If embed's true, we embed it into the Rust binary. If cache is true, we include it as a directory beside the, binary, or in the Docker image. So it's, like, part of the Docker image, there's a cache of what it was, and if you don't have that, it just means you get the fast string reference, but we will resolve it remotely.
So this is how Weaver knows what the strings mean, and which repository to go to. And the repository doesn't have to be in Weaver.
To show up in our distribution.
It's, like, fully generic. Don't have to do that, we can just do this by convention, right?
But it… I think the hardest question here is, in my mind, you know, what belongs in Weaver as a distribution, and what should Weaver do with the internet. Like, what should the weaver experience if you disable the internet to it be?
you know, if I download a distribution of Weaver, what is my out-of-the-box behavior?
I wanted to design something where we can evolve that over time. So if initially, what this thing does is it doesn't cache anything locally.
And it always resolves, remotely, these out-of-the-box templates. That could be step one.
Then we get user complaints saying, hey.
I want to use Weaver, not in the internet, and I'm referencing this Java thing that keeps trying to download it. How do I… we could be like, cool, let's figure out how to get in the distribution, right? But we can evolve.
Because we have an abstraction between how Weaver interacts with defaults.
and how they're configured. And we can expand that crate to do more over time, You know, and again.
I… what I don't want, is I don't want every frickin' template embedded in Weber.
That was the main… main reason I made this proposal.
That would be an insane binary.
**Laurent Querel** 41:53 Yeah, but that's why we created this dash dash template with a virtual directory to be able to direct or to point to something that was external. It was following a discussion with Martin, by the way, during KubeCon last year.
So that is… perfectly fine for me. The fact that we want to move diagnostic templates outside of Weaver, not sure that makes sense for me.
But, but it's a very small thing, for this big picture that you are describing.
**Josh Suereth** 42:29 Okay, we'll see. I guess what I'll say is, if you think about Weaver, right, and if I say, you know, Weaver Generate templates, and I say CodeGen slash Java, that feels like Weaver has it out of the box.
Even if we're downloading from a remote repo.
So, that's… that's kind of what I'm going after here.
**Laurent Querel** 42:51 Yeah, true.
**Josh Suereth** 42:52 Yes.
Go ahead, Jeremy, you had your hand up.
**Jeremy Blythe** 42:56 One of the things… so it feels a bit like this would be… A library where you can go and pick things that you want.
So, I could go to… Weaver templates, and I can go and get what I want from there.
when it comes to policies, one of the things I think we should support that we don't.
is that I want more than one of the policies from This policy… from this library of policies that's been made.
So one thing we don't support at the moment is, if you want to add to, like… I want all of the OTEL policies, plus some other things, I've got to copy and paste that, make my own rego files, and then do that.
**Josh Suereth** 43:43 You can reference policies more than once. So you can actually… you can specify the command more than once, and you can have… you can say, I want to refer to the hotel policies, and I want to refer to my directory policies.
And it will pull them both in and merge them all together.
**Jeremy Blythe** 44:00 Okay, I didn't know. Don't think I've… I haven't implemented it that way in LifeCheck, so that's a thing.
**Josh Suereth** 44:06 Yeah, I would take a look at registry generate, because there's an add policies function, and the argument is repeated, and since the argument's repeated with virtual directory refs, you should be able to add policies from multiple remote extension points.
**Jeremy Blythe** 44:22 Okay, but, I guess… okay, that's, like, a thing, but the… the concept is… will the concept feel like, for some of these things, that I've got a library of stuff that I can go and pull multiple things from?
Or am I set to just one set of things?
**Josh Suereth** 44:39 Yeah, it's supposed to feel like you can just pull. So, like, the idea… the idea here is we're gonna lean into the virtual directory ref thing.
**Jeremy Blythe** 44:46 Policies gets interesting, right? Because.
**Josh Suereth** 44:50 We still have to figure out what to do with a default inclusion of a policy. Right now, we default include some policies, if I recall correctly.
But how do I override the behavior to say, no, don't include anything by default, only use the ones I've specified? And here's the 5.
You know, that's something that I do think we need to sort out. But this should feel like I have a policies argument that says, you know, O tell Semcov, you know, my custom Prometheus policies, cool, or, like, this GitHub URL, this hash, this directory.
And I can have all 3 of those get pulled in together.
And I think that makes sense. For templates, again, because the way… the way… we can talk about this later, too, but the way we regenerate works, it's not a repeated field, so you'd have to call it multiple times, right? You'd say we regenerate docs slash markdown, docs slash HTML, CodeGen Go, CodeGen Python, you know? And I'd have to make 4 calls or 5 calls for that.
But I do think, if it helps, what I can do on the proposal, we do this at work, is we write what we call the user guide, which is just the documentation. So I'll write the documentation as if we had launched a feature of how you use Weaver.
And I can put that as, like, an example of, like, where we want it… what we want Weaver to look like in terms of usage, and then we can evaluate it that way. Because I feel like that's the important part. How will… how will users use this? Yeah.
**Jeremy Blythe** 46:28 Yeah, yeah.
**Josh Suereth** 46:30 Okay. Write the release note first.
Cool.
Any other questions there?
Unfortunately.
**Jeremy Blythe** 46:42 I'm gonna have to drop, sorry.
**Josh Suereth** 46:43 Dropped, yeah.
**Jeremy Blythe** 46:45 I have to go, early, so… Okay.
**Josh Suereth** 46:48 I think… I think we might take this offline, unless… Lauren, did you have a chance to look at Lyudmila's, comments here?
**Laurent Querel** 46:58 Not yet, unfortunately.
But, I will, I guess it's related to the section I wrote. Yeah, I will, I will look at that and answer the comment, probably today.
**Josh Suereth** 47:15 Yeah, this… for context, I think what Lumila's pushing for, because she mentioned this on my PR, is we talk about having a manifest and a resolve schema.
we're talking about moving the manifest into the resolve schema. So, the resolve schema and the manifest might be the same thing, or they might be separate.
Okay. And that's, that's like a thing we have to figure out. I think Ludmila wants to be able to reference, the resolve schema directly and have enough information in there that you don't need to go look for a manifest.
But… I… I have concerns with that, and I think we need to talk through that. So I think this is a discussion I think will take another 30 minutes, and probably we can talk about it next time.
And yeah, but please, please take a look at these, because I think she made a bunch of, comments. I think this, this is more, We need to get this sorted out, because the next PR I plan to write for Weaver is the resolving a Resolved Registry, and we need to figure out if I look for manifest and then resolved registry, or if I look for the Resolve Registry specifically directly first.
**Laurent Querel** 48:22 Amy.
**Josh Suereth** 48:23 And I, you know, initially I was thinking of doing the latter, not the former.
And once that's implemented, that is… it's changeable, but it's more annoying, you know?
Yeah. Don't want to waste effort. Okay, cool. So let's talk about that.
Do you have anything you wanted to talk about or ask before we call it?
**ariannavespri** 48:43 You know, I was, just, listening. I started working on one of the things that you assigned to me, but, you know, it's been a busy week, and, you know, as soon as I've got something, I'm gonna ping you. And, thank you so much.
**Josh Suereth** 48:57 If you have any questions or anything, just let us know. Absolutely. I'll also briefly mention, we have a… we have a docs agent that I've been trying out, and if you see it doing shenanigans.
Just yell at it, because… I told it to only update box code, and it keeps writing code instead of docs.
**ariannavespri** 49:17 Good to know.
**Josh Suereth** 49:18 Yeah, so… Anyway, just word of warning, if you see any conflicts from that thing or whatever, let us know.
**ariannavespri** 49:25 Okay, thank you.
**Josh Suereth** 49:27 Okay, alright. And Laurent, there's another docs PR to review, if you want to take a look at it from the agent.
**Laurent Querel** 49:33 But I had to…
**Josh Suereth** 49:34 I had to get it to write it twice, because it tried to change all of our code, and it's from an issue that you opened Three years ago? 2 years ago?
**Laurent Querel** 49:43 Okay.
**Josh Suereth** 49:44 out.
**Laurent Querel** 49:45 Which, which number for the PR?
**Josh Suereth** 49:48 Good question.
It's still in draft. It is 11.48.
**Laurent Querel** 49:58 1128.
**Josh Suereth** 50:00 It's real tiny now.
**Laurent Querel** 50:05 Okay.
**Josh Suereth** 50:07 Yep.
So, the issue… the issue was the one about adding, in all of our examples, a comment that says that this is generated code.
And, like, you know, where to find documentation on Jinja syntax and that kind of stuff.
**Laurent Querel** 50:21 Oh, yes, yes, yes, yes.
**Josh Suereth** 50:22 So…
**Laurent Querel** 50:23 Bill.
**Josh Suereth** 50:24 what I've been doing is I, like, all our issues are marked, like, good first issue, code, documentation, that sort of thing. Anything that's listed as docs, I'm feeding to the docs agent if I think it's small enough that it could handle it.
And seeing how it goes.
But that's the latest one. So, I think we only have 3 left after this. 2 of which I don't think the agent can do.
**Laurent Querel** 50:46 Okay.
Okay, great. Yeah, I will look at that also.
**Josh Suereth** 50:51 Lots of.
**Laurent Querel** 50:51 the dish. Yeah, thank you.
**Josh Suereth** 50:53 Alright, thanks, everybody. We'll see ya.
**ariannavespri** 50:56 Bye, bye-bye. Bye.

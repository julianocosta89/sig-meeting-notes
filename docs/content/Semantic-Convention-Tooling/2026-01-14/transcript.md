SIG: Semantic Convention Tooling
Date: 2026-01-14
Duration: 65 minutes
Zoom Recording URL: https://zoom.us/rec/share/Mmm47v7NQLQ9FLRsWj0pRkbxNWEfVH8Yo3ovKaUnA7D_jW2AlwCqN2hBTgxQdGht.l4LkQc-_2IRuwPdj
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:00:14 Hi, folks.
ariannavespri 00:00:19 Hello?
Arthur Silva Sens 00:00:23 Hello!
Liudmila Molkova 00:00:27 Arthur, your… learning crust and hating it. Did I get it right?
Arthur Silva Sens 00:00:34 I… I used to hate… oh my god.
I… I used to hate more.
I'm hating less and less as I… as I learn.
Liudmila Molkova 00:00:48 Hmm.
Arthur Silva Sens 00:00:49 But the beginning was terrible.
Liudmila Molkova 00:00:54 You probably should read your book, because I… I… I still hate it.
Arthur Silva Sens 00:01:02 I'm now learning traits.
Whatever that is.
Liudmila Molkova 00:01:11 The syntax is so dense.
Like… So many characters.
Arthur Silva Sens 00:01:18 Yeah.
Liudmila Molkova 00:01:25 Hi, Josh.
Josh Suereth 00:01:28 Hey!
Arthur Silva Sens 00:01:29 Hello.
Josh Suereth 00:01:30 So, my… my conflict with the last 30 got canceled, so we can… I don't have to make a request to change the… Oh, hold on, my camera's.
Liudmila Molkova 00:01:40 I'll need to drop after 30 minutes.
Josh Suereth 00:01:43 Alright, well then, I still want to talk about things, but did you see my topic? Because it's related to yours.
Liudmila Molkova 00:01:50 No, I haven't.
Josh Suereth 00:01:52 Alright, let's, let's, let's jump in, because we have a lot to discuss this week.
let's start with your topic, but I'm just gonna caveat that I have… Started changing the resolution algorithm.
And in doing so, there was a lot of cleanup that had to happen.
We have a very inconsistent set of Rust types to denote a… a resource, or sorry, a schema. And so, actually, the file formats aren't even frickin' visible when you resolve, initially.
So what I have set up… is… the manifest file that is Weaver.
will… will be the schema file that you're defining in your OTEP.
So, you know how you have the schema file that has, like, a URL to where you go? Okay, so when you give Weaver a URI, It's gonna be the directory where you expect that manifest to exist.
Or the manifest itself.
And then, we use the manifest to understand if there is a resolve schema, and then we'll look at the resolve schema.
And that's where this version would come in.
So, the file form… I still think we need the file format, like you're saying here, but there's this… this meta issue where, like, we'll have the manifest in the middle.
And so the question I have is, should the manifest tell you the version of the schema or not? Like… Or should the manifest just, like, point at a resolved schema file?
Liudmila Molkova 00:03:35 I liked your suggestion that we have a version inside each file, right?
Josh Suereth 00:03:42 Yeah.
Liudmila Molkova 00:03:43 Just more, more ways to evolve.
Or we will need the major version bump every file, essentially, when we major version bump the manifest, if ever.
Josh Suereth 00:03:57 Yeah, that's… that's a good point. Okay, alright, let's, with that, with that said, I've made a, like, your, specifically your PR, given the changes I'm making to Resolved, we're gonna have huge, major conflicts, so, I would ask if you could just not… not make changes to the existing stuff until after the new resolution now goes through, because I had to touch.
Liudmila Molkova 00:04:19 Okay.
Josh Suereth 00:04:20 Almost everything.
Ian Weaver… Weaver SemConv, Weaver Resolved Registry, and Weaver Resolver. So all the, like, the initial ecosystem, I had to… It was unfortunate, but we'll… we'll talk more.
Liudmila Molkova 00:04:35 It's okay.
Josh Suereth 00:04:36 Okay, cool. Yeah, go ahead. You wanna… you wanna talk about the schema thing?
Liudmila Molkova 00:04:42 Yeah, I just wanted to share… the summary of how I think we should do it. I think we should rename it to File Format from Version, because version is ambiguous, and here is how the different formats look like.
It would probably be somewhat painful to keep in mind that we need to update the minor version when we, let's say, add something to the schema.
And I think what we can do, we can, have a CI check, I don't know, just dump the JSON schema, and if there are changes, I don't know, ILCI, or… we can figure it out, but we need CI check if we do this.
Otherwise, we will forget to update versions. I think we need to follow SEMBER, even if it's painful, because if we introduce alternative sambware, it will suck.
Josh Suereth 00:05:34 I 100% agreed. Is there… so, in my PR, I actually started… I didn't make it file format, but I started doing this and all the files consistently, but I have it converted.
So I have resolved slash version, manifest slash version, right? Well, I don't have manifest, because I actually used a sem… but whatever. Materialized slash, right? Yeah.
Liudmila Molkova 00:05:56 Your, your format is fine as well.
Josh Suereth 00:05:59 Okay, the important here is the SEMCOM, which I'm 100% on board with. I think Arthur actually added a SEMVER dependency in a PR that I think we could use here.
So, yeah, I think this works really well.
Liudmila Molkova 00:06:14 Cool. Then, a couple of other small things, in case anybody has, thoughts.
So, I think we should have the schema URL everywhere, that points to the manifest in these files. It's optional.
But… I don't know, I propose to remove… we have registry URL and registry ID, I think it's the source where we got the registry.
So, Rob.
I…
Josh Suereth 00:06:48 Yeah, no, okay. This, this one, this one specifically is somewhat… this, this, these are important for dependencies.
Liudmila Molkova 00:06:57 Oh, why?
Josh Suereth 00:06:59 Yeah, so I need to untangle everywhere where it is. Registry ID is how we identify a dependency and determine if you have a loop.
So, if somebody depends on OTEL SEMCOM version 1, and someone depends on OTel SemComf version 2, they're in conflict, and you have to resolve them. And you have to make sure you only pull in one version of OTelSemComf, if you have, like, that diamond pane.
Liudmila Molkova 00:07:25 So…
Josh Suereth 00:07:26 we want to name our registries so that we… like, think of it like a depend… a dependency in any kind of, like, packaging system. We need to… Go ahead.
Liudmila Molkova 00:07:37 Isn't it the same as schema URL? It also identifies the… it identifies the specific version of the registry.
Josh Suereth 00:07:44 Yeah, the… We could… we could move to schema URL as well.
instead of registry URL, I agree this should probably be schema URL. The only caveat I have, and I need to look into the details, if I'm resolving a raw registry, where it's just the raw definition, the schema URL and its location won't be the same thing.
Laurent Querel 00:08:06 Yes.
I think that that's, I had the same, thinking yesterday, working on the section.
into this document, Lumila, I think the… We have, situation where, having a dependency to a schema URL totally makes sense, and I think that's what you'd like to achieve.
But, we also have situations, I think, where… the importing a role, semantic convention registry that we are… on which we are building that has not been yet published, also makes sense, and in that case.
the registry rail is, like, the second choice.
To express a dependency.
In both cases, I think they have the… a need for an IV.
But, personally, I will keep the schema URL and registry URL two, options that can't be used together. They are exclusive from each other, but they can define precisely what we want to… on which… on what we want to depend.
Liudmila Molkova 00:09:17 Okay.
I… I understand, and let's make it happen.
Laurent Querel 00:09:29 On the same, topic. I think the… there is something that, in my opinion, is not, Entirely unclear in the… in the OTEP.
Let me see, its name, Oh, sorry, went sealed.
Yeah, repository URL.
part of the manifest, that's something I think you added.
Currently.
that could not be only the repository URL. I think that also has to contain, like we did, for example, for the… the registry URL.
Contain the subfolder, because the logist itself is not necessarily Right away, in the, in the root of this, repo. It will be a subfolder.
And we have that, for example, for open telemetry.
It's part of the model… The subdirectory model, and not directly the root.
Liudmila Molkova 00:10:47 Wait, so, when you resolve… when you… create a manifest. You're… Intent to publish it.
Why do you care about manifest if you don't publish the schema?
If you don't pop, you only need the… to… to… in your manifest, to express where things live. If you… Don't publish the schema.
Laurent Querel 00:11:12 So what is the purpose of the repository URL?
Liudmila Molkova 00:11:15 Oh, I was… sorry, it's, like, if you look into pretty much any package manager, it has some information where the code lives, just for humans, and that was my final point.
Laurent Querel 00:11:27 Exactly. So, to understand where the code lived.
Because we… if… and if we want to be a relatively consistent when we, we specify the parameter, TRA, TRA, oh, sorry, dash dash, a registry, URL. We specify also the subfolder, because where the code lives, or where the semantic convention registry lives, could be a subfolder. And the rest of the repo has nothing to do with the semantic convention.
Josh Suereth 00:11:58 Yeah, let me… let me do some translation here. So, Lyudmila, think about depending on something which isn't released yet. So, like, we do this, we do this in Rust with modules. I think, like, in, you can do this in a lot of package managers, depending on how they are. You can depend on another codebase if you're doing, like, testing or integration testing. So the idea would be, when I declare a dependency, I declare a dependency directly on the GitHub repo at a particular hash.
or a particular file, like, with… so I want to depend on the source, and I'm pulling in, like, a raw dependency.
at, like, a hash that hasn't been published yet, because I want to test my registry to see what it, like, it will look like with that change. You know, in Rust, we have an example where, like, there's, a breaking change with schemas, schemas, the automatic JSON schema thing.
One thing that I saw people do was they changed their crate dependency to depend right on a GitHub repo.
against the source code, and the dependency manager handles that, right? So if we, as Weaver, want to support, depending on another unpublished thing.
as, like, a temporary thing you can do, or an optional thing you can do. That's where, depending on a Git repo, makes sense. So instead of repo URL, we want it to be something like… where we could depend on an unpublished thing. But to Lauren's point, I don't think we want to encourage people to do that going forward for published repos. Like, we want publishing to be a bit more rigorous.
Going forward.
Liudmila Molkova 00:13:36 Sweet.
Josh Suereth 00:13:36 Somebody takes a manifest.
Liudmila Molkova 00:13:39 And all they hear when they take the manifest is results schema URL for this manifest file.
You're saying it's not… Necessary, it's not a required property.
Josh Suereth 00:13:53 Well, okay, can I… can we… do you mind if we move down to my proposal here? Yeah. Okay.
Laurent Querel 00:13:59 Yeah, just before you start, Josh, what you just explained.
is a different matter from what I explained in the second part.
Initially, first thought, we were talking about the dependencies. Totally agree with you.
Second part, I was talking about the repository URL, which is not… Relative to dependency?
It's something that Lumia added into the manifest.
That reflects the location where the current semantic convention is, in fact.
And what I'm saying is, we need… for the same reason that we need this, bracket model into the registry URL to specify where is The unreserved, or let's say the… we name it, right now, the… not the auto ring, but you use a different term, a definition.
Josh Suereth 00:14:59 Yep.
Laurent Querel 00:14:59 Registry?
Just for… to complete my previous explanation, it's a different topic in that case.
Josh Suereth 00:15:10 Right, I guess the… so, what I'm saying, Lauren, is I don't know if, like, we… let's talk about this, but, I don't know if we want to have… published schema, be just randomly, like, GitHub tags directory in GitHub.
Laurent Querel 00:15:27 No, no, no, no, yeah. The Puish Web, no. The.
Josh Suereth 00:15:30 Which means that resolved URL might not need to support that, only the definition, like, when you define… when you're pointing at a raw repository, would you need it?
Does that make sense?
Laurent Querel 00:15:42 No, there are… I disagree, but I, I don't understand why we… we will have… So, do you agree that the parameter, Dash air today.
require… The specification of not only a repository, But also, a subfolder.
In the future, obviously, we should be able to specify a schema URL that will be, in my opinion, a different parameter in the command line.
Josh Suereth 00:16:19 Don't think it should be a different parameter in the.
Laurent Querel 00:16:21 Okay, so if it's not a different parameter, why not? Then we should be able to recognize A rule registry?
Containing only definition.
Josh Suereth 00:16:33 Yeah. Like, today?
Laurent Querel 00:16:35 From a reserve registry, which is a manifest file that turns to different artifacts that we can download, right?
Josh Suereth 00:16:46 Yeah, so here's my proposal. Again, I have… I have some major revisions to the resolution algorithm. So this is my current proposal around manifests, alright? This is why I wanted to kind of jump the gun and go first, because I think a lot of what we're talking about, like, you should look at the code, in this PR that I have as a draft.
Laurent Querel 00:17:05 Okay.
Josh Suereth 00:17:06 Okay, so what I'd like is, in the future, when you send in a URL, The manifest is 100% optional today, okay? There doesn't need to be a manifest. You send a raw directory, Weaver works.
Going forward, I want that to issue a warning saying you should provide a manifest, because we're gonna use a manifest to do publishing.
Alright, secondly.
If… if we… if you send us, like, a directory, okay, we will look for a known file format for where manifest will live.
If you send us a file, we will assume that it's a manifest.
So if that URL that you send is a file, it gets loaded just as the manifest itself. And we treat the virtual directory as the, like, parent of that file, right?
Laurent Querel 00:17:53 Yes.
Josh Suereth 00:17:53 Okay, so that, that's, that's that. Then, if we get the manifest, we look inside. If you see Resolve Schema URL, We go resolve that schema, and we don't do any real resolution, because we don't need to. So, if you point Weaver at a resolved schema, it will do no resolution, because it just grabs in the resolved schema and renders it and does templating and all kind of stuff. We don't need to actually run this Crazy algorithm, because we can use the resolve schema.
Laurent Querel 00:18:24 That's real, I'm not sure I agree with it.
Josh Suereth 00:18:28 Okay, if there… let me… I'll finish, and then we can talk about that. If there is no resolve schema URL in the manifest, that means that this is still the definition schema, this is still a repo where you have definitions, and we will perform resolution… we will look for definition YAML files, and we will perform resolution there.
And this is generically how we load schemas. So, resolve schema formats, I think we should update versions, in the file format, so I can actually resolve version 1 and version 2 and handle things. I can show you the code that does this if you're curious, but I have this implemented.
Laurent Querel 00:19:09 Yeah, so…
Josh Suereth 00:19:10 What's… what's your concern here? Yeah.
Laurent Querel 00:19:12 No, several thoughts. I'm totally in agreement with it, sorry. No, no, I misinterpret something at some point, and no, I… Totally, align with this study.
Josh Suereth 00:19:26 Okay. Alright, so if that's the path forward for Manifest, let's come back to this discussion about repository URL. Like, in the manifest, what I'm suggesting is, you could drop repository URL if you wanted.
is that…
Laurent Querel 00:19:47 for… for a published, registry. I think that's what you… You need to edit, right?
Liudmila Molkova 00:19:53 Wait, okay, wait, so… I added this at the metadata. It's completely optional. It's just for human beings. In the… for the Josh's proposal, you… it's essentially the place where you've got this manifest from.
Josh Suereth 00:20:08 Yep.
Liudmila Molkova 00:20:09 So what… what you… Laurent, you want is the… the… in Josh's proposal, where you've got it from.
So it doesn't have to be there, you don't need it for dependency, it's more like a part of the process that resulted in you getting this manifest file.
Laurent Querel 00:20:27 It can still be preserved in…
Liudmila Molkova 00:20:30 As a part of the history. But it's, it's like, the… it's, it's not… Used in any part of the logic.
Laurent Querel 00:20:40 Do you agree, Lunila, that if I take… so, it's optional for a published repository.
Do you agree that if it's there, I can use this repository URL News Weaver.
use "-air, put the repository URL, and I should be able to reserve the corresponding semantic convention. Because the repository URL contains our points to Not the published version, but the original A repository containing the registry, right?
Liudmila Molkova 00:21:14 So if you get this file somehow, you already have it. You don't need it the second time.
Josh Suereth 00:21:21 Yeah, so Lauren, I would say this registry URL, if I have a raw repository, I wouldn't put it in my manifest.
Because.
Laurent Querel 00:21:29 Yes, yes, I agree.
Josh Suereth 00:21:31 And then we use whatever they told us where it was as the repos… like, Weaver can fill in the repository URL with the… with the URL.
Laurent Querel 00:21:38 I don't disagree with that.
Now, let's say we are in the context of we are downloading… A manifest style representing a reserved registry.
And in this reserve manifest file.
Optionally, we, if I understand well, we have a repository URL.
Liudmila Molkova 00:22:02 A registry URL, but yeah, I agreed, we'll have it. Okay, I was using the term just on the… no, we have a repository URL, I confirm.
Laurent Querel 00:22:13 If you look at your documentation.
you have the concept of repository URL.
Liudmila Molkova 00:22:19 This is in the hot tub.
And it's a separate word. Let me just remove the repository. Imagine it does not exist. We have, in the schemas.
In the resolved schema, we have registry, the URL.
Which is… So let's just remove this friend.
Josh Suereth 00:22:42 So, yeah, this repository URL is just kind of documentation for, like, error messages. I don't think this is… Because…
Laurent Querel 00:22:50 Okay.
Josh Suereth 00:22:50 Excellent.
Laurent Querel 00:22:51 It's 966, so it's right there, and I was interpreting it And I didn't change this section of the document.
I was interpreting it as exactly what you said.
the URL for people that are curious to look at the origin of this, artifact.
They are looking to this repository URL to see exactly the content of this repository before resolution.
So, if I understand well, you no longer have that into your documentation in Mina, right?
Liudmila Molkova 00:23:25 Not in Data, but in the resolved schema URL, there will be a thing that we now call registry URL.
That will be what you wanted to be the… URL.
That was used for the… That was the source of the registry.
Laurent Querel 00:23:46 Okay, with the, with the bracket, model, for example, different…
Liudmila Molkova 00:23:51 Whatever was provided in minus our option, I think. Okay, so in that case, we order you.
Josh Suereth 00:23:56 Okay, and Ludmelon, I still think I would… I would maybe change this name, but just, like, you know.
source, or, what… Maven had something with this, where you have, like, authors, you can have, you know, license, you can have, like, whatever we want to throw in here, that's what I viewed this as myself. Yeah. Documentation for people, like, hey, where do I contribute, where do I raise issues? Like, if we wanted to have links like that, I'm fine adding, maybe throw it in a meta section or something, or, like, an about, yeah, and then… then I think it… But I don't… I would… I would hate to just lose this, because we think it's confusing. I'd rather put it somewhere where people know it's non-normative, it's just, like, information for you to know about this thing.
Liudmila Molkova 00:24:42 Yeah.
Josh Suereth 00:24:43 Okay. Cool.
Also, thank you for, spending some time on this. I should have sent some updates about how we were duplicating efforts earlier. I didn't know we were, though.
Liudmila Molkova 00:24:57 That's okay.
Josh Suereth 00:24:58 Okay. Cool.
Anything else you want to call out for the multi-registry OTEP?
Liudmila Molkova 00:25:06 I was… we don't have time, but I, I just put it here so we have some space to talk with Lauren in case he has any thoughts, but we probably cannot.
Josh Suereth 00:25:18 Okay. Because I need to go in 5 minutes. 5 minutes, yeah, let's talk about… I think Arthur has to leave in 5 minutes. I actually… my conflict canceled, so I'm gonna stay for 30 minutes, because I think Lauren and I might have to walk through, some of… is Jeremy here, too? I think so.
I want to talk through… yeah, Jeremy's here, good. I want to talk through this, more people, the better, but, this is some significant refactoring, so we'll save that for later. Arthur, draft PR, registry infer. Tell us more.
Arthur Silva Sens 00:25:47 Yeah, we don't need to discuss much here, we don't even have that much time, but I just wanted to call your attention that the PR is open, and I have a few doubts, because Like, this is the biggest worst PR I've ever done in my life.
I put… I put some, questions, as a comment, a little bit down.
Josh Suereth 00:26:14 Only 700 likes, man. That's, you're still fine.
Arthur Silva Sens 00:26:19 Yeah, it's too much for me. I know it's okay for you, but, like, this is too much for me.
I have no idea if I put the code in the right place, I don't understand yet the difference between crates and modules.
I created some objects that I have a feeling I didn't need to, this YAML group.
But yeah.
I will… If you can read the PR later and just give feedback on the PR, that's already very good enough for me.
Jeremy Blythe 00:26:51 Yeah, I just had a quick look.
I think there's… There's potentially some A bit more overlap and some, like you pointed out, maybe some code that you… will take you below 700, I think.
Nice. There's a few, like.
Things that could be implemented as, like, In different ways, so… But I'm happy to, like, give this a first pass, it's… because it's very, sort of, closely related to lifejack stuff.
So, I can take that.
Arthur Silva Sens 00:27:24 Awesome, thank you.
Liudmila Molkova 00:27:26 Wow, you are creating, yeah, the… semantic convention definitions, and you're generating them in schema V1 that, we… are discussing to moving away from, but I… I think… I don't know what others think. For the purposes of this PR, I feel like if you generate something in V2, it might take a bit before It can be consumed. Or, no! It can be! It can be consumed right away!
Josh Suereth 00:27:55 Yeah, V2 translates back into V1 right now.
Arthur Silva Sens 00:28:00 let's a…
Josh Suereth 00:28:01 I might need to do V12 into… this V1 into V2, so you might actually be okay going both ways, but that's… that's a different story.
What I'll say, in terms of code organization, because I think that's a decent meta discussion to have now, the way to think about it is source is just the implementations of the CLI, and things that need to get reused between CLI commands, we want to have in crates.
major components we're putting in crates, because, like, for example, LiveCheck started as just live check, and now it's LiveCheck and MCP with Jeremy's PR. So, like, it'll be used in both.
So if we think infer might be something we want to use from, like, a public API, and from the CLI, and from MCP, we probably want to move it into a crate, so that your core engine is a reusable library from those three entry points. Does that make sense?
Arthur Silva Sens 00:28:56 Yeah, yeah, got it.
Jeremy Blythe 00:28:58 I'm kind of… I'll look at it in more detail, but it may be… That it doesn't warrant its own crate, but actually some of the code could be part of the live check crate.
That's kind of… But I, yeah, I'll take a look at that.
Arthur Silva Sens 00:29:15 Yeah, please comment on the PR. I try to use as much code from live check as possible.
I see that. But yeah, maybe I missed something.
Jeremy Blythe 00:29:25 No, it looks… It looks good, actually, like, the… That you can do that in 700 lines is pretty cool, actually.
Arthur Silva Sens 00:29:34 Awesome.
Laurent Querel 00:29:36 Yeah, that's cool. I will also look at the… Le Pierre on the FinTV.
Josh Suereth 00:29:44 I'm slightly jealous, man, I wish I could have done as much in 700 lines.
Arthur Silva Sens 00:29:51 I mean, I'm reusing the gRPC server from LifeCheck, I'm reusing the conversion from samples to samples from LifeCheck as well.
Josh Suereth 00:30:01 Yeah.
Yeah, that makes sense. Interesting. Okay.
Cool, so we'll follow up on… offline on that. If it's alright, can we move on to talking about the new resolution algorithm?
Because I feel like this is going to take 30 minutes. Yeah, thank you, Arthur.
Arthur Silva Sens 00:30:17 Yeah, no problem.
Josh Suereth 00:30:19 Okay.
Cool. So, basically the TLDR here is, I have a new resolution algorithm coming out, the idea is that we want to be able to load from a resolve schema as a dependency instead of from definitions, which means I had to significantly alter how the resolve process works, from a dependency standpoint. From a practical standpoint, the, like, group resolution trampolining that happens, where, like, you try to resolve attributes, if you have any errors, but you've resolved a few, you continue until you stop resolving and still have errors, that's still the same.
What I've done is I changed first how loading works. So there's an official way to load now that returns this loaded SEMCOM registry. So I'm gonna show this quick. A loaded SEMCOM registry is either you had… you loaded a resolved schema, a Resolved version 2 schema.
Or you have an unresolved repository.
Which is, I have a repository, I have a set of specs I've loaded, I have the imports, for that repository that I've extracted from the specs. We can talk about this structure later. I don't… I'm not super happy with it, but the more… the two important parts are, I have the specs I've loaded, I know where it came from, and I have the dependencies that are also loaded SEMCOM specs. So this is a recursive structure.
So I might have a recursive structure where I have unresolved, unresolved, and then resolved, or I have unresolved, and then, like, a resolved or a set of resolved, okay? This is designed for when we will have multiple dependencies, even though I still limit it to only allowing one dependency.
Per repo, until we're ready to go deeper.
Okay.
Laurent Querel 00:32:09 Makes sense.
Josh Suereth 00:32:10 Now, the second thing that happens is… during resolution, We will resolve our dependencies.
like, when we get an unresolved repo, the first thing we do is resolve our dependencies. Resolved dependencies turns into this structure.
Which is either I've resolved a dependency, and I have a V1 resolved schema or a V2 resolved schema.
So, if I depend on a raw thing, I will actually run a whole resolution process and get a resolve schema for my dependency prior to doing anything on the current thing I'm looking at.
Okay.
Whereas before, Laurent, what you were doing was you were just throwing all the groups together. Well, I don't have any raw groups, right?
So, as part of that, a resolved dependency has the ability for you to look up attributes per group.
Where you will get, like, we can still participate in resolution. These are all hidden, by the way, in the crate, so that they only impact it, resolution itself. But, we have this notion where I can look up group attributes to say, cool, someone referred to a group in their unresolved group, so I'll go look up all the attributes from my dependency that I need and pull them in. And V1 and V2, we're actually translating them back into V1 in a way that resolution will work.
We have this notion of an importable dependency, so I can import groups. This is used for the import section, right? So, if you have an imports clause in your manifest to say, I want to import these groups from my dependencies, we will just Throw out and look at our dependencies and figure out, okay, this group comes in here, this group comes in here.
I'm making the current algorithm work, but I think there's a lot for us to dive into later in terms of how we want dependencies to work. We're getting closer to the ability to have multiple dependencies here.
And I wanna, I wanna move that direction.
But not quite ready for it.
Okay.
Laurent Querel 00:34:24 Yeah.
Josh Suereth 00:34:24 So… so that's… that's the key… Architectural changes that need to happen.
So… Effectively, the resolve step, right, we resolve dependencies into resolved dependency, meaning we actually run a full resolution on them, instead of only grabbing raw groups.
then, we get this resolved dependency list. And then, when we need to import, we will import the groups from Resolve Dependency.
when we have an attribute reference, we will pull it from the resolved dependency list, if it isn't already in the existing set, like, local repo. So we check local repo first, then we check dependencies.
And if you… if we can't find a group, we look in the resolve dependency after we've checked local. If we can't find attributes, same thing.
We search the dependency in the order that they show up.
Now, again, since there can only be one, not a problem, but that's also something I put in the algorithm that I'm enforcing.
Okay.
Two do's. Where does it stand? Resolution actually works, and I'm passing a lot of tests.
What I'm not able to consistently pass is we actually… We're relying on the order of file loads for the order of our catalog registry.
In our test suite.
And with the new algorithm, I was using inconsistent sorting.
things. I was using some hash sets and things. So, I now have unstable catalog registries. So, I'm currently working on stabilizing the catalog registry and making sure it's always sorted, and so there's actually a new phase to resolve where I will take the catalog registry, I will sort every attribute in it.
And then I will manipulate all the attribute references to be updated against the new sorted order.
The second thing that, We need to figure out, is uniqueness gets weird.
because Uniqueness was looking for everything in the local group, I'm not checking Uniqueness in dependencies yet, so I need to actually add an explicit, make sure I have not defined a group that's defined in a dependency.
So that's… that's… I'm gonna… I'm gonna figure out how to do that. Unless we wanted to allow this. So that's, like, the question I have, is I have to go through a good bit of work to prevent it.
do we want to allow you to define a signal that has the same name as a dependency if you don't import that signal, right? So that you don't have a conflict.
Laurent Querel 00:37:05 So, so in the, in the multi-registry, analysis, that exists into the repo. We… I introduced the concept of reference with, Conflict resi- res- res- resolution.
Josh Suereth 00:37:22 Yep. Something like.
Laurent Querel 00:37:24 The name of the dependency, the registry that… on which we depend.
column, an ID.
That could be, a group ID.
And we know that at some point, like you said, we'd like to go into this direction to support more, elaborated, more complicated dependencies.
dependency graph.
So, maybe that's an opportunity.
Like you said, it's an effort to deduplicate.
Maybe it's an opportunity to go in this direction, even if we still support only pure, linear dependencies.
And not a real DAG, like we could imagine, or something even more… complicating than that.
Josh Suereth 00:38:15 Yeah, yeah, like, I'm, I do think we need to support some diamonds, because I think everyone will depend on semantic conventions.
Laurent Querel 00:38:23 Yes. So I think we need to… we need to find a way to support diamonds with that.
Josh Suereth 00:38:27 that… that's TBD, like, that's where, we can take… That resolved dependency chart, and then we can figure out how to deal with diamond hell in that.
Laurent Querel 00:38:38 Yeah. I described it a solution into the document, by the way. Maybe that's not the one that you want to retain, but .
Josh Suereth 00:38:46 Yeah.
Laurent Querel 00:38:46 Based on equivalence.
I think it's… it's… Yeah, good.
Josh Suereth 00:38:51 The thing here is we can go one of two ways. We can actually say in the model, if you override… like, if I were to create my own registry that is not Semcov, and I put a metric that has a Semcov name.
It should… it's… we should require it to be a refinement.
I cannot override it.
So I need a different group ID, even if the metric's the same name.
Because I can only refine semconv, because SEMCOV is somewhere… otherwise, that dependency doesn't make… like, I'm breaking the dependency. That is… that is Proposal 1.
Proposal two is we say, no, we're gonna need this flexibility, you can do whatever the hell you want, as long as you don't import the metric you're overriding. You can override it locally, and people know that you're not SemConv, because you have your own name and URL.
Even though CENCOMF shows up in your dependency chain.
we would… we would have to rely on Providence to tell us that this does not come from CENCOM.
So that's, that's option B. And I think I want to pick A or B. Right now, the reason I want to make the decision is B is what's implemented, because it was the easiest thing to get done, it was just, like, making it work.
A, I will have to do work for. And so I want us to make a decision so that I know which one to do.
Laurent Querel 00:40:15 So, when you import, in the import section of your custom registry, or the local registry.
Sometimes, because of the diamond situation.
You will have to specify exactly, for example, the matrix or the attribute group that you are importing, because maybe they are existing in two versions.
You are importing two dependencies.
Each of them are depending on the hotel registry.
but different version.
Maybe… or maybe they are using… The… they are totally independent dependencies.
But they happen to use the same metric ID, In that case, we have a conflict, and I think during the import, we should be able to specify which one we want to import. That means also that we need to detect this situation.
Yeah. And when we resolve, we present the error, and we recommend to specify among the values possibilities the name of the registry of the dependency that you have to import. That was the thinking.
Josh Suereth 00:41:33 Right.
Okay, I, I, I think I agree with that. So basically, to reiterate, if I import… A group from a dependency, and it conflicts with a local group, that would cause an error.
If I don't import the group, and I don't depend on it in any way.
And I have a conflict. That's not an error.
That's fine. That's acceptable.
the one… I do want to get into when we support multiple registries. I think the approach I want to take is actually linearizing versus, like, what Rust does, where you can have multiple competing dependencies.
I can go into why I think that's a better model. I think we're… we're more… we're closer to an object inheritance model, so I'd rather go with, like, what Python, Scala, those folks do, where… Every single dependency, every single thing with the same type has one version that gets chosen.
and that we rely on SEMCOM of those things to say, cool, if you try to resolve a diamond, deadly diamond, where you have two dependencies on two different versions, if they're not SEMConf comp compatible.
You get an error?
And if they are semconf compatible, we just take the latest one, and we can issue a warning to tell you that, maybe, or that's just part of dependency resolution. So, that's how I want to do diamonds later on.
But even in that example, what you were saying, like, applies, of, I can have repository A that I'm depending on, repository B I'm depending on, they both define a metric of the same type.
And I'm gonna pick one that I like, and use that one. And I will refer to it by its repository URL when I… and I might import that specific one.
But I wouldn't import the other one, and I need the ability to deal with that conflict. So that means that we should not consider this an error.
Laurent Querel 00:43:29 The refinement that was described into this document… imagine that we are in a situation, a big enterprise, and they have, An intermediary semantic conversion registry fully reserved, representing the… the interc files, common… Entities, or common matrix, and so on.
So now you are implementing the registry for microservice, or for an application.
And, so you… and you are also depending on another intermediary semantic convention registry for your team.
Because you share across a subset of microservices.
a set of other definitions. So you import the enterprise, you import the… the… the team, semantic convention.
In order to create your own custom… registry for your service. In that case, we could have a situation where In fact, we… we… we import, two times the same definitions.
And I was thinking that… the concept of equivalence, I think, could resolve a lot of situations without even asking the user to disambiguate.
Josh Suereth 00:44:56 Yes. So if…
Laurent Querel 00:44:57 If two definitions are strictly equivalent.
We don't have to, to ask for, conflict resolution.
And I think that, will solve a lot of situations, for example, for the open telemetry, which is a common node in many of those DAG, and that was the idea of equivalence. I don't know if that fits well with what you have in mind.
Josh Suereth 00:45:24 I think… I think we… that does… so, we can… with what I'm planning to do now, based on this discussion, I'm gonna go with B, but I think that's something we could add in the future. I wouldn't add… I'm not gonna add that immediately. That's, That's a bit…
Laurent Querel 00:45:39 Yeah. Yeah.
Josh Suereth 00:45:41 But also, immediately, what I'm… like, I'm not allowing multiple dependencies to, return a group, like, because we're only gonna allow one dependency.
Laurent Querel 00:45:51 Yeah, today, yes, definitely, yeah.
Josh Suereth 00:45:54 a thing that we can build and grow out. Okay, cool. But in terms of the… even with one dependency, I'm planning to start, like, change the semantics now, so… if you don't import… a group.
you can actually make your own group with the same ID, and it would be theoretically a conflict, but it's not a conflict because you haven't imported the other one, so everything's gravy.
So I think I'll go with that.
The other thing, the other things that are, that are going on here, I need a stable sort.
So, I'm literally, I know that we didn't do this initially, I don't know why. I'm adding ordered and partial ordered to almost everything in Weaver Semcov.
I… and I don't… we can figure out if the ordering is fine later. I don't care what the ordering is, it just has to be stable so that tests don't fail.
So…
Laurent Querel 00:46:52 I was thinking that I was already in this situation, but I probably, Because we, this, this problem of, having tests that, pass.
Every time, was definitively a sin.
And, I remember sorting a lot of, basically every intermediary, container part of the registry, if I remember well, were based on, Sorted, like a tree map thing.
And I was thinking that it was a stable sort. That was.
Josh Suereth 00:47:26 It's a hash map. You have one stable sort in there, or you have a couple stable sorts, but you're using… it uses more hash maps than tree maps. There's one stable sort, but it's the reference number of the attribute, not the order of the attribute, and so the way… the way the attributes are ordered is not… By their stable sort identity, it's by their hash ID.
And so the file, which is… kind of okay, but, it does mean that the order that we load files will change it. So I actually managed to trigger, inconsistent, attribute, where every time I'd run the test, the attribute catalog would flip around, and then the IDs would flip around.
Laurent Querel 00:48:08 Would that… would that be that you are sorting… because… Definitely that worked, initially. I think the difference between what worked before and what does not work for you is because you are not sorting everything.
Josh Suereth 00:48:22 No, no, no, no, no. No, it… you were sorting the files you loaded.
So you were sorting the groups prior to doing the resolution algorithm?
And so the attribute catalog would be consistent. But you weren't sorting the attributes as they go into the catalog.
because I'm resolving, like, a piece of the files as a dependency, and then I'm resolving another piece, my attribute catalog is different, because my attribute catalog doesn't include the groups from here, same order that you had.
Laurent Querel 00:48:50 Okay.
Josh Suereth 00:48:51 And so, I ran into instabilities, because actually, the attribute catalog that's created here, and then my dependency usage of it, pulling it in the way I am lazily, means I no longer have a consistent sort.
Laurent Querel 00:49:05 Okay, see.
Josh Suereth 00:49:06 So yeah, like, previously it relied on every single group being sorted by its ID.
Across every dependency.
Well, I don't… I don't have that anymore. I'm actually using Resolve Registry. I don't know what's going to be pulled in, because I only pull in on demand.
So, that's why I'm basically taking what you had for stable sort, and I'm expanding on it.
Laurent Querel 00:49:29 Okay, okay.
Josh Suereth 00:49:30 So the guarantee we will have is basically there will be a stable attribute… anytime you see an attribute catalog that comes out.
While we're building it, this isn't true, but, like, as a step, I'm going to sort the entire attribute catalog so they're always in the same order.
Laurent Querel 00:49:49 Yeah. So it's not dependent on the…
Josh Suereth 00:49:51 order of the files, like the group IDs that came in, it's actually dependent on the attributes intrinsically themselves.
Laurent Querel 00:49:58 Makes sense.
Josh Suereth 00:49:59 Yeah, okay.
But, The last thing is, we had inconsistencies in how we would load and resolve throughout our unit tests. Some… Unit tests used one loading mechanism. Some unit tests use a different loading mechanism.
Laurent Querel 00:50:17 When I created my new loading mechanism, I deprecated what I thought was the primary, because it's what's used in Source Weaver.
Josh Suereth 00:50:24 It turns out a lot of our unit tests weren't using that as their loading mechanism.
So what I'm doing is I'm actually going and cleaning up all our unit tests so that we have it consistently used the same loading actual method, and we use this same loading method I've created for doing dependencies.
Just to make sure it all works, and to make sure it's all tested everywhere. So actually, the resolution algorithms were not using the same loading algorithm that Weaver itself was using. And that's where I ran into this whole mess of fun.
Laurent Querel 00:50:58 We can imagine.
Yeah, that will be a gigantic, gigantic PR.
Josh Suereth 00:51:04 Yeah, it's gonna be… I wish it was only 700 lines.
Okay. So, basically, yeah, the stable resolve schema, in the future, the attribute catalog will be sorted.
The other thing with Rust-related issues, I'm gonna nick SemComf Registry completely as a type. I'm just gonna kill it. I don't think it's needed anymore. It's fully redundant with, with other things. The Weaver abstractions and set, what's happening as I go refactor is actually Schema Resolver is becoming kind of the Weaver abstraction, just without the policy engine. So you know how the Weaver abstraction we created is, like, there is a load step, then that loads and runs policies, then there's a resolve step.
Which does resolution and then runs after resolution policies, and possibly the comparison policies, if you have a comparison flag.
Schema Resolver in the resolving thing will have a load and a resolve step, that the only difference between it and the Weaver thing is just it doesn't have policies in it.
So, I think that's a good thing, but I'm just calling out that that's there. And I'm planning to nix anything that was confusing there. The other thing I'm running into, virtual directory lacked clone.
Because, it wasn't clear that you would, it tries to remember the temporary directory it had, and that temporary directory was not shareable. As a hack, what I've done is I am forcing a new virtual directory to be created every time I need to clone it.
Laurent Querel 00:52:39 Which means the temporary files.
Josh Suereth 00:52:43 just as a workaround to get stuff working, I'm planning to nix that, and make a new virtual directory structure that uses, like, an arc or something that is clonable, where… maybe just an RC, I don't even know if I need an ARC, but, you know, something.
If you have concerns with that, let me know, but I was gonna add clone into virtual directory.
Laurent Querel 00:53:07 No, I don't… no, I think if you had this, reference center thing, That, that makes totally sense.
Josh Suereth 00:53:15 Okay.
Cool.
That's it for, like, the major concerns. This is going to be a big… PR. So, from a architectural standpoint, if you have concerns around this loading definitions and the structure of resolved dependencies, let me know now.
Because that will save me a lot of time in, cleanup if I get it early. And then, apologies for the review that's incoming.
Laurent Querel 00:53:46 So I will look at the… so it's the 1136, right?
Josh Suereth 00:53:50 Yep, yep, you can see it's not passing tests at all, it's still unstable, it's still in a rough shape, but I'm getting you, I was passing all tests prior to, changing the loading part of resolve schema. So I was passing all of the, like, final tests we had, and I was passing all the multi-registry tests.
So, I think from the standpoint of, like, is the bones of the algorithm correct? Yes.
stable catalog.
once I get that sorted out and get some tests around it, this'll… this'll move quicker, but it's… it's a lot of… it's gonna be a lot of tedious reviews, because every single expected JSON file will change in the entire.
It's back. And that has been a pain in the ass.
Laurent Querel 00:54:43 Yes.
Okay, I will look at that definitively. Probably in multiple phases, I will start first with the… Yeah, the global approach, not entering into the detail of some algorithm, some function, but like you said, making sure that we are on the same page on the eye level.
do you have, some kind of with me, into the PR, describing the, the main, decision. You already explained a lot of them during the… this, SIG meeting, but maybe there are some others that are not… Maybe describe somewhere.
Josh Suereth 00:55:24 I haven't written them, and I haven't finished all the decisions yet, but yeah, I will make sure I do that soon. The file I would start with, by the way, is the dependency file, because if you look at the dependency file, you can see how I'm treating dependencies, and how I'm doing lookups.
into the architecture of how I'm doing things. The other thing is, in the PR, I have deprecated but not removed the previous resolution algorithm, and I am slowly removing it from the entire codebase, and then it's going to be gutted.
You can… so you can actually compare the difference between the new resolution algorithm and the old one. There's not a big… like, architecturally, it looks exactly the same, it calls the same methods.
There's the subtle differences in how it does imports, and the fact that I don't need to GC, because I've never imported things I don't want.
Laurent Querel 00:56:16 So huge, Josh, for working on this gigantic stuff. It's, That will put the Weaver in the next chapter, definitively, and I really appreciate all the work that you are doing there. It's incredible.
Josh Suereth 00:56:31 Thank you, man. Yeah, it's, It's been fun. It's just, it's also slightly frustrating, because it's… it's touching… I didn't think I would touch as much code as I am.
Laurent Querel 00:56:42 I mean, that's the core of the system, so I'm not surprised. Yeah. So, talking about that, and the OTEC, the previous discussion we had, I really think that these two things, I think the, the, the OTEP… I think we need to keep, it open.
Until we have, what you are doing done, in order to make sure that we… we validate it to some way, in some ways, the… the value scene that we… we are describing into the, the… into the OTEP.
Josh Suereth 00:57:26 That… yep, I think that makes a lot of sense. And I have been reading the OTEP and using it to drive changes in my PR, so you'll see some of the OTEP implemented in the PR.
you'll see two-dos for the rest of the OTEMP there, too.
Laurent Querel 00:57:42 Yeah.
Josh Suereth 00:57:44 Okay.
Laurent Querel 00:57:45 Excellent.
Jeremy Blythe 00:57:45 What's, one quick comment on… Rc versus ARC.
there was something that I was looking at to improve… to, like, remove more, cloning… in… there's quite a few places now where we're doing async, so, like, in the web server, in the… in the MCP, in live check, in… there's, like, quite a few places now.
And so if the registry that's returned from the Weaver thing.
Is… already in an arc, I think that will set us up, and will save us some time later on.
Josh Suereth 00:58:23 So, so, I'm trying to… I… I don't want to phrase this. The registry that's returned should be something you can put in an arc safely, and if you want to add send to it, you can. This… the issue I'm having with the, temporary directory crap… My hope is that you don't need that anymore.
Like, that thing is just gone.
But.
Laurent Querel 00:58:52 I mean, externally.
Josh Suereth 00:58:55 Yeah.
Jeremy Blythe 00:58:56 I think what I'm saying is, if… with the codebase as it is right now.
There's a bunch of cloning going on.
Because we can't, share these things so easily, with reference counting.
Yes. If you imagine that there was reference counting in there, and then we were able to share things better, we would need them to be async compatible. That's… that's kind of… that's my statement.
Yeah, right. Things will pass tests and things will work, but only because we're doing a bunch of cloning today.
Laurent Querel 00:59:28 Notice, Jeremy, that async does not mean that you can't use RC.
Rc will work still require arc?
I think, with single-core, we'll just, satisfied with RC.
But we… we are in a situation where we are in a work-stealing approach, so ARC will be required.
Jeremy Blythe 00:59:50 Yep.
Josh Suereth 00:59:51 Okay.
Jeremy Blythe 00:59:52 Could be for a later PR, I was just putting it out there, though.
Josh Suereth 00:59:55 No, no, I actually noticed that as well, because I was trying to do something with parallel, and I couldn't send. So, my thinking is we should start by marking data that we need to go between threads as send first.
Jeremy Blythe 01:00:09 Yep.
Josh Suereth 01:00:10 then… then we can start, like, re-architecting, like, core things to use ARC. So if we start marking things as send that you need to be send, we'll know where to put the arcs.
Jeremy Blythe 01:00:21 Okay.
Josh Suereth 01:00:21 Yeah, so if there's, like, a structure you need between things, add send to it, open a bug if we can't… like, if it doesn't work, or it violates something, or whatever. But it's similar to, like, adding ORD and partial ORD in my mind. Like, it's… we're expanding our codebase to be more useful in different things.
Jeremy Blythe 01:00:40 Yep, for sure.
Josh Suereth 01:00:42 Cool. But yeah, I'm… I'm amenable to this, Jeremy. I just didn't want to… I don't want to add Arc unless we don't need it, so if we can use the compiler to tell us exactly where the arcs have to go, that'd be ideal. Because Arc is a little frustrating to deal with in… when you don't want it.
At times.
Jeremy Blythe 01:01:00 Sure.
Josh Suereth 01:01:01 Yeah.
Jeremy Blythe 01:01:03 Right.
Josh Suereth 01:01:05 Alright. Oh, by the way, ARC is no less frustrating than RC, so instead of adding RC, I'll add ARC. But, But I don't want to add either unless we actually need them, yeah.
Jeremy Blythe 01:01:17 If we write log mutex.
Josh Suereth 01:01:21 Oh, God, yeah, that one's fun.
Jeremy Blythe 01:01:24 Alright.
Josh Suereth 01:01:25 Alright, thanks, everybody. Have a good day.
Laurent Querel 01:01:27 Nope.

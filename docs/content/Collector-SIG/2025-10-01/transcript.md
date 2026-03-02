SIG: Collector SIG
Date: 2025-10-01
Duration: 18 minutes
Zoom Recording URL: https://zoom.us/rec/share/V77gBz7SLEqrR5Twkx6NNmfeE0X8-ZSBYHhjvyxdtA2LiFAr-b-v-UhBAWypwboi.r6AjljKHf_o0qXFE
============================================================

## Zoom Recording Transcript

**Christos Markou** 01:20 Hello?
**Ondrej Dubaj** 01:29 Hate?
**Damien Mathieu** 01:37 Hey.
**Andrzej Stencel** 02:34 Hi, folks. Always Todd.
That's right first.
**Christos Markou** 02:48 Yeah, sure, first is mine.
let me quickly share my screen so I can talk over the items. So, yeah, hello, hello everyone. I wanted to share with, this SIG this, the work that is happening around, linking
metrics and… and signals in general that we emit from the collector, and, collector contribute, to SMAT conventions, which… which is something that we will need looking forward when we're going to, start,
adapting stabilized, metrics that are stable from semantconventional perspective, and also when we would like to stabilize, components, for example, specific receivers or whatever. So…
Yeah, two things to, note here is that, there is a proposal that I had, sent, I had raised an issue a couple of months ago about linking,
Components metrics, let's say scrapers or receivers metrics, to some unconventional definitions.
show us to provide a way, for us to, when we define a metric in a receiver, to have a way to reference, what is the correspond of SMAT conventions, if that exists already.
And at the same time, would like to have the option to define, yeah, would like to define the stability parametric, which is something that is already supported.
And I can talk about this, but what we miss right now is to have specific rules about how we can move through different stability levels and what should be the requirements. For example, when we would want to declare a metric in the collector as beta.
A requirement could be that this metric should have a reference to a semantic convention that is also beta already. Things like that. So, yeah, I think that, yeah, I was wondering if this should go through an RFC or whatever. I chatted with Andre this morning.
Yeah, I'm still not sure, but let me know if I should, take this.
Through an RFC. But for now, the… I think the best place to discuss this is this issue, and that was about…
Yeah, what I mentioned earlier, linking metrics to cement conventions. This can expand to attributes and other signals, but I'm focusing on metrics right now.
And…
Yeah, the latest update on this is that we already have support for defining stability level per metric. That was already supported by, mdataGen, the generator that we use.
But the stability level was not exposed in the documentation, so this PR allowed us to, generate docs that look like this, so this column here will have stability.
And, last week, I proposed to have this, to expand… to start using this in CollectorContrib, and, start adding stability for all the metrics, for all of the metrics that we have right now.
I sent a bunch of PRs, some of those are already merged. Then Alex
raised a concern about… concern about what should be the initial, stability level that we start with. I started with development, because it's the first one that OpenTelemetry allows, and but…
yeah, I'm not sure if… yeah, Alex answered the concern if they should be alpha, or something like this, and this took us to another issue, which is about defining the rules that we should
Follow about moving through the stability levels.
And, so right now.
the… we have support for defining stability parametric. There is this ongoing work about adding the baseline, which is development. I think it's fine for now to have development in all collector contrib components, and once we have specific guidelines, we can, of course.
change them altogether and go to Alpha, if we agree on this. And,
Next steps is to work on these guidelines, about stability levels, and…
at the same time, because this is probably something that we would need anyways, I have started, like, working on APR to start seeing how we could link our metrics to some other conventions. So, for now,
I've came up with something like this, an extra additional field, pointing to a specific reference, and, yeah, this would generate
table… would generate a documentation table with something like this, and you can… I know it's not ideal, I have thought about some validation that we might have. I already have some validation here about checking if the metric in the link
matches the metric of the name, and also if the version here of the semad conventions, link, matches the semad convention version that we define on Metadata YAML on the top scope.
Yeah, it's not ideal, but probably it's the best that we can do right now. An alternative could be, to use Weaver. I tried with Weaver as well.
I'm not sure if we've reached that mature yet, and also if we want to change this anyway. And, there is this proposal by Antoine already.
But also, this one, it is already, used in some components, but this one is used to generate, actually, the metadata.yaml. So, event… in any case, we still need to use mdata.gen, so…
probably we need support in MTAT again to define, the SMAT conventional reference.
Yeah, I think that's it more or less…
If there are questions or whatever, I can discuss this now, otherwise I would appreciate any feedback on the issue directly.
And I'll stop sharing.
**Andrzej Stencel** 09:21 This looks great, and thanks for doing this, Christus. I think it's very valuable. I don't have much to add to this. I don't see a need for an RFC at this moment, but…
If someone does, then please pick up. For now, maybe just working on the issues is good enough.
**Christos Markou** 09:44 Wow.
**Evan Bradley** 09:45 Oh, go on.
**Christos Markou** 09:47 Yeah, my, my only comment would be, I forgot to mention that, this could also apply on internal collector metrics. I don't know what is the… I checked there was an issue about internal collector metrics and stabilized those. I guess this will also, help us with that as well.
Sure, Evan.
Want to say something?
**Evan Bradley** 10:13 Oh, nothing big. I was just gonna echo what Andre said, that, it's a… I think this is a great, effort. I also don't think it needs an RFC. We're… we're pretty much just only working in mDataGen, this isn't, like, collector architecture, and I think it's… it's fairly uncontentious, and we could…
reverse it by just removing it later, so I think we're good to just proceed.
**Christos Markou** 10:41 Okay, cool, sounds good.
**Andrzej Stencel** 10:51 Okay, Mario's next.
**Christos Markou** 10:53 Yeah, cool.
**Moritz Wiesinger** 10:54 There it goes.
I started looking a bit into something that came up on this observability news site. There's a changelog comparison tool that can kind of show you per component if there's…
Breaking changes, or something like that.
And…
Man, I don't have the link available right now. But, yeah. Anyways, it kind of shows you whatever the changelog was for that specific component, and if there was specific changes to it.
But it has a big warning that…
component labels in the changelog are not standardized at all, and so it…
Works sometimes, and sometimes it doesn't.
And I actually had some, some other use cases as well already, to kind of compare, in our Dynatrace distribution.
against our manifest of components, what kind of changelog, we need to keep from contribute core collectors, and what we can drop.
In terms of components there?
And… Maybe it would be cool to actually standardize the component field in there.
And after some quick Slack discussion, and I'll share here…
There was already some discussion, and it seems Antoine basically did all the groundwork already. It's all there. Changelogen has support for validation and the configuration.
And GitHub Gen actually already supports generating the components.
So… If we check that here… I think there is… Where is it?
Here.
So there's already a subcommand in GitHubgen that you can call, and it will just go through,
The respective collector repo, and generate the whole list of components.
So I did that.
Just to see what it comes up with, and…
That is for Contrib… yeah, for contributor, I believe, and we already get a huge list. I haven't checked if it's extensive, or anything, or complete, but it looks pretty good already.
So, yeah, I wanted to kind of get some feedback if that's something we should follow and standardize, and…
validate against? So that we have kind of a more…
more machine-readable, changelog, which would be cool, I think.
And then my other question would be if the format of this is kind of good enough, or…
like, I don't know, classic example would be…
reduction processor. We'll always say in the component reduction processor, and not processor slash reduction.
Stuff like that.
I don't know if we want to kind of keep that this way, how it's generated right now, or if that should be somewhat…
I don't know, some other format.
There's also things like that done in the end.
Which could be weird, I don't know.
Yeah, Andre?
**Andrzej Stencel** 14:18 Yeah, I'm all for standardizing this. This would help everyone. And I like this format. To me, it's understandable, readable, more readable than
putting it together. It's…
Yeah, I think it's almost like the Go package name, but not exactly right, because really, the connector slash town is really connector slash count connector, but…
Yeah, I think it's good to drop that trailing connector thing. For other directory names, it's basically the directory name and the package, which I think is…
**Moritz Wiesinger** 14:57 I think so, yeah.
**Andrzej Stencel** 14:59 No.
**Evan Bradley** 15:02 Yeah, I also think this would be great. In particular, I would love if we could sort our changelog, like, public changelog entries for upstream, alphabetically. It kind of…
it feels, a little user-unfriendly how, right now, things are just kind of thrown about, and it can be a little hard if you're looking for a particular changelog to know where to look. Especially since the,
you know, everybody uses their own component name. I've been a little reluctant just because I don't want to, like, require contributors to understand these, but I think it should be straightforward enough.
But, yeah, you can see here, like, they're just all over. If I want to find, like, if I know that, the Prometheus receiver had a particular, change in this, or I want to check if it did, I have to go through the whole list. I can't just, like, scan to where I know it is in an alphabetical list. As for…
whether to use the directory name or the component name, I don't know. I do agree with Andre's point that, like, you can see Click House Exporter there, it's all, like, shoved together, one word. I think, especially for people who might not have English as the first language, that can probably be hard to parse.
So…
**Moritz Wiesinger** 16:15 I was wondering, this looks very alphabetical, but then this doesn't look at all like it's alphabetical. It's kind of weird.
**Evan Bradley** 16:21 I think… so, I think it's alphabetical by, The changelog entry.
Like, the file name.
**Moritz Wiesinger** 16:30 Oh, okay.
**Andrzej Stencel** 16:31 Golden is after internal, so… It's not really a… I think it's just a currency.
**Moritz Wiesinger** 16:36 events.
**Evan Bradley** 16:37 Yeah. But, that is a… that's close, though, but no, it's… I think…
**Moritz Wiesinger** 16:41 space.
**Evan Bradley** 16:41 the file name. So,
I think we just go through the files right now, but yes, I would love to sort this, and I'd love to make them standard so you know what to look for.
**Moritz Wiesinger** 16:51 Yeah, could be a… Probably a nice and easy enhancement for changelog Chain anyways.
Cool.
Yeah, I haven't written up an issue yet, but I will, I guess, in Collector Core, even though it kinda concerns everything. Or should we start in Contrib with this? I don't know. Contrip has far more components, so that's why I'm a bit wary.
**Andrzej Stencel** 17:18 I guess we can try with Core. It should be pretty straightforward there, and then move on with contract if we, like, straighten out any issues.
**Evan Bradley** 17:29 I think that's reasonable.
**Moritz Wiesinger** 17:32 Sounds good.
Thanks for the feedback.
**Evan Bradley** 17:41 Any other items from anyone?
Going once, going twice, floor's open if you… if you have anything.
Alright?
Say everyone in 3 weeks?
**Christos Markou** 18:03 Okay, bye.
**Ondrej Dubaj** 18:04 Thanks, honey.
